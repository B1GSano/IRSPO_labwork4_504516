import unittest

from geometric_lib.square import area


class SquareTestCase(unittest.TestCase):
	def test_zero_mul(self):
		res = area(0)
		self.assertEqual(res, 0)

	def test_square_mul(self):
		res = area(10)
		self.assertEqual(res, 100)