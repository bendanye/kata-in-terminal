from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    id: str
    question: str
