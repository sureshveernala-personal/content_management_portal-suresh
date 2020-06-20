from typing import List


class InvalidPassword(Exception):
    pass


class  InvalidQuestionId(Exception):
    pass


class InvalidSolutionIds(Exception):
    def __init__(self, solution_ids: List[int]):
        self.solution_ids = solution_ids


class SolutionIdsNotBelongsToQuestion(Exception):
    def __init__(self, solution_ids: List[int]):
        self.solution_ids = solution_ids
