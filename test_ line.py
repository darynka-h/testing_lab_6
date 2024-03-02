import unittest
from unittest import TestCase
from line import Point, Line


class test_square_preceding(TestCase):
    def setUp(self):
        self.point_1 = Point(0, 0)
        self.point_2 = Point(3, 3)
        self.line_1 = Line(self.point_1, self.point_2)
        self.line_5 = Line(self.point_1, self.point_2)
        self.point_11 = Point(-2, -6)
        self.point_22 = Point(1, -3)
        self.line_2 = Line(self.point_11, self.point_22)
        # ======= ПРАЦЮЄ ПЕРЕТИН ЦИХ ПРЯМИХ========
        self.line_3 = Line(Point(2, 2), Point(0, 0))
        self.line_7 = Line(Point(0, 2), Point(2, 2))
        # ===============
        self.line_4 = Line(Point(6, 1), Point(0, -5))
        self.line_6 = Line(Point(0, -5), Point(10, 5))


    def test_paralell_lines(self):
        self.assertEqual((self.line_1.initersect(self.line_2)), None, "Прямі паралельні!")
        self.assertEqual((self.line_3.initersect(self.line_4)), None, "Прямі паралельні!2")

    def test_same_lines(self):
        self.assertEqual((self.line_1.initersect(self.line_5)), self.line_1, "Прямі збігаються!")
        self.assertEqual((self.line_4.initersect(self.line_6)), self.line_4, "Прямі збігаються!")

    def test_intersection_point(self):
        print(self.line_3.initersect(self.line_7))
        self.assertTrue(self.line_3.initersect(self.line_7) != Point(0.0, 0.0), "Прямі мають точку перетину")
        # =======ЧОМУСЬ НЕ ПРАЦЮЄ ПЕРЕТИН ЦИХ ПРЯМИХ========
        self.assertEqual((self.line_3.initersect(self.line_7) == Point(2.0, 2.0)), True, "Прямі мають точку перетину")


if __name__ == '__main__':
    unittest.main(verbosity=2)
