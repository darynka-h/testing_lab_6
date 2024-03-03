import unittest
from unittest import TestCase
# import all_prefixes
from all_prefixes import all_prefixes

class TestPrefixes(TestCase):
    def setUp(self):
        self.word_1 = "lead"
        self.word_2 = "авангрд"
        self.word_3 = "Абракадабра"
        self.word_4 = "Desk"
        self.word_5 = "desktop"
        self.word_6 = "саксофон"



    def test_with_one_start_letter(self):
        self.assertEqual((all_prefixes(self.word_1)), set(['lea', 'le', 'lead', 'l']), "Не всі слова у результаті")
        self.assertEqual((all_prefixes(self.word_5)), set(['de', 'des', 'd', 'deskto', 'desk', 'desktop', 'deskt']), "Не всі слова у результаті")

    def test_with_repeated_start_letter(self):
        # self.assertEqual((all_prefixes(self.word_1)), set(['lea', 'le', 'lead', 'l']), "Не всі слова у результаті")
        self.assertEqual((all_prefixes(self.word_2)), set(
            ['а', 'анг', 'ангрд', 'аван', 'авангр', 'ав', 'ава', 'аванг', 'авангрд', 'ангр', 'ан']
            ), "Не всі слова у результаті")
        self.assertEqual((all_prefixes(self.word_6)), set(
            ['с', 'са', 'саксо', 'саксофон', 'сак', 'софо', 'саксоф', 'софон', 'со', 'саксофо', 'соф', 'сакс']
            ), "Не всі слова у результаті")
        
    def test_with_uppercase_letter(self):
        # self.assertEqual((all_prefixes(self.word_1)), set(['lea', 'le', 'lead', 'l']), "Не всі слова у результаті")
        self.assertEqual((all_prefixes(self.word_4)), set(
            ['des', 'de', 'desk', 'd']), "Не всі слова у результаті")
        self.assertEqual((all_prefixes(self.word_3)), set(
            ['ад', 'абракадабра', 'акад', 'абракад', 'абрака', 'абрак',
                'ак', 'абр', 'адабра', 'акадабра', 'а', 'абракадаб', 'адаб', 
                'ака', 'абракада', 'ада', 'адабр', 'акадаб', 'аб', 'акадабр',
                'абра', 'акада', 'абракадабр']
            ), "Не всі слова у результаті")
        
    # def test_line_initializing(self):
    #     self.assertIsInstance(self.line_2.point_1, Point, "Пряма неправильно ініціалізована")
    #     self.assertEqual((self.line_1.point_1.x), 0, "Пряма неправильно ініціалізована!")
    #     self.assertEqual((self.line_1.point_1.y), 0, "Пряма неправильно ініціалізована!")
    #     self.assertEqual((self.line_2.point_1.x), -2, "Пряма неправильно ініціалізована")
    #     self.assertEqual((self.line_2.point_1.y), -6, "Пряма неправильно ініціалізована")
    #     # self.assertEqual((isinstance(self.line_2.point_1, Point)), True, "Пряма неправильно ініціалізована")
    #     # self.assertEqual((isinstance(self.line_2.point_2, Point)), True, "Пряма неправильно ініціалізована")
    #     self.assertEqual((isinstance(self.line_2, Line)), True, "Пряма неправильно ініціалізована")
        
    # def test_coeff(self):
    #     self.assertEqual((self.line_9.line_coeff()), [2.0, 1.0], "Неправильні коефіцієнти прямої!")
    #     self.assertEqual((self.line_8.line_coeff()), [0.12, 0.0], "Неправильні коефіцієнти прямої!")

    # def test_paralell_lines(self):
    #     self.assertEqual((self.line_1.initersect(self.line_2)), None, "Прямі паралельні!")
    #     self.assertEqual((self.line_3.initersect(self.line_4)), None, "Прямі паралельні!2")

    # def test_same_lines(self):
    #     self.assertEqual((self.line_1.initersect(self.line_5)), self.line_1, "Прямі збігаються!")
    #     self.assertEqual((self.line_4.initersect(self.line_6)), self.line_4, "Прямі збігаються!")

    # def test_intersection_point(self):
    #     self.assertEqual((self.line_3.initersect(self.line_7).x == 2.0), True, "Прямі мають точку перетину")
    #     self.assertEqual((self.line_3.initersect(self.line_7).y == 2.0), True, "Прямі мають точку перетину")
    #     self.assertEqual((self.line_8.initersect(self.line_9).x == -0.53), True, "Прямі мають точку перетину")
    #     self.assertEqual((self.line_8.initersect(self.line_9).y == -0.06), True, "Прямі мають точку перетину")
    
    # def test_invalid_input(self):
    #     self.assertEqual((self.line_3.initersect("3x+2")), None, "Неправильний тип аргументу")
    #     self.assertEqual((self.line_3.initersect(self.line_7).y == 2.0), True, "Прямі мають точку перетину")
    #     self.assertEqual((self.line_8.initersect(self.line_9).x == -0.53), True, "Прямі мають точку перетину")
    #     self.assertEqual((self.line_8.initersect(self.line_9).y == -0.06), True, "Прямі мають точку перетину")


if __name__ == '__main__':
    unittest.main(verbosity=2)
