from content_management_portal.storages.question_storage_implementation import\
    QuestionStorageImplementation
from content_management_portal.interactors.storages.dtos import \
    QuestionsDto, QuestionStatusDto
import pytest


@pytest.mark.django_db
def test_get_questions_when_offset_is_more_than_available_return_empty_questions_list():
    # Arrange
    offset = 1
    limit = 1
    question_status_dtos = []
    expected_questions_dto = QuestionsDto(
        total_questions=0,
        offset=offset,
        limit=limit,
        questions_list= question_status_dtos
    )
    storage = QuestionStorageImplementation()

    # Act
    questions_dto = storage.get_questions(offset=offset, limit=limit)

    # Assert
    assert questions_dto == expected_questions_dto


@pytest.mark.django_db
def test_get_questions_return_questions_dto(
        rough_solution, test_case, prefilled_code, clean_solution,
        solution_approach, hint
    ):
    # Arrange
    offset = 1
    limit = 1
    question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=True,
            hint_status=True
        )
    ]
    expected_questions_dto = QuestionsDto(
        total_questions=2,
        offset=offset,
        limit=limit,
        questions_list= question_status_dtos
    )
    storage = QuestionStorageImplementation()

    # Act
    questions_dto = storage.get_questions(offset=offset, limit=limit)

    # Assert
    assert questions_dto == expected_questions_dto


@pytest.mark.django_db
def test_get_questions_return_questions_dto_when_no_rough_solutions(
        test_case, prefilled_code, clean_solution, solution_approach,
        hint
    ):
    # Arrange
    offset = 1
    limit = 1
    question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=False,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=True,
            hint_status=True
        )
    ]
    expected_questions_dto = QuestionsDto(
        total_questions=2,
        offset=offset,
        limit=limit,
        questions_list= question_status_dtos
    )
    storage = QuestionStorageImplementation()

    # Act
    questions_dto = storage.get_questions(offset=offset, limit=limit)

    # Assert
    assert questions_dto == expected_questions_dto

@pytest.mark.django_db
def test_get_questions_return_questions_dto_when_no_test_cases(
        rough_solution, prefilled_code, clean_solution, solution_approach,
        hint
    ):
    # Arrange
    offset = 1
    limit = 1
    question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=False,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=True,
            hint_status=True
        )
    ]
    expected_questions_dto = QuestionsDto(
        total_questions=2,
        offset=offset,
        limit=limit,
        questions_list= question_status_dtos
    )
    storage = QuestionStorageImplementation()

    # Act
    questions_dto = storage.get_questions(offset=offset, limit=limit)

    # Assert
    assert questions_dto == expected_questions_dto

@pytest.mark.django_db
def test_get_questions_return_questions_dto_when_no_prefilled_codes(
    rough_solution, test_case, clean_solution, solution_approach, hint
    ):
    # Arrange
    offset = 1
    limit = 1
    question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=False,
            solution_approach_status=True,
            clean_solution_status=True,
            hint_status=True
        )
    ]
    expected_questions_dto = QuestionsDto(
        total_questions=2,
        offset=offset,
        limit=limit,
        questions_list= question_status_dtos
    )
    storage = QuestionStorageImplementation()

    # Act
    questions_dto = storage.get_questions(offset=offset, limit=limit)

    # Assert
    assert questions_dto == expected_questions_dto

@pytest.mark.django_db
def test_get_questions_return_questions_dto_when_no_clean_solutions(
        rough_solution, test_case, prefilled_code, solution_approach,
        hint
    ):
    # Arrange
    offset = 1
    limit = 1
    question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=False,
            hint_status=True
        )
    ]
    expected_questions_dto = QuestionsDto(
        total_questions=2,
        offset=offset,
        limit=limit,
        questions_list= question_status_dtos
    )
    storage = QuestionStorageImplementation()

    # Act
    questions_dto = storage.get_questions(offset=offset, limit=limit)

    # Assert
    assert questions_dto == expected_questions_dto

@pytest.mark.django_db
def test_get_questions_return_questions_dto_when_no_solution_approach(
        rough_solution, test_case, prefilled_code, clean_solution, hint
    ):
    # Arrange
    offset = 1
    limit = 1
    question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=False,
            clean_solution_status=True,
            hint_status=True
        )
    ]
    expected_questions_dto = QuestionsDto(
        total_questions=2,
        offset=offset,
        limit=limit,
        questions_list= question_status_dtos
    )
    storage = QuestionStorageImplementation()

    # Act
    questions_dto = storage.get_questions(offset=offset, limit=limit)

    # Assert
    assert questions_dto == expected_questions_dto

@pytest.mark.django_db
def test_get_questions_return_questions_dto_when_no_hints(
        rough_solution, test_case, prefilled_code, clean_solution,\
        solution_approach
    ):
    # Arrange
    offset = 1
    limit = 1
    question_status_dtos = [
        QuestionStatusDto(
            question_id=1,
            statement="short_text1",
            rough_solution_status=True,
            test_cases_status=True,
            prefilled_code_status=True,
            solution_approach_status=True,
            clean_solution_status=True,
            hint_status=False
        )
    ]
    expected_questions_dto = QuestionsDto(
        total_questions=2,
        offset=offset,
        limit=limit,
        questions_list= question_status_dtos
    )
    storage = QuestionStorageImplementation()

    # Act
    questions_dto = storage.get_questions(offset=offset, limit=limit)

    # Assert
    assert questions_dto == expected_questions_dto