import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """
  # Added more unit tests below

  def test_ratio_normal(self):
    self.assertEqual(getRatio(10, 2), 5)
    self.assertEqual(getRatio(5, 5), 1)
    self.assertEqual(getRatio(9, 3), 3)

  def test_ratio_zero_denominator(self):
    self.assertIsNone(getRatio(10, 0))

  def test_ratio_negative_numbers(self):
    self.assertEqual(getRatio(-10, 2), -5)
    self.assertEqual(getRatio(10, -2), -5)
    self.assertEqual(getRatio(-10, -2), 5)

  def test_ratio_zero_numerator(self):
    self.assertEqual(getRatio(0, 5), 0)
    self.assertIsNone(getRatio(0, 0))


if __name__ == '__main__':
    unittest.main()
