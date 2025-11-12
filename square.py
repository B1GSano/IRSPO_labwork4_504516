import unittest


def area(a):
	"""
	Принимает на вход a - размер стороны квадрата
	Возвращает a^2 - площадь этого квадрата
	"""
	return a * a


def perimeter(a):
	"""
	Принимает на вход a - размер стороны квадрата
	Возвращает 4*a - периметр этого квадрата
	"""
	return 4 * a

class SquareTestCase(unittest.TestCase):
	def test_zero_mul(self):
		res = area(0)
		self.assertEqual(res, 0)

	def test_square_mul(self):
		res = area(10)
		self.assertEqual(res, 100)


