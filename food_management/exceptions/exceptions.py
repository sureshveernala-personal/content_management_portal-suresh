from typing import List
from datetime import datetime

class InvalidMealId(Exception):
    def __init__(self, meal_id: int):
        self.meal_id = meal_id


class InvalidFoodItemId(Exception):
    def __init__(self, food_item_ids: List[int]):
        self.food_item_ids = food_item_ids


class FoodItemIdNotInMeal(Exception):
    def __init__(self, food_item_ids: List[int]):
        self.food_item_ids = food_item_ids


class InvalidQuantity(Exception):
    def __init__(self, food_item_ids: List[int]):
        self.food_item_ids = food_item_ids


class DuplicateFoodItemId(Exception):
    def __init__(self, food_item_ids: List[int]):
        self.food_item_ids = food_item_ids


class MissedFoodItemIds(Exception):
    def __init__(self, food_item_ids: List[int]):
        self.food_item_ids = food_item_ids


class InvalidDatetime(Exception):
    def __init__(self, date_time: datetime):
        self.date_time = date_time