"""All functions and methods should be tested. All of them!! This helps us
catch errors in our library and avoids propagating them into ever more
complicated functions.

We will use the library pytest, which allows to test multiple inputs for
each test function (using the @pytest.mark.parametrize decorator).
"""

from math import sqrt

import pytest
from numpy import pi as PI

from mylibrary import Vector, Rotation, Shear, LinearMap


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
def test_rotation(rotation: LinearMap, vector: Vector, result: Vector) -> None:
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
def test_inverse_rotation(rotation: LinearMap, vector: Vector, result: Vector) -> None:
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
def test_shear(shear: LinearMap, vector: Vector, result: Vector) -> None:
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
def test_inverse_shear(shear: LinearMap, vector: Vector, result: Vector) -> None:
    shear_vector = shear(vector)
    assert shear.inverse(shear_vector) == result
