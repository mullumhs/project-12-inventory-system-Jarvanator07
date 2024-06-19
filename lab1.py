"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 1
-----------------------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class named Item that represents a generic item in an inventory system.
               Implement encapsulation using private attributes and public getters and setters.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Define the Item class with initialisation that uses setters for name, price, and quantity.
# Instead of directly setting private attributes in the __init__ method, use the class's own setters
# We will define the setters in later steps to add validation to the setting of these attributes.
class Item:
    def __init__(self, name, price, quantity):
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)

    # Step 2: Implement a getter for the name attribute.
    # This method should simply return the value of the private _name attribute.

    def get_name(self):
        return self.__name

    # Step 3: Implement a setter for the name attribute.
    # This method should check if the provided value is a string before setting the _name attribute.
    # If the value is not a string, it should raise a ValueError.

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name must be a string")

    # Step 4: Implement a getter for the price attribute.
    # This method should return the price formatted as a string with two decimal places.
        
    def get_price(self):
        return "Price: ${:.2f}".format(self.__price)

    # Step 5: Implement a setter for the price attribute.
    # This method should check if the provided value is a non-negative number before setting the _price attribute.
    # If the value is negative, it should raise a ValueError.

    def set_price(self, price):
        if isinstance(price, int) and price >= 0:
            self.__price = price
        else:
            raise ValueError("Price must be a non-negative integer")

    # Step 6: Implement a getter for the quantity attribute.
    # This method should simply return the value of the private _quantity attribute.

    def get_quantity(self):
        return "quantity: {:.0f}".format(self.__quantity)

    # Step 7: Implement a setter for the quantity attribute.
    # This method should check if the provided value is a non-negative integer before setting the _quantity attribute.
    # If the value is negative, it should raise a ValueError.

    def set_quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity must be a non-negative integer")

# Step 8: Create instances of the Item class and demonstrate the use of getters and setters.
# For example, create a new Item and attempt to set its attributes with both valid and invalid values.
# Print the outputs using the getters to show how the data is managed internally.
        
if __name__ == '__main__':
    try:
        item1 = Item("banana", 10, 10)
        print("successfully created item", "name:", item1.get_name(), "price:", item1.get_price(), "quantity:", item1.get_quantity())
    except ValueError as e:
        print("Error creating item", e)

    try:
        item2 = Item("apple", -10, 10)
        print("successfully created item", "name:", item2.get_name(), "price:", item2.get_price(), "quantity:", item2.get_quantity())
    except ValueError as e:
        print("Error creating item", e)

    try:
        item3 = Item("92637819", 10, 10)
        print("successfully created item", "name:", item3.get_name(), "price:", item3.get_price(), "quantity:", item3.get_quantity())
    except ValueError as e:
        print("Error creating item", e)
