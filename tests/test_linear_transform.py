"""We use the @pytest.mark.parametrize decorator to tell the test functions
what inputs to test when we run pytest. This inputs should include the inputs
for function we want to test (for example the __add__ method) as well as the expected result.
"""
from math import sqrt

import pytest
from numpy import pi as PI

from my_library import Vector, Rotation, Shear, LinearTransform


V1 = Vector(2, 1)
V2 = Vector(1, -1)

R1 = Rotation(PI / 2)
R2 = Rotation(PI / 4)

S1 = Shear(PI / 4)
S2 = Shear(PI / 3)


@pytest.mark.parametrize(
    ('rotation', 'vector', 'result'),
    (
        (R1, V1, Vector(-1, 2)),
        (R1, V2, Vector(1, 1)),
        (R2, V1, Vector(1 / sqrt(2), 3 / sqrt(2))),
        (R2, V2, Vector(sqrt(2), 0))
    )
)
def test_rotation(rotation: LinearTransform, vector: Vector, result: Vector) -> None:
    assert rotation(vector) == result


@pytest.mark.parametrize(
    ('rotation', 'vector', 'result'),
    (
        (R1, V1, V1),
        (R1, V2, V2),
        (R2, V1, V1),
        (R2, V2, V2)
    )
)
def test_inverse_rotation(rotation: LinearTransform, vector: Vector, result: Vector) -> None:
    rotated_vector = rotation(vector)
    assert rotation.inverse(rotated_vector) == result


@pytest.mark.parametrize(
    ('shear', 'vector', 'result'),
    (
        (S1, V1, Vector(3, 1)),
        (S1, V2, Vector(0, -1)),
        (S2, V1, Vector(2 + 1 / sqrt(3), 1)),
        (S2, V2, Vector(1 - 1 / sqrt(3), -1))
    )
)
def test_shear(shear: LinearTransform, vector: Vector, result: Vector) -> None:
    assert shear(vector) == result


@pytest.mark.parametrize(
    ('shear', 'vector', 'result'),
    (
        (S1, V1, V1),
        (S1, V2, V2),
        (S2, V1, V1),
        (S2, V2, V2)
    )
)
def test_inverse_shear(shear: LinearTransform, vector: Vector, result: Vector) -> None:
    shear_vector = shear(vector)
    assert shear.inverse(shear_vector) == result
