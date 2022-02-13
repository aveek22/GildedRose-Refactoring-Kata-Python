
class Item:
    """ Describes the specific item instance. """

    # The Quality of an item is never negative
    # The Quality of an item is never more than 50
    # "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.

    MIN_QUALITY = 0
    MAX_QUALITY = 50
    LEG_MAX_QUALITY = 80
    MIN_SELL_IN = 0

    def __init__(self, _name, _sell_in, _quality):
        """
            name :      name of the item
            sell_in:    number of days remaining to sell of the item
            quaality:   quality of the item
        """
        self.name = _name
        self.sell_in = _sell_in
        self.quality = _quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
        
    def update(self):
        """ Updates the sell in days and quality of the item """
        self._update_sell_in()
        self.quality = self._update_quality(self.sell_in)

    def _update_sell_in(self):
        """ Decreases the sell in days by 1 """
        self.sell_in -= 1

    def _update_quality(self, sell_in):
        """
        Updates the item quality
            - decrease by 1 if sell in more than or equal 0
            - decrease by 2 if sell in less than 0
            - quality can never be less than 0
        """
        if sell_in >= 0:
            return max(self.quality - 1, self.MIN_QUALITY)
        else:
            return max(self.quality - 2, self.MIN_QUALITY)