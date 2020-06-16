from food_management.interactors.storages.meal_storage_interface import\
    MealStorageInterface
from food_management.interactors.create_user_preference_meal_interactor import\
    CreateUserPreferenceMealInteractor
from food_management.interactors.presenters.presenter_interface import\
    PresenterInterface
from food_management.exceptions.exceptions import InvalidMealId,\
    InvalidFoodItemId
from food_management.interactors.storages.dtos import FoodItemDto
from unittest.mock import create_autospec, patch
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
import datetime
from freezegun import freeze_time


def test_create_user_preference_meal_with_invalid_meal_id(food_item_dtos):
    # Arrange
    meal_id = 1
    user_id = 1
    expected_meal_id = 1
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.validate_meal_id.side_effect = InvalidMealId(meal_id=1)
    presenter.raise_invalid_meal_id_exception.side_effect = NotFound

    with pytest.raises(NotFound):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter, meal_id=meal_id, user_id=user_id,
            food_item_dtos=food_item_dtos
        )

    # Assert
    kwargs = presenter.raise_invalid_meal_id_exception.call_args.kwargs
    error = kwargs['error']
    meal_id = error.meal_id
    assert meal_id == expected_meal_id


@freeze_time('2020-01-01')
def test_create_user_preference_meal_with_invalid_food_item_id(food_item_dtos):
    # Arrange
    meal_id = 1
    user_id = 1
    expected_food_item_ids = [2, 3]
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.get_food_item_ids.return_value = [1]
    meal_storage.get_meal_deadline_date_time.return_value = \
        datetime.datetime(2020,2,2)
    presenter.raise_invalid_food_item_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter, meal_id=meal_id, user_id=user_id,
            food_item_dtos=food_item_dtos
        )

    # Assert
    kwargs = presenter.raise_invalid_food_item_id_exception.call_args.kwargs
    error = kwargs['error']
    food_item_ids = error.food_item_ids
    assert food_item_ids == expected_food_item_ids


@freeze_time('2020-01-01')
def test_create_user_preference_meal_with_food_item_id_not_in_meal(
        food_item_dtos
    ):
    # Arrange
    meal_id = 1
    user_id = 1
    expected_food_item_ids = [2, 3]
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.get_food_item_ids.return_value = [1, 2, 3]
    meal_storage.get_food_item_ids_in_meal.return_value = [1]
    meal_storage.get_meal_deadline_date_time.return_value = \
        datetime.datetime(2020,2,2)
    presenter.raise_invalid_food_item_id_not_in_meal_exception.side_effect = \
        BadRequest

    with pytest.raises(BadRequest):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter, meal_id=meal_id, user_id=user_id,
            food_item_dtos=food_item_dtos
        )

    # Assert
    kwargs = presenter.raise_invalid_food_item_id_not_in_meal_exception\
                      .call_args.kwargs
    error = kwargs['error']
    food_item_ids = error.food_item_ids
    assert food_item_ids == expected_food_item_ids


@freeze_time('2020-01-01')
def test_create_user_preference_meal_with_invalid_quantity():
    # Arrange
    meal_id = 1
    user_id = 1
    food_item_dtos = [
        FoodItemDto(food_item_id=1, quantity=3),
        FoodItemDto(food_item_id=2, quantity=-3),
        FoodItemDto(food_item_id=3, quantity=-1)
    ]
    expected_food_item_ids = [2, 3]
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.get_food_item_ids.return_value = [1, 2, 3]
    meal_storage.get_food_item_ids_in_meal.return_value = [1, 2, 3]
    meal_storage.get_meal_deadline_date_time.return_value = \
        datetime.datetime(2020,2,2)
    presenter.raise_invalid_quantity_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter, meal_id=meal_id, user_id=user_id,
            food_item_dtos=food_item_dtos
        )

    # Assert
    kwargs = presenter.raise_invalid_quantity_exception.call_args.kwargs
    error = kwargs['error']
    food_item_ids = error.food_item_ids
    assert food_item_ids == expected_food_item_ids


