class GildedRose(object):

    PASSES = "Backstage passes to a TAFKAL80ETC concert"
    BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros" 
    CONJURED = "Conjured Mana Cake"

    def __init__(self, items):
        self.items = items

    #Ensure quality is between 0 and 50
    def constrain_quality(self, quality: int):
        return max(0, min(quality, 50))

    def update_quality(self):
        for item in self.items:
            if item.name != self.SULFURAS:
                # in case of wrong input values
                item.quality = self.constrain_quality(item.quality)  
                item.sell_in -= 1
                
            # Update quality based on item type
            match item.name:
                case self.PASSES:   # the quality increases by 1, 2 or 3 based on the sell_in 
                    item.quality += (-item.quality) if item.sell_in < 0 else (3 if item.sell_in < 6 else (2 if item.sell_in < 11 else 1))         
                case self.BRIE:     # twice as fast after sell_in < 0
                    item.quality += 2 if item.sell_in < 0 else 1    
                case self.CONJURED: # twice as fast as normal item
                    item.quality -= 4 if item.sell_in < 0 else 2    
                case self.SULFURAS: # do nothing for Sulfuras
                    pass    
                case _:             # default normal item, twice as fast after sell_in < 0
                    item.quality -= 2 if item.sell_in < 0 else 1  

            if item.name != self.SULFURAS:
                item.quality = self.constrain_quality(item.quality)
            

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
