import unittest
from unittest import TestCase
from line import Point, Line


class TestLine(TestCase):
    def setUp(self):
        self.point_1 = Point(0, 0)
        self.point_2 = Point(3, 3)
        self.line_1 = Line(self.point_1, self.point_2)
        self.line_5 = Line(self.point_1, self.point_2)
        self.point_11 = Point(-2, -6)
        self.point_22 = Point(1, -3)
        self.line_2 = Line(self.point_11, self.point_22)
        self.line_3 = Line(Point(2, 2), Point(0, 0))
        self.line_7 = Line(Point(0, 2), Point(2, 2))
        self.line_4 = Line(Point(6, 1), Point(0, -5))
        self.line_6 = Line(Point(0, -5), Point(10, 5))
        self.line_8 = Line(Point(0, 0), Point(8, 1))
        self.line_9 = Line(Point(0, 1), Point(1, 3))

    def test_point_initializing(self):
        self.assertEqual((self.point_1.x), 0, "Точка неправильно ініціалізована!")
        self.assertEqual((self.point_1.y), 0, "Точка неправильно ініціалізована!")
        self.assertEqual((self.point_2.x), 3, "Точка неправильно ініціалізована")
        self.assertEqual((self.point_2.y), 3, "Точка неправильно ініціалізована")

    def test_line_initializing(self):
        self.assertIsInstance(self.line_2.point_1, Point, "Пряма неправильно ініціалізована")
        self.assertEqual((self.line_1.point_1.x), 0, "Пряма неправильно ініціалізована!")
        self.assertEqual((self.line_1.point_1.y), 0, "Пряма неправильно ініціалізована!")
        self.assertEqual((self.line_2.point_1.x), -2, "Пряма неправильно ініціалізована")
        self.assertEqual((self.line_2.point_1.y), -6, "Пряма неправильно ініціалізована")
        # self.assertEqual((isinstance(self.line_2.point_1, Point)), True, "Пряма неправильно ініціалізована")
        # self.assertEqual((isinstance(self.line_2.point_2, Point)), True, "Пряма неправильно ініціалізована")
        self.assertEqual((isinstance(self.line_2, Line)), True, "Пряма неправильно ініціалізована")
        
    def test_coeff(self):
        self.assertEqual((self.line_9.line_coeff()), [2.0, 1.0], "Неправильні коефіцієнти прямої!")
        self.assertEqual((self.line_8.line_coeff()), [0.12, 0.0], "Неправильні коефіцієнти прямої!")

    def test_paralell_lines(self):
        self.assertEqual((self.line_1.initersect(self.line_2)), None, "Прямі паралельні!")
        self.assertEqual((self.line_3.initersect(self.line_4)), None, "Прямі паралельні!2")

    def test_same_lines(self):
        self.assertEqual((self.line_1.initersect(self.line_5)), self.line_1, "Прямі збігаються!")
        self.assertEqual((self.line_4.initersect(self.line_6)), self.line_4, "Прямі збігаються!")

    def test_intersection_point(self):
        self.assertEqual((self.line_3.initersect(self.line_7).x == 2.0), True, "Прямі мають точку перетину")
        self.assertEqual((self.line_3.initersect(self.line_7).y == 2.0), True, "Прямі мають точку перетину")
        self.assertEqual((self.line_8.initersect(self.line_9).x == -0.53), True, "Прямі мають точку перетину")
        self.assertEqual((self.line_8.initersect(self.line_9).y == -0.06), True, "Прямі мають точку перетину")
    
    def test_invalid_input(self):
        self.assertEqual((self.line_3.initersect("3x+2")), None, "Неправильний тип аргументу")
        self.assertEqual((self.line_3.initersect(self.line_7).y == 2.0), True, "Прямі мають точку перетину")
        self.assertEqual((self.line_8.initersect(self.line_9).x == -0.53), True, "Прямі мають точку перетину")
        self.assertEqual((self.line_8.initersect(self.line_9).y == -0.06), True, "Прямі мають точку перетину")


if __name__ == '__main__':
    unittest.main(verbosity=2)
