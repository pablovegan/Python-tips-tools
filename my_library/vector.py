from __future__ import annotations

import numpy as np


MAX_NORM = 10


class NormError(ValueError):
    def __init__(self, norm: float, max_norm: float) -> None:
        self.message = f"Norm = {norm} but it cannot be grater than {max_norm}."
        super().__init__(self.message)


class Vector2D:
    """Create a 2D vector

    Arguments:
        x (float): first component
        y (float): second component

    Attributes:
        x (float): first component
        y (float): second component
    """

    def __init__(self, x, y):
        """Initialize the class

        Args:
            x (float): first component
            y (_type_): _description_

        Raises:
            NormError: Norm is bigger than maximum norm
        """
        self.x = x
        self.y = y

        if self.norm() > MAX_NORM:
            raise NormError(self.norm(), MAX_NORM)

        print(f"Vector ({x},{y}) initialized")

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        """Sum two vectors

        Args:
            other_vector (Vector2D): _description_

        Raises:
            TypeError: You must pass in a Vector2D instance!

        Returns:
            Vector2D: _description_
        """

        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")

        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other: Vector2D | float) -> Vector2D | float:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scaler value (rhs)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and the other vector/number.
        """
        if isinstance(other, Vector2D):
            result: float = self.x * other.x + self.y * other.y
            return result
        if not isinstance(other, int | float):
            raise TypeError("You must pass in an int/float!")
        return Vector2D(self.x * other, self.y * other)

    def __eq__(self, other_vector: object) -> bool:
        """Check if the vectors have the same values.

        Args:
            other_vector: Other vector (rhs)

        Returns:
            True, if the both vectors have the same values.
            False, else.
        """
        if not isinstance(other_vector, Vector2D):
            return False
        return self.x == other_vector.x and self.y == other_vector.y

    def norm(self) -> float:
        """Return the norm of the function

        Returns:
            float: _description_
        """
        vector_norm = np.sqrt(self.x**2 + self.y**2)

        return vector_norm
