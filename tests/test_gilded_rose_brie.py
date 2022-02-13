import unittest

from app.gilded_rose import GildedRose
from app.products import Product

product = Product()


class GildedRoseBrieTest(unittest.TestCase):
    """ Tests for Aged Brie products """

    def test_brie_before_sell_in(self):
        items = [product.create(name="Aged Brie", sell_in=5, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(5, items[0].quality)

    def test_brie_on_sell_in(self):
        items = [product.create(name="Aged Brie", sell_in=0, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_brie_after_sell_in(self):
        items = [product.create(name="Aged Brie", sell_in=-5, quality=2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-6, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_brie_zero_quality(self):
        items = [product.create(name="Aged Brie", sell_in=5, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_max_quality(self):
        items = [product.create(name="Aged Brie", sell_in=5, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_brie_over_max_quality(self):
        items = [product.create(name="Aged Brie", sell_in=5, quality=55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_brie_negative_quality(self):
        items = [product.create(name="Aged Brie", sell_in=5, quality=-4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
