def get_answer_from_solution(solution):
    return _find_between(solution, "####", "####").strip()


def _find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""
