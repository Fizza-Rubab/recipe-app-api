from django.test import SimpleTestCase

from app import calc
class CalcTests(SimpleTestCase):
    '''Test the calc module'''
    def test_calc_add(self):
        res = calc.add(7,4)
        self.assertEqual(res,11)

    def test_calc_subtract(self):
        res = calc.subtract(4,3)
        self.assertEqual(res, 1)