"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py

from lab1 import Item

# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.

class InventoryManager:
    def __init__(self):
        self._items = []

    def add_item(self, name, price, quantity):
        item = Item(name, price, quantity)
        self._items.append(item)

    def update_item(self, name, price, quantity):
        item = self.get_item(name)
        if item:
            item.set_price(price)
            item.set_quantity(quantity)
        else:
            raise ValueError("Item not found")

    def remove_item(self, name):
        item = self.get_item(name)
        if item:
            self._items.remove(item)
        else:
            raise ValueError("Item not found")
            
    def display_inventory(self):
        for item in self._items:
            print(item.get_name(), item.get_price(), item.get_quantity())
                


# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

potions = InventoryManager()
enchantments = InventoryManager()
talismans = InventoryManager()

potions.add_item("Healing Potion.", 10, 10)
enchantments.add_item("Fire Resistance.", 100, 4)
talismans.add_item("Talisman of Fire Resistance.", 1000, 1)
potions.display_inventory()
enchantments.display_inventory()
talismans.display_inventory()