@freeze_time('2020-01-01')
def test_create_user_preference_meal_when_duplicate_food_item_ids():
    # Arrange
    meal_id = 1
    user_id = 1
    expected_food_item_ids = [1]
    food_item_dtos = [
        FoodItemDto(food_item_id=1, quantity=3),
        FoodItemDto(food_item_id=1, quantity=3),
        FoodItemDto(food_item_id=3, quantity=3)
    ]
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.get_food_item_ids.return_value = [1, 2, 3]
    meal_storage.get_food_item_ids_in_meal.return_value = [1, 2, 3]
    meal_storage.get_meal_deadline_date_time.return_value = \
        datetime.datetime(2020,2,2)
    presenter.raise_duplicate_food_item_id_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter, meal_id=meal_id, user_id=user_id,
            food_item_dtos=food_item_dtos
        )

    # Assert
    kwargs = presenter.raise_duplicate_food_item_id_exception.call_args.kwargs
    error = kwargs['error']
    food_item_ids = error.food_item_ids
    assert food_item_ids == expected_food_item_ids


@freeze_time('2020-01-01')
def test_create_user_preference_meal_when_missing_food_item_ids(
        food_item_dtos
    ):
    # Arrange
    meal_id = 1
    user_id = 1
    expected_food_item_ids = [4, 5]
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.get_food_item_ids.return_value = [1, 2, 3, 4, 5, 6]
    meal_storage.get_food_item_ids_in_meal.return_value = [1, 2, 3, 4, 5]
    meal_storage.get_meal_deadline_date_time.return_value = \
        datetime.datetime(2020,2,2)
    presenter.raise_missed_food_item_ids_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter, meal_id=meal_id, user_id=user_id,
            food_item_dtos=food_item_dtos
        )

    # Assert
    kwargs = presenter.raise_missed_food_item_ids_exception.call_args.kwargs
    error = kwargs['error']
    food_item_ids = error.food_item_ids
    assert food_item_ids == expected_food_item_ids


@freeze_time('2020-02-02')
def test_create_user_preference_meal_with_invalid_date_time(food_item_dtos):
    # Arrange
    meal_id = 1
    user_id = 1
    expected_date_time = datetime.datetime(2020, 1, 1)
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.get_meal_deadline_date_time.return_value = expected_date_time
    presenter.raise_invalid_date_time_exception.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter, meal_id=meal_id, user_id=user_id,
            food_item_dtos=food_item_dtos
        )

    # Assert
    kwargs = presenter.raise_invalid_date_time_exception.call_args.kwargs
    error = kwargs['error']
    date_time = error.date_time
    assert date_time == expected_date_time


@freeze_time('2020-01-01')
def test_create_user_preference_meal_when_update(food_item_dtos):
    # Arrange
    meal_id = 1
    user_id = 1
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.get_food_item_ids.return_value = [1, 2, 3]
    meal_storage.get_food_item_ids_in_meal.return_value = [1, 2, 3]
    meal_storage.is_update.return_value = True
    meal_storage.update_user_preference_meal.return_value = None
    meal_storage.get_meal_deadline_date_time.return_value = \
        datetime.datetime(2020,2,2)

    # Act
    interactor.create_user_preference_meal_wrapper(
        presenter=presenter, meal_id=meal_id, user_id=user_id,
        food_item_dtos=food_item_dtos
    )

    # Assert
    meal_storage.update_user_preference_meal.assert_called_once_with(
        meal_id=meal_id, user_id=user_id, food_item_dtos=food_item_dtos
    )


@freeze_time('2020-01-01')
def test_create_user_preference_meal_when_create(food_item_dtos):
    # Arrange
    meal_id = 1
    user_id = 1
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateUserPreferenceMealInteractor(meal_storage=meal_storage)
    meal_storage.get_food_item_ids.return_value = [1, 2, 3]
    meal_storage.get_food_item_ids_in_meal.return_value = [1, 2, 3]
    meal_storage.is_update.return_value = False
    meal_storage.create_user_preference_meal.return_value = None
    meal_storage.get_meal_deadline_date_time.return_value = \
        datetime.datetime(2020,2,2)

    # Act
    interactor.create_user_preference_meal_wrapper(
        presenter=presenter, meal_id=meal_id, user_id=user_id,
        food_item_dtos=food_item_dtos
    )

    # Assert
    meal_storage.create_user_preference_meal.assert_called_once_with(
        meal_id=meal_id, user_id=user_id, food_item_dtos=food_item_dtos
    )
