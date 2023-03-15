from typing import Protocol, List


class QuestionOption(Protocol):
    def select(self, questions: List[str]) -> List[str]:
        ...
