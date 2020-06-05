import pytest
from content_management_portal.storages.prefilled_code_storage_implementation \
    import PrefilledCodeStorageImplementation


@pytest.mark.django_db
def test_get_prefilled_code_ids_when_no_prefilled_codes_return_empty_list():
    # Arrange
    expected_rough_solutios = []
    storage = PrefilledCodeStorageImplementation()

    # Act
    prefilled_codes = storage.get_prefilled_code_ids()

    # Assert
    assert prefilled_codes == expected_rough_solutios

@pytest.mark.django_db
def test_get_prefilled_code_ids_when_prefilled_codes_availble_return_list(prefilled_code):
    # Arrange
    expected_rough_solutios = [1]
    storage = PrefilledCodeStorageImplementation()

    # Act
    prefilled_codes = storage.get_prefilled_code_ids()

    # Assert
    assert prefilled_codes == expected_rough_solutios
