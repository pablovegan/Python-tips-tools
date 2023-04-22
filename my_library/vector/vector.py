from __future__ import annotations  # We import this module to use the Vector2D type annotation

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


class Vector2D:
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
        >>> vector = Vector2D(1,2)
        >>> vector
        vector.Vector2D(1,2)

        Returns:
            The representation of the vector.
        """
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        """This method is called when we want to print our vector as a string.
        >>> vector = Vector2D(1,2)
        >>> print(vector)
        (1,2)

        Returns:
            The vector as a string.
        """
        return f"({self.x}, {self.y})"

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        """Returns the addition vector of the self and the other vector.

        Args:
            other_vector: Other vector (right hand side).

        Returns:
            The addition vector of the self and the other vector.
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

    @property
    def norm(self) -> float:
        """Returns the Euclidean norm of the vector. Since the method doesn't accept any input,
        we can treat it as an attribute. To do that we just have to add the @property decorator
        on top of the method.

        Returns:
            float: euclidean norm of the vector.
        """
        return np.sqrt(self.x**2 + self.y**2)

    def projection(self, component: int) -> Vector2D:
        """Project the vector onto the first or second component.

        Args:
            component (int): The subspace onto which to project the vector.
                Takes values 0 or 1.

        Raises:
            ValueError: Component must be either 0 or 1.

        Returns:
            Vector2D: The projected vector.
        """
        if component == 0:
            Vector2D(self.x, 0)
        elif component == 1:
            Vector2D(0, self.y)
        else:
            raise ValueError("Component must be either 0 or 1.")
