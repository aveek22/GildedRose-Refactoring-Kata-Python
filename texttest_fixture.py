from __future__ import print_function
import sys

from app.gilded_rose import GildedRose
from app.products import Product

def main():

    product = Product()
    print(f'OMGHAI!')

    # Create the list of products to be added
    product_list = [
        product.create(name='Aged Brie', sell_in=2, quality=0),
        product.create(name='Elixir of the Mongoose', sell_in=5, quality=7),
        product.create(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80),
        product.create(name='Sulfuras, Hand of Ragnaros', sell_in=1, quality=80),
        product.create(name='BackStage Passes to a TAFKAL80ETC concert', sell_in=15, quality=20),
        product.create(name='BackStage Passes to a TAFKAL80ETC concert', sell_in=10, quality=49),
        product.create(name='BackStage Passes to a TAFKAL80ETC concert', sell_in=5, quality=49),
        product.create(name='Conjured Mana Cake', sell_in=3, quality=6),
    ]

    days = 5

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1

    for day in range(days):
        print(f'-------- day {day} --------')
        print(f'name, sellIn, quality')

        for item in product_list:
            print(item)
        print('')
        GildedRose(product_list).update_quality()


if __name__ == '__main__':
    main()