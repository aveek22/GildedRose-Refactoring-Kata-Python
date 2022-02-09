import unittest

from app.gilded_rose import GildedRose
from app.products import Product

product = Product()


class GildedRoseSulfurasTest(unittest.TestCase):
    ''' Tests for Sulfuras products '''

    def test_sulfuras_before_sell_in(self):
        items = [product.create(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_on_sell_in(self):
        items = [product.create(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_after_sell_in(self):
        items = [product.create(name="Sulfuras, Hand of Ragnaros", sell_in=-5, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(-5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_max_quality_85(self):
        items = [product.create(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=85)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_max_quality_65(self):
        items = [product.create(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=65)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


if __name__ == '__main__':
    unittest.main()