import unittest

from app.gilded_rose_app import GildedRoseApp
from app.products import Product

product = Product()


class GildedRoseAppTest(unittest.TestCase):
    ''' Tests for all products '''

    # Test for Regular Products
    def test_regular_item_before_sell_in(self):
        items = [product.create(name="foo", sell_in=10, quality=4)]
        gilded_rose = GildedRoseApp(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(3, items[0].quality)