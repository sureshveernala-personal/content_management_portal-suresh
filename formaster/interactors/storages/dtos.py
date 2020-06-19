from dataclasses import dataclass


@dataclass
class FormDto:
    form_id: int
    is_live: bool


@dataclass
class MCQResponseDTO:
    user_id: int
    question_id: int
    option_id: int


@dataclass
class FillInBlanksResponseDTO:
    user_id: int
    question_id: int
    response_text: str
