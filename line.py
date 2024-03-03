"""
implementation of work
"""
import numpy as np


class Point:
    """class Point"""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:
    """class Line"""
    def __init__(self, point_1: 'Point', point_2: 'Point') -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def line_coeff(self):
        unknown_matrix = np.array([[self.point_1.x, 1], [self.point_2.x, 1]])
        inv_matrix = np.linalg.inv(unknown_matrix)
        free_members = np.array([self.point_1.y, self.point_2.y])
        B = np.array(free_members)
        result = np.dot(inv_matrix, B).tolist()
        for i, el in enumerate(result):
            result[i] = round(el, 2)
        return result

    @staticmethod
    def lines_intersection(firt_line_coeff, second_line_coeff):
        """Function parametrs are coefficients of line
        Function returns tuple of x and y coordinates.
        """
        all_x = firt_line_coeff[0] - second_line_coeff[0]
        all_c = second_line_coeff[1] - firt_line_coeff[1]
        x_intersection = all_c/all_x
        y_intersection = firt_line_coeff[0] * x_intersection + firt_line_coeff[1]
        return Point(round(x_intersection, 2), round(y_intersection, 2))

    def initersect(self, line_2: 'Line'):
        """
        >>> line1 = Line(Point(2, 2), Point(3, 3))
        >>> line2 = Line(Point(-3, -3), Point(-4, -4))
        >>> line1.initersect(line1)

        >>> line_3 = Line(Point(2, 2), Point(0, 0))
        >>> line_7 = Line(Point(0, 2), Point(2, 2))
        >>> line1.initersect(line1)
        Point(2.0, 2.0)
        """
        if isinstance(line_2, Line):
            line_1_coeff = self.line_coeff()
            line_2_coeff = line_2.line_coeff()
            if line_1_coeff == line_2_coeff:
                return self
            if line_1_coeff[0] == line_2_coeff[0]:
                return None
            result = self.lines_intersection(line_1_coeff, line_2_coeff)
            return result


# line_3 = Line(Point(2, 2), Point(0, 0))
# line_7 = Line(Point(0, 2), Point(2, 2))
# result = line_3.initersect(line_7)
# print(result)


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
