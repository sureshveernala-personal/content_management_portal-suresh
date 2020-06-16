from abc import ABC
from abc import abstractmethod
from typing import List
from datetime import datetime
from food_management.exceptions.exceptions import InvalidMealId,\
    InvalidFoodItemId, FoodItemIdNotInMeal, InvalidQuantity,\
    DuplicateFoodItemId, MissedFoodItemIds, InvalidDatetime


class PresenterInterface(ABC):

    @abstractmethod
    def get_create_user_preference_meal(self, ):
        pass


    @abstractmethod
    def raise_invalid_meal_id_exception(self, error: InvalidMealId):
        pass


    @abstractmethod
    def raise_invalid_food_item_id_exception(self, error: InvalidFoodItemId):
        pass


    @abstractmethod
    def raise_invalid_food_item_id_not_in_meal_exception(
            self, error: FoodItemIdNotInMeal
        ):
        pass


    @abstractmethod
    def raise_invalid_quantity_exception(self, error: InvalidQuantity):
        pass


    @abstractmethod
    def raise_duplicate_food_item_id_exception(
            self, error: DuplicateFoodItemId
        ):
        pass


    @abstractmethod
    def raise_missed_food_item_ids_exception(self, error: MissedFoodItemIds):
        pass


    @abstractmethod
    def raise_invalid_date_time_exception(self, error: InvalidDatetime):
        pass
