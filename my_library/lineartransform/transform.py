from abc import ABC, abstractmethod
from math import sin, cos

from my_library import Vector2D


class LinearTransform(ABC):
    """The matrix of our linear transform will consist on a list of rows with

    Args:
        ABC (_type_): _description_
    Attributes:
        matrix (list[list[float]]): the matrix of our linear transform.
        inv_matrix (list[list[float]]): the matrix of the inverse of our linear transform.
    """
    def __init__(self, matrix: list[list[float]]):
        self.matrix = matrix
        self.inv_matrix = self._inverse()  # we can call an undefined abstract method

    def __call__(self, vector: Vector2D) -> Vector2D:
        """Matrix times vector multiplication."""
        x = self.matrix[0, 0] * vector.x + self.matrix[0, 1] * vector.y
        y = self.matrix[1, 0] * vector.x + self.matrix[1, 1] * vector.y
        return Vector2D(x, y)

    @abstractmethod
    def _inverse(self) -> list[list[float]]:
        """The code for the abstract method will be specified inside each subclass.

        Because the method is not intended to be part of the user API, the convention is to
        begin the method's name with an underscore.

        Returns:
            list[list[float]]: _description_
        """
        ...

    def inverse_transform(self, vector: Vector2D) -> Vector2D:
        x = self.inv_matrix[0, 0] * vector.x + self.inv_matrix[0, 1] * vector.y
        y = self.inv_matrix[1, 0] * vector.x + self.inv_matrix[1, 1] * vector.y
        return Vector2D(x, y)


class Rotation(LinearTransform):

    def __init__(self, angle: float):
        self.angle = angle
        matrix = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]
        super().__init__(matrix)

    def _inverse(self):
        return [[cos(self.angle), sin(self.angle)], [-sin(self.angle), cos(self.angle)]]


class Shear(LinearTransform):
    """Shear transformation parallel to the x axis.

    Args:
        LinearTransform (_type_): _description_
    """

    def __init__(self, parameter: float):
        self.parameter = parameter
        matrix = [[1, parameter], [0, 1]]
        super().__init__(matrix)

    def _inverse(self):
        return [[1, -self.parameter], [0, 1]]
