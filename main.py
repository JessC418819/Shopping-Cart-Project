# Module import
from datetime import datetime   # Imports the datetime module (for use on the receipt)
today = datetime.now()          # This assigns datetime to a variable (for use on the receipt)

# Shopping menu
shoppingDict = {
   "001": ("Margherita Pizza", 10.00), # The dictionary uses the key as the product code, and the tuple values for the item & cost
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

# Display shop menu
print("Code   | Item                   | Cost (£)")        # Prints the shop menu header
print("-" * 42)                                            # Prints 38 - as a menu separator
for key, values in shoppingDict.items():                   # For loop to print through full dictionary, Key=Product Code, Value[0]=Item Name, [Value[1]=Price 
  print(f"{key:<6} | {values[0]:<22} | {values[1]:>6.2f}") # F string (easier variable management) 2f used for 2 decimal places, proper spacing handled with ><num
print()

shoppingCart = [] # Declare an empty list which will be called on later (to add the user's items)

# Main Shopping Loop
while True: # Opens an infinite loop (always True)
         
    # Item code
    itemCode = input('Enter the item code of the product you\'d like to purchase (type "CHECKOUT" to finish): ').strip() # Asks the user to input the item code or "checkout", uses strip to remove empty spaces from the user's input

    if itemCode.upper() == "CHECKOUT": # Forces the user input (itemCode) to upper case, then checks for the word "checkout"
        break                          # Breaks the loop and moves onto receipt logic

    if itemCode not in shoppingDict:                       # Checks if the user's input (itemCode) is in the dictionary
        print("Invalid product code, please try again.")   # Informs the user of invalid product code
        continue                                           # Go back to the top of the loop
    
    # Quantity
    quantity = input("Enter the quantity you would like: ").strip() # Asks the user to input a QTY and removes additional spacing

    if quantity.upper() == "CHECKOUT": # Forces the user input (quantity) to upper case, then checks for the word "checkout"
      break                            # Breaks the loop and moves onto receipt logic

    try:                               # The try block is used for error handling of quantity
        quantity = int(quantity)       # Converts the user's input to an integer
        if quantity < 1:               # Checks if the QTY is zero or minus
          print('Invalid quantity. Please enter at least 1 of the item you want or type "CHECKOUT" to finish.') # Warns the user of invalid quantity
          continue                     # Go back to the top of the loop

    except ValueError:                 # If the conversion to integer fails
        print('Invalid quantity. Please enter at least 1 of the item you want or type "CHECKOUT" to finish.') # Warns the user of invalid quantity
        continue                       # Go back to the top of the loop

    # Add item to cart
    selectedItem = shoppingDict[itemCode] # Gets item from dictionary (using the item code the user typed)
    shoppingCart.append((selectedItem[0], selectedItem[1], quantity))  # Populates the empty shopping cart list declared earlier
    print(f"{quantity} x {selectedItem[0]} @ £{selectedItem[1]:.2f} added to shopping cart.") # Prints each order line added to cart

# Receipt file logic
receipt = open("finalreceipt.txt", "wt")    # Creates and opens the text file
print("\nOrder details:\n")                 # Prints the receipt header in the console 
receipt.write("Receipt:\n\n")               # Prints a receipt header into the text file.

total = 0   # Sets total to zero to be updated in the for loop below

print("Item                     QTY    Cost (£)")              # Prints the receipt menu to console
print("-" * 40)                                                # Prints menu separator to console
receipt.write("Item                     QTY    Cost (£)\n")    # Prints the receipt menu to file

for item in shoppingCart:                                                   # For loop to go through each item in the shoppingCart
    orderLine = item[1] * item[2]                                           # Saves an order line total by working out price * qty
    total = total + orderLine                                               # Updates the total each loop with itself + price*qty total
    print(f"{item[0]:<25} {item[2]:<4} {orderLine:>6.2f}")                  # Prints each order line to terminal (with proper spacing from ><num)
    receipt.write(f"{item[0]:<25} {item[2]:<4} {orderLine:>6.2f}\n")        # Writes each order line to file with same alignment (with proper spacing from ><num)

print(f"\nTotal: {total:>30.2f}\n")                     # Write total amount to console (with proper spacing from ><num)
receipt.write(f"\nTotal: {total:>30.2f}\n\n")           # Write total amount to file (with proper spacing from ><num)

print(today.strftime("%d-%m-%Y %H:%M:%S"))              # Prints the time to the console, formatted in a user-friendly way
receipt.write(today.strftime("%d-%m-%Y %H:%M:%S"))      # Write the time to the file, formatted in a user-friendly way

receipt.close()                                         # Close the text file
