def get_answer_from_solution(solution: str) -> str:
    return _find_between(solution, "####", "####").strip()


def _find_between(s: str, first: str, last: str) -> str:
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""
