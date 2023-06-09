"""This module contains the LinearMap abstract class and two subclasses:
Rotation and Shear.

Examples:
    We can define a rotation linear map and then apply the transformation to a vector
    as if it were a function:

    >>> angle = 0.5
    >>> map = Rotation(angle)
    >>> map(Vector(1, 0))
    Vector(0.8775825618903728, 0.479425538604203)

    And with the inverse method, we can apply the inverse transformation

    >>> shear_angle = 0.5
    >>> map = Shear(shear_angle)
    >>> map.inverse(Vector(1, 1))
    Vector(-0.830487721712452, 1)

"""

from abc import ABC, abstractmethod
from math import sin, cos, tan

from mypackage.vector import Vector


class LinearMap(ABC):
    """This abstract class will serve us as a base for other linear maps that we
    will later especify in subclasses.

    Args:
        matrix (list[list[float]]): matrix of our linear map. It consists on a list
            of rows, each row being a list of the numbers in each column.

    Attributes:
        matrix (list[list[float]]): the matrix of our linear map.
        inv_matrix (list[list[float]]): the matrix of the inverse of our linear map.
    """

    def __init__(self, matrix: list[list[float]]) -> None:
        self.matrix = matrix
        self.inv_matrix = self._get_inverse()  # we can call an undefined abstract method

    def __call__(self, vector: Vector) -> Vector:
        """Apply the linear map to a vector (which translates into ordinary matrix
        times vector multiplication).

        Note:
            The call method allows an instance of this class to behave as a function.

        Args:
            vector (Vector): Vector to map.

        Returns:
            Vector: Transformed vector.
        """
        x = self.matrix[0][0] * vector.x + self.matrix[0][1] * vector.y
        y = self.matrix[1][0] * vector.x + self.matrix[1][1] * vector.y
        return Vector(x, y)

    @abstractmethod
    def _get_inverse(self) -> list[list[float]]:
        """Return the inverse of the linear map.

        Note:
            The code for the abstract method will be specified inside each subclass. Because
            this method is not defined in the LinearMap class, we won't be able to create an
            instance of this class.

            Also, because the method is not intended to be part of the user API, the convention
            is to begin the method's name with an underscore.

        Returns:
            list[list[float]]: Matrix of the inverse transformation.
        """
        ...  # the three dots mean "ellipsis"

    def inverse(self, vector: Vector) -> Vector:
        """Apply the inverse of our map to a vector.

        Note:
            When giving a name to a method, you should take into account how would
            you name an instance of this class. For example, if we create an instance
            called 'rotation', it is very clear to read `rotation.inverse(some_vector)`
            and guess that it applies the inverse rotation to the vector.

        Args:
            vector (Vector): Vector to transform.

        Returns:
            Vector: Transformed vector.
        """
        x = self.inv_matrix[0][0] * vector.x + self.inv_matrix[0][1] * vector.y
        y = self.inv_matrix[1][0] * vector.x + self.inv_matrix[1][1] * vector.y
        return Vector(x, y)


class Rotation(LinearMap):
    """Two dimensional rotation of a certain angle.

    Args:
        angle (float): angle of the rotation.

    Attributes:
        angle (float): angle of the rotation.
    """

    def __init__(self, angle: float) -> None:
        self.angle = angle
        matrix = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]
        super().__init__(matrix)

    def _get_inverse(self) -> list[list[float]]:
        return [[cos(self.angle), sin(self.angle)], [-sin(self.angle), cos(self.angle)]]


class Shear(LinearMap):
    """Shear transformation parallel to the x axis.

    Args:
        shear_angle (float): angle of the shear transformation.

    Attributes:
        shear_factor (float): cotangent of the shear angle.
    """

    def __init__(self, shear_angle: float) -> None:
        self.shear_factor = 1 / tan(shear_angle)  # shear factor is the cotangent of the shear angle
        matrix = [[1, self.shear_factor], [0, 1]]
        super().__init__(matrix)

    def _get_inverse(self) -> list[list[float]]:
        return [[1, -self.shear_factor], [0, 1]]
