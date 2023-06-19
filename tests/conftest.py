"""The conftest.py file allows us to initialise test functions
that can be repeatedly used across several tests.
"""

import sys
from typing import Any
from typing import Dict

import pytest

from mypackage import Vector, Rotation, LinearMap


@pytest.fixture
def vector_fixture() -> Vector:
    """This vector can be used in tests as `vector_fixture`
    instead of `Vector(2, 1)`.
    """
    return Vector(2, 1)


@pytest.fixture
def rotation_fixture() -> LinearMap:
    """This linear map can be used in tests as `rotation_fixture`
    instead of `Rotation(5 / 2)`.
    """
    return Rotation(5 / 2)
