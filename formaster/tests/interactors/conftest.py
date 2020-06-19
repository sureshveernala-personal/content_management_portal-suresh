import pytest
from formaster.interactors.storages.dtos import FormDto, MCQResponseDTO


@pytest.fixture
def form_dto():
    form_dto = FormDto(form_id=1, is_live=True)

    return form_dto


@pytest.fixture
def mcq_response_dto():
    mcq_response_dto = MCQResponseDTO(question_id=1, option_id=1, user_id=1)

    return mcq_response_dto


@pytest.fixture
def fill_in_blanks_response_dto():
    fill_in_blanks_response_dto = \
        MCQResponseDTO(question_id=1, option_id=1, user_id=1)

    return fill_in_blanks_response_dto
