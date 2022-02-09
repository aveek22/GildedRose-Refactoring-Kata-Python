import unittest

from app.gilded_rose import GildedRose
from app.products import Product

product = Product()


class GildedRoseConjuredTest(unittest.TestCase):
    ''' Tests for Conjured products '''

    def test_conjured_before_sell_in(self):
        items = [product.create(name="Conjured Mana Cake", sell_in=2, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_conjured_on_sell_in(self):
        items = [product.create(name="Conjured Mana Cake", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_conjured_after_sell_in(self):
        items = [product.create(name="Conjured Mana Cake", sell_in=-5, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(-6, items[0].sell_in)
        self.assertEqual(16, items[0].quality)

    def test_conjured_min_quality(self):
        items = [product.create(name="Conjured Mana Cake", sell_in=5, quality=-10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured_max_quality(self):
        items = [product.create(name="Conjured Mana Cake", sell_in=10, quality=55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)


if __name__ == '__main__':
    unittest.main()