import pytest

from ects import score_to_ects


def test_hundred_gives_a():
    # Arrange
    score = 100
    # Act
    result = score_to_ects(score)
    # Assert
    assert result == "A"


@pytest.mark.parametrize("score, expected", [
    (90, "A"), (89, "B"), (82, "B"), (81, "C"), (74, "C"),
    (73, "D"), (64, "D"), (63, "E"), (60, "E"), (59, "F"), (0, "F"),
])
def test_boundaries_go_to_higher_range(score, expected):
    assert score_to_ects(score) == expected


def test_sixty_is_e_and_fifty_nine_is_f():
    assert score_to_ects(60) == "E"
    assert score_to_ects(59) == "F"


def test_fractional_score_between_bounds_falls_to_lower_grade():
    # 89.5 ще не доходить до 90 -> B
    assert score_to_ects(89.5) == "B"


@pytest.mark.parametrize("bad", [-1, 101])
def test_score_out_of_range_is_rejected(bad):
    with pytest.raises(ValueError, match="range 0..100"):
        score_to_ects(bad)


@pytest.mark.parametrize("bad", ["90", None, True])
def test_non_numeric_score_is_rejected(bad):
    with pytest.raises(ValueError, match="must be a number"):
        score_to_ects(bad)
