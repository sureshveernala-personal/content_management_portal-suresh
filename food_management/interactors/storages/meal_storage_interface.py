from abc import ABC
from abc import abstractmethod
from typing import List
from food_management.interactors.storages.dtos import FoodItemDto


class MealStorageInterface(ABC):


    @abstractmethod
    def create_user_preference_meal(
            self, user_id: int,
            meal_id: int, food_item_dtos: List[FoodItemDto]
        ):
        pass


    @abstractmethod
    def update_user_preference_meal(
            self, user_id: int,
            meal_id: int, food_item_dtos: List[FoodItemDto]
        ):
        pass


    @abstractmethod
    def validate_meal_id(self, meal_id: int):
        pass


    @abstractmethod
    def get_meal_deadline_date_time(self, meal_id: int):
        pass


    @abstractmethod
    def get_food_item_ids(self):
        pass


    @abstractmethod
    def get_food_item_ids_in_meal(self, meal_id: int):
        pass


    @abstractmethod
    def is_update(self, user_id: int, meal_id: int):
        pass
