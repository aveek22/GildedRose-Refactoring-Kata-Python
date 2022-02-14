from app.item import Item
from app.product_list import ProductList


class Product:
    """ Checks the item that needs to be created. """
    
    @staticmethod
    def create(name, sell_in, quality):

        if name == ProductList.AGED_BRIE.value:
            return AgedBrie(name, sell_in, quality)

        elif name == ProductList.BACKSTAGE_PASS.value:
            return BackstagePass(name, sell_in, quality)

        elif name == ProductList.SULFURUS.value:
            return Sulfuras(name, sell_in, quality)

        elif name == ProductList.CONJURED.value:
            return Conjured(name, sell_in, quality)

        else:
            return Item(name, sell_in, quality)


class AgedBrie(Item):
    """
    "Aged Brie" actually increases in Quality the older it gets
    """
    def _update_quality(self, sell_in):
        if self.quality < 0:
            return Item.MIN_QUALITY

        return min(self.quality + 1, Item.MAX_QUALITY)


class BackstagePass(Item):
    """
    "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    Quality changes as follows:
        - 2 when sell_in value is 10 days or less
        - 3 when sell_in value is 5 days or less
        - 0 when sell_in value is 0
    """
    def _update_quality(self, sell_in):
        if sell_in > 10:
            return min(self.quality + 1, Item.MAX_QUALITY)
        elif sell_in > 5:
            return min(self.quality + 2, Item.MAX_QUALITY)
        elif sell_in >=0:
            return min(self.quality + 3, Item.MAX_QUALITY)
        else:
            return Item.MIN_QUALITY


class Sulfuras(Item):
    """
        - "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.
        - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality.
    """
    def _update_quality(self, sell_in):
        if self.quality < Item.LEG_MAX_QUALITY:
            return Item.LEG_MAX_QUALITY
        else:
            return Item.LEG_MAX_QUALITY

    def _update_sell_in(self):
        pass


class Conjured(Item):
    """
    "Conjured" items degrade in Quality twice as fast as normal items
    Quality decreases as follows:
        - 2 when sell_in date is more than equal 0
        - 4 when sell_in date is less than 0
    """
    def _update_quality(self, sell_in):
        if self.quality < 0:
            return Item.MIN_QUALITY
        elif self.quality > 50:
            return Item.MAX_QUALITY

        if sell_in >= 0:
            return max(self.quality - 2, Item.MIN_QUALITY)
        else:
            return max(self.quality - 4, Item.MIN_QUALITY)