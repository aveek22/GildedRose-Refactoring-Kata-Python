import unittest

from app.gilded_rose import GildedRose
from app.products import Product

product = Product()


class GildedRoseRegularTest(unittest.TestCase):
    ''' Test for Regular Items '''

    def test_regular_item_before_sell_in(self):
        items = [product.create(name="Regular Product", sell_in=5, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Regular Product", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(5, items[0].quality)

    def test_regular_item_on_sell_in(self):
        items = [product.create(name="Regular Product", sell_in=0, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Regular Product", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_regular_item_after_sell_in(self):
        items = [product.create(name="Regular Product", sell_in=-5, quality=9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Regular Product", items[0].name)
        self.assertEqual(-6, items[0].sell_in)
        self.assertEqual(7, items[0].quality)

    def test_regular_item_zero_quality(self):
        items = [product.create(name="Regular Product", sell_in=10, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Regular Product", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_regular_item_negative_quality(self):
        items = [product.create(name="Regular Product", sell_in=10, quality=-4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Regular Product", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()