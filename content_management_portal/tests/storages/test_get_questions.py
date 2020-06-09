from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.interactors.storages.dtos import \
    QuestionStatusDto
import pytest


@pytest.mark.django_db
def test_get_questions_when_from_value_is_more_than_available_return_empty_questions_list():
    # Arrange
    from_value = 0
    to_value = 1
    expected_question_status_dtos = []
    storage = QuestionStorageImplementation()

    # Act
    question_status_dtos = storage.get_questions(from_value=from_value, to_value=to_value)

    # Assert
    assert question_status_dtos == expected_question_status_dtos


@pytest.mark.django_db
def test_get_questions_return_question_status_dtos(
        rough_solution, test_case, prefilled_code, clean_solution,
        solution_approach
    ):
    # Arrange
    from_value = 0
    to_value = 1
    expected_question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=True
        )
    ]
    storage = QuestionStorageImplementation()

    # Act
    question_status_dtos = storage.get_questions(from_value=from_value, to_value=to_value)

    # Assert
    assert question_status_dtos == expected_question_status_dtos


@pytest.mark.django_db
def test_get_questions_return_question_status_dtos_when_no_rough_solutions(
        test_case, prefilled_code, clean_solution, solution_approach
    ):
    # Arrange
    from_value = 0
    to_value = 1
    expected_question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=False,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=True
        )
    ]
    storage = QuestionStorageImplementation()

    # Act
    question_status_dtos = storage.get_questions(from_value=from_value, to_value=to_value)

    # Assert
    assert question_status_dtos == expected_question_status_dtos

@pytest.mark.django_db
def test_get_questions_return_question_status_dtos_when_no_test_cases(
        rough_solution, prefilled_code, clean_solution, solution_approach
    ):
    # Arrange
    from_value = 0
    to_value = 1
    expected_question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=False,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=True
        )
    ]
    storage = QuestionStorageImplementation()

    # Act
    question_status_dtos = storage.get_questions(from_value=from_value, to_value=to_value)

    # Assert
    assert question_status_dtos == expected_question_status_dtos

@pytest.mark.django_db
def test_get_questions_return_question_status_dtos_when_no_prefilled_codes(
    rough_solution, test_case, clean_solution, solution_approach
    ):
    # Arrange
    from_value = 0
    to_value = 1
    expected_question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=False,
            solution_approach_status=True,
            clean_solution_status=True
        )
    ]
    storage = QuestionStorageImplementation()

    # Act
    question_status_dtos = storage.get_questions(from_value=from_value, to_value=to_value)

    # Assert
    assert question_status_dtos == expected_question_status_dtos

@pytest.mark.django_db
def test_get_questions_return_question_status_dtos_when_no_clean_solutions(
        rough_solution, test_case, prefilled_code, solution_approach
    ):
    # Arrange
    from_value = 0
    to_value = 1
    expected_question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=False
        )
    ]
    storage = QuestionStorageImplementation()

    # Act
    question_status_dtos = storage.get_questions(from_value=from_value, to_value=to_value)

    # Assert
    assert question_status_dtos == expected_question_status_dtos

@pytest.mark.django_db
def test_get_questions_return_question_status_dtos_when_no_solution_approach(
        rough_solution, test_case, prefilled_code, clean_solution
    ):
    # Arrange
    from_value = 0
    to_value = 1
    expected_question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=False,
            clean_solution_status=True
        )
    ]
    storage = QuestionStorageImplementation()

    # Act
    question_status_dtos = storage.get_questions(from_value=from_value, to_value=to_value)

    # Assert
    assert question_status_dtos == expected_question_status_dtos
