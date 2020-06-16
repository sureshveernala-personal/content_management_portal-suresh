from food_management.interactors.storages.meal_storage_interface \
    import MealStorageInterface
from food_management.interactors.storages.dtos import FoodItemDto
from typing import List
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.exceptions.exceptions import InvalidMealId,\
    InvalidFoodItemId, FoodItemIdNotInMeal, InvalidQuantity,\
    DuplicateFoodItemId, MissedFoodItemIds, InvalidDatetime
from datetime import datetime


class CreateUserPreferenceMealInteractor():


    def __init__(self, meal_storage: MealStorageInterface):
        self.meal_storage = meal_storage


    def create_user_preference_meal_wrapper(
            self, user_id: int, meal_id: int,
            food_item_dtos: List[FoodItemDto],
            presenter: PresenterInterface
        ):
        try:
            self.create_user_preference_meal(
                user_id=user_id, meal_id=meal_id, food_item_dtos=food_item_dtos
            )
        except InvalidMealId as error:
            presenter.raise_invalid_meal_id_exception(error=error)
        except InvalidFoodItemId as error:
            presenter.raise_invalid_food_item_id_exception(error=error)
        except FoodItemIdNotInMeal as error:
            presenter.raise_invalid_food_item_id_not_in_meal_exception(
                error=error
            )
        except InvalidQuantity as error:
            presenter.raise_invalid_quantity_exception(error=error)
        except DuplicateFoodItemId as error:
            presenter.raise_duplicate_food_item_id_exception(error=error)
        except MissedFoodItemIds as error:
            presenter.raise_missed_food_item_ids_exception(error=error)
        except InvalidDatetime as error:
            presenter.raise_invalid_date_time_exception(error=error)


    def create_user_preference_meal(
            self, user_id: int, meal_id: int, food_item_dtos: List[FoodItemDto],
        ):
        self.meal_storage.validate_meal_id(meal_id=meal_id)
        self._validate_meal_date_time(meal_id=meal_id)
        food_item_ids = [
            food_item_dto.food_item_id
            for food_item_dto in food_item_dtos
        ]
        self._validate_food_item_ids(
            food_item_ids=food_item_ids, meal_id=meal_id
        )
        self._validate_quantity(food_item_dtos=food_item_dtos)
        is_update = self.meal_storage.is_update(
            user_id=user_id, meal_id=meal_id
        )

        if is_update:
            self.meal_storage.update_user_preference_meal(
                user_id=user_id, meal_id=meal_id, food_item_dtos=food_item_dtos
            )
        else:
            self.meal_storage.create_user_preference_meal(
                user_id=user_id, meal_id=meal_id, food_item_dtos=food_item_dtos
            )
        return


    def _validate_meal_date_time(self, meal_id: int):
        meal_deadline_date_time = self.meal_storage.get_meal_deadline_date_time(
            meal_id=meal_id
        )
        present_time = datetime.now()
        if meal_deadline_date_time <= present_time:
            raise InvalidDatetime(date_time=meal_deadline_date_time)


    def _validate_food_item_ids(
            self, meal_id: int, food_item_ids: List[int]
        ):
        total_food_item_ids = self.meal_storage.get_food_item_ids()
        invalid_food_item_ids = [
            food_item_id
            for food_item_id in food_item_ids
            if food_item_id not in total_food_item_ids
        ]
        if invalid_food_item_ids:
            raise InvalidFoodItemId(food_item_ids=invalid_food_item_ids)

        total_food_item_ids_in_meal = \
            self.meal_storage.get_food_item_ids_in_meal(meal_id=meal_id)
        food_item_ids_not_in_meal = [
            food_item_id
            for food_item_id in food_item_ids
            if food_item_id not in total_food_item_ids_in_meal
        ]
        if food_item_ids_not_in_meal:
            raise FoodItemIdNotInMeal(food_item_ids=food_item_ids_not_in_meal)

        self._validation_for_duplicate_food_item_ids(food_item_ids)
        missing_food_item_ids= \
            list(set(total_food_item_ids_in_meal) - set(food_item_ids))
        if missing_food_item_ids:
            raise MissedFoodItemIds(food_item_ids=missing_food_item_ids)

        return


    def _validate_quantity(self, food_item_dtos: List[FoodItemDto]):
        negative_quantity_food_item_ids = [
            food_item_dto.food_item_id
            for food_item_dto in food_item_dtos
            if self._is_negative(food_item_dto.quantity)
        ]
        if negative_quantity_food_item_ids:
            raise InvalidQuantity(
                food_item_ids=negative_quantity_food_item_ids
            )


    @staticmethod
    def _is_negative(number: int):
        is_negative = number < 0
        return is_negative


    @staticmethod
    def _validation_for_duplicate_food_item_ids(food_item_ids: List[int]):
        unique_food_item_ids = []
        duplicate_food_item_ids = []
        for food_item_id in food_item_ids:
            if food_item_id in unique_food_item_ids:
                duplicate_food_item_ids.append(food_item_id)
            else:
                unique_food_item_ids.append(food_item_id)
        if duplicate_food_item_ids:
            raise DuplicateFoodItemId(food_item_ids=duplicate_food_item_ids)
