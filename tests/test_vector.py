"""All functions and methods should be tested. All of them!! This helps us catch errors
in our library and avoids propagating them into ever more complicated functions.

We will use the library pytest, which allows to test multiple inputs for each test function.
For that we use the @pytest.mark.parametrize decorator. This inputs should include the inputs
for function we want to test (for example the __add__ method) as well as the expected result.
"""

import math

import pytest

from mylibrary import Vector


V1 = Vector(0, 0)
V2 = Vector(-1, 1)
V3 = Vector(2.5, -2.5)
V4 = Vector(2, 1)


@pytest.mark.parametrize(
    ('vector_1', 'vector_2', 'result'),
    (
        (V1, V2, Vector(-1, 1)),
        (V1, V3, Vector(2.5, -2.5)),
        (V3, V2, Vector(1.5, -1.5)),
        (V3, V1, Vector(2.5, -2.5))
    )
)
def test_add(vector_1: Vector, vector_2: Vector, result: Vector) -> None:
    assert vector_1 + vector_2 == result


@pytest.mark.parametrize(
    ('vector_1', 'vector_2', 'result'),
    (
        (V1, V2, 0.0),
        (V1, V3, 0.0),
        (V3, V2, -5.0),
    )
)
def test_mul_vec(vector_1: Vector, vector_2: Vector, result: Vector) -> None:
    assert vector_1 * vector_2 == result


@pytest.mark.parametrize(
    ('variable_1', 'variable_2', 'result'),
    (
        (V1, 2.0, Vector(0.0, 0.0)),
        (V2, 2.0, Vector(-2.0, 2.0)),
        (V3, 2.0, Vector(5.0, -5.0)),
    )
)
def test_mul_float(variable_1: Vector, variable_2: Vector, result: float) -> None:
    assert variable_1 * variable_2 == result


@pytest.mark.parametrize(
    ('vector', 'result'),
    (
        (V1, 0),
        (V2, math.sqrt(2)),
        (Vector(1, 2), math.sqrt(5))
    )
)
def test_norm(vector: Vector, result: float) -> None:
    assert vector.norm == result


@pytest.mark.parametrize(
    ('vector', 'subspace', 'result'),
    (
        (V1, None, Vector(0, 0)),
        (V2, None, Vector(-1, 0)),
        (V4, Vector(1, 1), Vector(1.5, 1.5)),
        (V2, Vector(1, 1), Vector(0, 0))
    )
)
def test_projection(vector: Vector, subspace: Vector | None, result: Vector) -> None:
    assert vector.projection(subspace) == result


@pytest.mark.skip(reason="Not implemented")
def test_whatever_method() -> None:
    pass
