#Creating a variable called available_items that has a list of items as values
available_items = ["apple", "banana", "orange", "grape"]

#Creating a variable called shopping_cart that has an empty list as a value
#That will store the items later
shopping_cart = []

#Using the input() method to prompt user to enter their value
#Creating 3 variables ( item1, item2, item3)  to store the inputs and convert them to lowercase using the lower() method
item1 = input("Enter the first item you want to buy: ").lower()
item2 = input("Enter the second item you want to buy: ").lower()
item3 = input("Enter the third item you want to buy: ").lower()

#we are using an if else statement to check if the items are available in the available_items list
#if it is available we will add it to the shopping_cart list using the append() method
#if the item is not available we will print a message saying that the item is not available 

if item1 in available_items:
    shopping_cart.append(item1)
    print(f"{item1} has been added to your shopping cart.")
else:
    print(f"Sorry, {item1} is not available in our store.")



if item2 in available_items:
    shopping_cart.append(item2)
    print(f"{item2} has been added to your shopping cart.")
else:
    print(f"Sorry, {item2} is not available in our store.")



if item3 in available_items:
    shopping_cart.append(item3)
    print(f"{item3} has been added to your shopping cart.")
else:
    print(f"Sorry, {item3} is not available in our store.")

#checking special items and add them to discount
if "banana" in shopping_cart:
    print("You have a special discount on bananas!")

#displaying the results:
print("\nYour shopping cart contains the following items:")
print(shopping_cart)

#Nothing wiil be printed out without any items
if not shopping_cart:
    print("Your shopping cart is empty. Please add some items to your cart.")