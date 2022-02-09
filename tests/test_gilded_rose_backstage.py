import unittest

from app.gilded_rose import GildedRose
from app.products import Product

product = Product()


class GildedRoseBackstageTest(unittest.TestCase):
    ''' Tests for Backstage Pass products '''

    def test_backstage_sell_in_12(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=12, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_sell_in_10(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_sell_in_8(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=8, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_sell_in_5(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_sell_in_3(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=3, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_sell_in_0(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_after_concert(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=-2, quality=15)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_at_sell_in_5(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=5, quality=55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_quality_at_sell_in_10(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=10, quality=55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_quality_at_sell_in_15(self):
        items = [product.create(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=15, quality=55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("BackStage Passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(50, items[0].quality)


if __name__ == '__main__':
    unittest.main()