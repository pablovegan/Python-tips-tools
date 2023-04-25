"""Imports should follow always the same order:
import python_standard_library

import third_party_libraries

import local_librariess
"""

from __future__ import annotations  # We import this module to use the Vector type annotation
from typing import Optional
import warnings
import math

import numpy as np


# Module constants should be on top and use UPPER_CASE_WITH_UNDERSCORES names
MAX_NORM = 100


class NormError(ValueError):
    """Custom exception class. Raised when the norm is greater than the maximum.
    Custom Exception classes are very useful for exception handling.

    Args:
        norm (float): The norm of the vector.
        max_norm (float): The maximum norm allowed.

    Attributes:
        message (str): The message to display when the exception is raised.
    """

    def __init__(self, norm: float, max_norm: float) -> None:
        self.message = f"Norm = {norm} but it cannot be greater than {max_norm}."
        super().__init__(self.message)


class Vector:
    """Class docstrings in Google format should have the arguments of the __init__ method
    and the attributes of the class, but not the methods.

    Args:
        x (float): first component of the vector
        y (float): second component of the vector

    Attributes:
        x (float): first component of the vector
        y (float): second component of the vector

    Raises:
        NormError: the norm of the vector is greater than the maximum norm.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

        if self.norm > MAX_NORM:
            raise NormError(self.norm, MAX_NORM)

    def __repr__(self) -> str:
        """Return the vector representation. We type the following to output
        the vector representation:
        >>> vector = Vector(1,2)
        >>> vector
        vector.Vector(1,2)

        Returns:
            The representation of the vector.
        """
        return f"vector.Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        """This method is called when we want to print our vector as a string.
        >>> vector = Vector(1,2)
        >>> print(vector)
        (1,2)

        Returns:
            The vector as a string.
        """
        return f"({self.x}, {self.y})"

    def __add__(self, other_vector: Vector) -> Vector:
        """Returns the addition vector of the self and the other vector.

        Args:
            other_vector: Other vector (right hand side).

        Returns:
            The addition vector of the self and the other vector.
        """
        if not isinstance(other_vector, Vector):
            raise TypeError("You must pass in a Vector instance!")
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector(x, y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scaler value (rhs)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and the other vector/number.
        """
        if isinstance(other, Vector):
            result: float = self.x * other.x + self.y * other.y
            return result
        if not isinstance(other, int | float):
            raise TypeError("You must pass in an int/float!")
        return Vector(self.x * other, self.y * other)

    def __eq__(self, other_vector: object) -> bool:
        """Check if the vectors have the same values.

        Args:
            other_vector: Other vector (rhs)

        Returns:
            True, if the both vectors have the same values.
            False, else.
        """
        if not isinstance(other_vector, Vector):
            return False
        # math.isclose returns true or false if the numbers are equal up to a small error
        equal_x: bool = math.isclose(self.x, other_vector.x, abs_tol=1e-10)
        equal_y: bool = math.isclose(self.y, other_vector.y, abs_tol=1e-10)
        return equal_x and equal_y

    @property
    def norm(self) -> float:
        """Returns the Euclidean norm of the vector. Since the method doesn't accept any input,
        we can treat it as an attribute. To do that we just have to add the @property decorator
        on top of the method.

        Returns:
            float: euclidean norm of the vector.
        """
        return np.sqrt(self.x**2 + self.y**2)

    def projection(self, subspace: Optional[Vector] = None) -> Vector:
        """By default projects the vector onto its first component. If a vector spanning a subspace
        is given, then the vector is projected along this subspace.

        Args:
            subspace (Vector, optional): vector that spans the subspace onto which to project the vector.
                Defaults to None.

        Returns:
            Vector: The projected vector.
        """
        if subspace is None:
            warnings.warn(
                "If no subspace is given, the vector is projected onto the first component!"
            )
            return Vector(self.x, 0)
        else:
            # Note that self is instance of the Vector class
            projection_coef: float = (
                subspace * self
            ) / subspace.norm**2
            return subspace * projection_coef
