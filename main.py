# Modules and configuration variables
from datetime import datetime   # Imports the datetime module
today = datetime.now()          # Assigns datetime to a variable to be called on
shoppingCart = []               # Declare an empty list to be used in shopping logic (add the user's item choice to)

# Shopping menu
shoppingDict = {
   "001": ("Margherita Pizza", 10.00),   # The dictionary uses the key as the product code, and the tuple values for the item & cost
   "002": ("Pepperoni Pizza", 10.00),
   "003": ("Beef Burger", 5.00),
   "004": ("Chicken Burger", 5.00),
   "005": ("Chips", 5.00),
   "006": ("Add Bacon", 1.50),
   "007": ("Add Cheese", 0.75),
   "008": ("Hot Drink - Tea", 1.50),
   "009": ("Hot Drink - Coffee", 1.50),
   "010": ("Cold Drink - Coke", 2.25),
   "011": ("Cold Drink - Fanta", 2.25),
   "012": ("Cold Drink - 7up", 2.25),
   "013": ("Ice Cream", 0.99),
   "014": ("Wind Break", 34.99),
   "015": ("Sun Umbrella", 22.50),
   "016": ("Mini BBQ", 7.00),
   "017": ("Portable TV", 154.97)
}

# Defines a function to display the shopping menu
def shop_menu():
    print("Code   | Item                   | Cost (£)")          # Prints the shop menu header
    print("-" * 42)                                              # Prints menu separator to the console
    for key, values in shoppingDict.items():                     # For loop to print through full dictionary, Key=Product Code, Value[0]=Item Name, [Value[1]=Price 
        print(f"{key:<6} | {values[0]:<22} | {values[1]:>6.2f}") # F string (easier variable management) 2f used for 2 decimal places, proper spacing handled with ><num
    print()

# Defines a function to run the shopping loop
def shopping_loop(): 
    while True:      # Opens an infinite loop (always True)

        # Item code input logic
        itemCode = input('Enter the item code of the product you\'d like to purchase (type "CHECKOUT" to finish): ').strip()

        if itemCode.upper() == "CHECKOUT":
            break

        if itemCode not in shoppingDict:
            print("Invalid product code, please try again.")
            continue

        # Quantity input logic
        quantity = input("Enter the quantity you would like: ").strip()

        if quantity.upper() == "CHECKOUT":
            break

        try:
            quantity = int(quantity)
            if quantity < 1:
                print('Invalid quantity. Please enter at least 1 of the item you want or type "CHECKOUT" to finish.')
                continue
        except ValueError:
            print('Invalid quantity. Please enter at least 1 of the item you want or type "CHECKOUT" to finish.')
            continue

        # Add item to cart logic
        selectedItem = shoppingDict[itemCode]
        shoppingCart.append((selectedItem[0], selectedItem[1], quantity))
        print(f"{quantity} x {selectedItem[0]} @ £{selectedItem[1]:.2f} added to shopping cart.")

# Defines a function to handle the checkout logic
def checkout():
    receipt = open("finalreceipt.txt", "wt")    # Creates and opens the text file
    print("\nOrder details:\n")                 # Prints the receipt header in the console 
    receipt.write("Receipt:\n\n")               # Writes the receipt header into the text file. 

    total = 0   # Sets total to zero to be updated in the for loop below
   
    print("Item                     QTY    Cost (£)")              # Prints the receipt menu header to the console
    print("-" * 40)                                                # Prints menu separator to the console
    receipt.write("Item                     QTY    Cost (£)\n")    # Writes the receipt menu header to the text file

    for item in shoppingCart:                                                   # For loop to go through each item in the shoppingCart
        orderLine = item[1] * item[2]                                           # Saves an order line total by working out price * qty
        total = total + orderLine                                               # Updates the total each loop with itself + price*qty total
        print(f"{item[0]:<25} {item[2]:<4} {orderLine:>6.2f}")                  # Prints each order line to the terminal (with proper alignment using :><)
        receipt.write(f"{item[0]:<25} {item[2]:<4} {orderLine:>6.2f}\n")        # Writes each order line to the text file (with proper alignment using :><)

    print(f"\nTotal: {total:>30.2f}\n")                     # Prints the total amount to the console (with proper alignment using :><)
    receipt.write(f"\nTotal: {total:>30.2f}\n\n")           # Writes the total amount to the text file (with proper alignment using :><)

    print("Thanks for your custom!\n")                      # Prints a friendly message of appreciation to console
    receipt.write("Thanks for your custom!\n")              # Writes a friendly message of appreciation to the text file

    print(today.strftime("%d-%m-%Y %H:%M:%S"))              # Prints the time to the console, formatted in a user-friendly way
    receipt.write(today.strftime("%d-%m-%Y %H:%M:%S"))      # Writes the time to the text file, formatted in a user-friendly way

    receipt.close()

shop_menu()     # Calls function to display the shop menu
shopping_loop() # Calls function to run the shopping loop
checkout()      # Call function to run checkout process
