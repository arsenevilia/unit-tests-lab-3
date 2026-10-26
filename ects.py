"""Переведення балів (0..100) у шкалу ECTS. Автор: Арсеньєв Ілля, група 3-41."""

AUTHOR = "Арсеньєв Ілля"

# (нижня межа діапазону, оцінка); межа входить у вищий діапазон
_SCALE = ((90, "A"), (82, "B"), (74, "C"), (64, "D"), (60, "E"), (0, "F"))


def score_to_ects(score):
    """Повертає літеру ECTS для балу 0..100.

    Бал поза 0..100 (або не число) -> ValueError.
    """
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise ValueError("score must be a number")
    if score < 0 or score > 100:
        raise ValueError("score must be in range 0..100")
    for lower, grade in _SCALE:
        if score >= lower:
            return grade
