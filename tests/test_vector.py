import pytest

from my_library import Vector2D


V1 = Vector2D(0, 0)
V2 = Vector2D(-1, 1)
V3 = Vector2D(2.5, -2.5)


@pytest.mark.parametrize(
    ('vector_1', 'vector_2', 'result'),
    (
        (V1, V2, Vector2D(-1, 1)),
        (V1, V3, Vector2D(2.5, -2.5)),
        (V3, V2, Vector2D(1.5, -1.5)),
        (V3, V1, Vector2D(2.5, -2.5))
    )
)
def test_add(vector_1: Vector2D, vector_2: Vector2D, result: Vector2D) -> None:
    assert vector_1 + vector_2 == result


@pytest.mark.parametrize(
    ('vector_1', 'vector_2', 'result'),
    (
        (V1, V2, 0.0),
        (V1, V3, 0.0),
        (V3, V2, -5.0),
    )
)
def test_mul_vec(vector_1: Vector2D, vector_2: Vector2D, result: Vector2D) -> None:
    assert vector_1 * vector_2 == result


@pytest.mark.parametrize(
    ('variable_1', 'variable_2', 'result'),
    (
        (V1, 2.0, Vector2D(1.0, 0.0)),
        (V2, 2.0, Vector2D(-2.0, 2.0)),
        (V3, 2.0, Vector2D(5.0, -5.0)),
    )
)
def test_mul_float(variable_1: Vector2D, variable_2: Vector2D, result: float) -> None:
    assert variable_1 * variable_2 == result


@pytest.mark.skip(reason="Not implemented")
def test_norm() -> None:
    pass
