from abc import ABC, abstractmethod
from math import sin, cos, tan

from my_library.vector import Vector


class LinearTransform(ABC):
    """The matrix of our linear transform will consist on a list of rows with

    Args:
        matrix (list[list[float]]): matrix of our linear transformation.

    Attributes:
        matrix (list[list[float]]): the matrix of our linear transform.
        inv_matrix (list[list[float]]): the matrix of the inverse of our linear transform.
    """

    def __init__(self, matrix: list[list[float]]) -> None:
        self.matrix = matrix
        self.inv_matrix = self._get_inverse()  # we can call an undefined abstract method

    def __call__(self, vector: Vector) -> Vector:
        """Matrix times vector multiplication. The call method allows an instance of this class
        to behave as a function.

        Args:
            vector (Vector): Vector to transform.

        Returns:
            Vector: Transformed vector.

        Examples:
            We can define a linear transformation and then apply the tranform to a vector
            as if it were a function:

            >>> transformation = LinearTransform(some_matrix)
            >>> transformation(some_vector)

        """
        x = self.matrix[0][0] * vector.x + self.matrix[0][1] * vector.y
        y = self.matrix[1][0] * vector.x + self.matrix[1][1] * vector.y
        return Vector(x, y)

    @abstractmethod
    def _get_inverse(self) -> list[list[float]]:
        """The code for the abstract method will be specified inside each subclass.

        Because the method is not intended to be part of the user API, the convention is to
        begin the method's name with an underscore.

        Returns:
            list[list[float]]: Matrix of the inverse transformation.
        """
        ...  # the three dots mean "ellipsis"

    def inverse(self, vector: Vector) -> Vector:
        """Apply the inverse of our transformation to a vector.
        When giving a name to a method, you should take into account how would
        you name an instance of this class.

        Args:
            vector (Vector): Vector to transform.

        Returns:
            Vector: Transformed vector.

        Examples:
            If we create a transformation object, we can call the inverse method:

            >>> transformation = LinearTransform(some_matrix)
            >>> transformation.inverse(some_vector)

        """
        x = self.inv_matrix[0][0] * vector.x + self.inv_matrix[0][1] * vector.y
        y = self.inv_matrix[1][0] * vector.x + self.inv_matrix[1][1] * vector.y
        return Vector(x, y)


class Rotation(LinearTransform):
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


class Shear(LinearTransform):
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
