import unittest

from app.gilded_rose import GildedRose
from app.products import Product

product = Product()


class GildedRoseAppRegularTest(unittest.TestCase):
    ''' Test for Regular Products '''

    def test_regular_item_before_sell_in(self):
        items = [product.create(name="Regular Product", sell_in=10, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Regular Product", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(3, items[0].quality)


if __name__ == '__main__':
    unittest.main()