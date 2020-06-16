from dataclasses import dataclass


@dataclass
class FoodItemDto:
    food_item_id: str
    quantity: int
