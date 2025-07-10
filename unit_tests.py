from gilded_rose import *
from unittest import *

def test_gilded_rose():
    
    PASSES = "Backstage passes to a TAFKAL80ETC concert"
    BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros" 
    CONJURED = "Conjured Mana Cake"
    # Test case 1: Normal item
    items = [Item("Normal Item", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 19  # Quality decreases by 1
    assert items[0].sell_in == 9

    items = [Item(PASSES, 5, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 23  # Quality increases by 1
    assert items[0].sell_in == 4

    items = [Item(PASSES, 10, -1)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 2  # Quality increases by 1
    assert items[0].sell_in == 9

    items = [Item(PASSES, 5, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in ==  4
    assert items[0].quality == 23

    items = [Item(PASSES, 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 22

    # Test case 2: Aged Brie
    items = [Item(BRIE, 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 21  # Quality increases by 1
    assert items[0].sell_in == 9

    # Test case 3: Aged Brie after sell by date
    items = [Item(BRIE, 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 22  # Quality increases by 2 after sell by date
    assert items[0].sell_in == -1

    # Test case 4: Backstage passes with more than 10 days
    items = [Item(PASSES, 15, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 21  # Quality increases by 1
    assert items[0].sell_in == 14

    # Test case 5: Backstage passes with 10 days or less
    items = [Item(PASSES, 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 22  # Quality increases by 2
    assert items[0].sell_in == 9

    # Test case 6: Backstage passes with 5 days or less
    items = [Item(PASSES, 5, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 23  # Quality increases by 3
    assert items[0].sell_in == 4

    # Test case 7: Backstage passes after sell by date
    items = [Item(PASSES, 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0  # Quality drops to 0 after sell by date
    assert items[0].sell_in == -1

    items = [Item("Normal Item", 0, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 8

    # Test case 8: Sulfuras
    items = [Item(SULFURAS, 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80  # Quality remains the same
    assert items[0].sell_in == 0  # Sell-in remains the same

    # Test case 9: Conjured item
    items = [Item(CONJURED, 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 18  # Quality decreases by 2
    assert items[0].sell_in == 9

    # Test case 10: Conjured item after sell by date
    items = [Item(CONJURED, 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 16  # Quality decreases by 4 after sell by date
    assert items[0].sell_in == -1

    # Test case 11: Quality should not go below 0
    items = [Item("Normal Item", 5, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0  # Quality remains 0
    assert items[0].sell_in == 4

    # Test case 12: Quality should not exceed 50
    items = [Item(BRIE, 5, 49)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50  # Quality capped at


test_gilded_rose()
