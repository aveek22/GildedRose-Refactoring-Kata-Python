
class GildedRoseApp():
    '''
        This app is used to update the item properties.
    '''

    def __init__(self, _items):
        '''
            Initiate the class with a list of items to be updated.
        '''
        self.items = _items

    def update_quality(self):
        '''
            Loops through each item to update the quality and sell_in value
        '''
        for item in self.items:
            item.update()