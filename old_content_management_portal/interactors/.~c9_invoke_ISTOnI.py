from content_management_portal.interactors.storages.\
    rough_solution_storage_interface import RoughSolutionStorageInterface

class DeleteRoughSolutionInteractor:
    def __init__(
            self,
            rough_solution_storage: RoughSolutionStorageInterface,
        ):
        self.rough_solution_storage = rough_solution_storage

    def delete_rough_solution(self, rough_solution_id: int):
        is_valid_rough_solution_id = \
            self.rough_solution_storage.is_valid_rough_solution_id(
                rough_solution_id=rough_solution_id
            )
        is_invalid_rough_solution_id  = not is_valid_rough_solution_id
        if is_invalid_rough_solution_id
        
        self.rough_solution_storage.delete_rough_solution(
            rough_solution_id=rough_solution_id
        )
        return
