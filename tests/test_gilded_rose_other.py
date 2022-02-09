import unittest

from app.gilded_rose import GildedRose
from app.products import Product

product = Product()


class GildedRoseAppBrieTest(unittest.TestCase):
    ''' Tests for Other products '''

    def test_other_1(self):
        items = [product.create(name="+5 Dexterity Vest", sell_in=20, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_other_2(self):
        items = [product.create(name="Elixir of the Mongoose", sell_in=8, quality=16)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Elixir of the Mongoose", items[0].name)
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(15, items[0].quality)


if __name__ == '__main__':
    unittest.main()