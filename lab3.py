"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 3
-----------------------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Develop a user interface for the Inventory Management System. This interface will
               allow users to interact with the InventoryManager to add, update, remove, and view
               items in the inventory using a command-line interface.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import necessary classes (Item class from lab1, InventoryManager class from lab2)
from lab1 import Item
from lab2 import InventoryManager
# Step 2: Define an add_item function that prompts the user for item details and adds the item to the inventory

def add_item(inventory):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    inventory.add_item(name, price, quantity)
    print("Item added")

# Step 3: Define an update_item function that prompts the user for item details and updates the item in the inventory
    
def update_item(inventory):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    inventory.update_item(name, price, quantity)
    print("Item updated")

# Step 4: Define a remove_item function that prompts the user for an item name and removes the item from the inventory
    
def remove_item(inventory):
    name = input("Enter item name: ")
    inventory.remove_item(name)
    print("Item removed")

# Step 5: Define a display_inventory function that displays all items in the inventory
    
def display_inventory(inventory):
    inventory.display_inventory()

def main():
    # Step 6: Initialise an instance of InventoryManager
    inventory = InventoryManager()
    # Step 7: Use the actions dictionary to map user input to the corresponding functions
    actions = {
        "1": add_item,
        "2": update_item,
        "3": remove_item,
        "4": display_inventory
    }

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")

        # Step 8: Implement the logic to call the appropriate function based on user input
        # Exit the loop if the user chooses 5, otherwise display an error message for invalid choices
        if choice == "5":
            break
        elif choice in actions:
            actions[choice](inventory)
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()