import pytest
from food_management.interactors.storages.dtos import FoodItemDto


@pytest.fixture
def food_item_dtos():
    food_item_dtos = [
        FoodItemDto(food_item_id=1, quantity=3),
        FoodItemDto(food_item_id=2, quantity=3),
        FoodItemDto(food_item_id=3, quantity=3)
    ]
    return food_item_dtos