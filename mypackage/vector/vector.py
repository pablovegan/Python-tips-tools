"""This module contains the Vector class and the NormError exception.

Attributes:
    MAX_NORM (float): Maximum norm allowed for a Vector instance.

Note:
    Imports should follow always the same order:
        import python_standard_library

        import third_party_libraries

        import local_librariess
"""

from __future__ import annotations  # We import this module to use the Vector type annotation

import math
import warnings

import numpy as np


# Module level variables should be on top
# If a constant, its name shoud be UPPER_CASE_WITH_UNDERSCORES
MAX_NORM: float = 100


class NormError(ValueError):
    """Exception raised when a vector's norm is greater than MAX_NORM.

    Note:
        Custom exception classes are very useful for exception handling.

    Args:
        norm (float): The norm of the vector.

    Attributes:
        message (str): The message to display when the exception is raised.
    """

    def __init__(self, norm: float) -> None:
        message = f"Norm = {norm}, but it cannot be greater than {MAX_NORM}."
        super().__init__(message)


class Vector:
    """Two dimensional vector.

    Note:
        Remember that class docstrings in Google format should contain the arguments
        of the __init__ method and the attributes of the class, but not the methods.

    Args:
        x (float): first component of the vector.
        y (float): second component of the vector.

    Attributes:
        x (float): first component of the vector.
        y (float): second component of the vector.

    Raises:
        NormError: the norm of the vector is greater than MAX_NORM.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

        if self.norm > MAX_NORM:
            raise NormError(self.norm)

    def __repr__(self) -> str:
        """Return the vector representation.

        Note:
            The idea behind representations is that, when we execute the output of this
            function, we should create an identical copy of this object.

        Returns:
            The representation of the vector.

        Examples:
            We type the following to output the vector representation:

            >>> vector = Vector(1, 2)
            >>> vector
            Vector(1, 2)

        """
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        """This method is called when we want to print our vector as a string.

        Returns:
            The vector instance as a string.

        Examples:
            To call __str__ simply type

            >>> vector = Vector(1, 2)
            >>> print(vector)
            (1, 2)

        """
        return f"({self.x}, {self.y})"

    def __add__(self, other_vector: Vector) -> Vector:
        """Returns the addition vector of self and the other vector.

        Args:
            other_vector: Other vector (right hand side).

        Raises:
            TypeError: Not Vector passed in.

        Returns:
            The addition vector of self and the other vector.

        Examples:

            >>> Vector(1, 0) + Vector(0, 1)
            Vector(1, 1)

        """
        if not isinstance(other_vector, Vector):
            raise TypeError("You must pass in a Vector instance!")
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector(x, y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scalar value (right hand side).

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and the other vector/number.

        Examples:

            >>> Vector(1, 0) * 4
            Vector(4, 0)

            >>> Vector(1, 0) * Vector(1, 1)
            1

        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        if not isinstance(other, int | float):
            raise TypeError("You must pass in an int/float!")

        return Vector(self.x * other, self.y * other)

    def __eq__(self, other_vector: object) -> bool:
        """Check if the vectors have the same values up to some tolerance.

        Args:
            other_vector: Other vector (right hand side).

        Returns:
            True, if both vectors have the same values.
            False, else.

        Examples:

            >>> Vector(1, 0) == Vector(2, 0)
            False

        """
        if not isinstance(other_vector, Vector):
            return False
        # math.isclose returns true if the numbers are equal up to a small error
        equal_x: bool = math.isclose(self.x, other_vector.x, abs_tol=1e-10)
        equal_y: bool = math.isclose(self.y, other_vector.y, abs_tol=1e-10)
        return equal_x and equal_y

    @property
    def norm(self) -> float:
        """Returns the Euclidean norm of the vector.

        Note:
            Since the method doesn't accept any input, we can treat it as an attribute.
            To do that we just have to add the @property decorator on top of the method.

        Returns:
            float: the euclidean norm of the vector.

        Examples:
            >>> vector = Vector(1,0)
            >>> vector.norm
            1.0

        """
        return np.sqrt(self.x**2 + self.y**2)

    def projection(self, subspace: Vector | None = None) -> Vector:
        """By default projects the vector onto its first component. If a vector spanning
        a subspace is given, then the vector is projected along this subspace.

        Args:
            subspace (Vector, optional): vector that spans the subspace onto which to project
            the vector. Defaults to None.

        Returns:
            Vector: The projected vector.

        Examples:
            >>> Vector(1,1).projection(Vector(0,1))
            Vector(0.0, 1.0)

        """
        if subspace is None:
            warnings.warn(
                "No subspace given: the vector is projected onto the first component!", stacklevel=2
            )
            return Vector(self.x, 0)
        else:
            # Note that self is the instance of the Vector class
            projection_coef: float = (subspace * self) / subspace.norm**2
            return subspace * projection_coef
