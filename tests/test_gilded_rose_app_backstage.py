import unittest

from app.gilded_rose_app import GildedRoseApp
from app.products import Product

product = Product()


class GildedRoseAppBrieTest(unittest.TestCase):
    ''' Tests for Backstage Pass products '''

    def test_regular_item_before_sell_in(self):
        items = [product.create(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRoseApp(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)


if __name__ == '__main__':
    unittest.main()