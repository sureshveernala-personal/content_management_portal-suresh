import pytest
from content_management_portal.storages.test_case_storage_implementation \
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase


@pytest.mark.django_db
def test_swap_test_cases(test_case, test_cases_swap_details_dto):
    # Arrange
    storage = TestCaseStorageImplementation()

    # Act
    storage.swap_test_cases(
        test_cases_swap_details=test_cases_swap_details_dto
    )

    # Assert
    first_test_case = TestCase.objects.get(id=1)
    second_test_case = TestCase.objects.get(id=2)
    assert first_test_case.test_case_number == 2
    assert second_test_case.test_case_number == 1
