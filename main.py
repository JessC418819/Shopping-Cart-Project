from datetime import datetime # Imports the datetime module (for receipt)

# Tuple dictionary setup | Jess/Ben: Complete/tested
shoppingDict = {
  "001": ("Margarita Pizza", 10.00),
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

# Display the shop | Jess/Ben: Complete/tested
for key, values in shoppingDict.items():  # For loop to print through full dictionary line by line for ease of viewing
  print(key)                                 
  print(f"{values[0]}: £{values[1]:.2f}") # F string used to for easier variable inserts. :.2f used for 2 decimal places

# Setup shopping cart (list) | Jess/Ben: Complete/tested
shoppingCart = [] # Declare the List 'shoppingCart[]' but leave it empty to be called upon later after the user has chosen their items

# Main Shopping loop | Everyone: Ben to add quantity input validation (see placeholder) | Nathan to add print statement for cart (see placeholder)
while True: # Opens an infinite loop (it's always True)
    itemCode = input('Enter the item code of the product you\'d like to purchase here (type "CHECKOUT" to finish): ') # Asks the user to input the item code or "checkout"

    if itemCode.upper() == "CHECKOUT": # Safely handles closure of the infinite loop
        break # Breaks the loop
     # Nathan to insert checkout print statement here (element 5)
  
    if itemCode not in shoppingDict: # Checks if the user's input (itemCode) is in the dictionary
        print("Invalid product code, please try again.")
        continue # Go back to the top of the loop

    quantity = int(input("How many would you like? Type here: "))
    # Ben to insert quantity handling here (element 4)

     # (This was more complicated than you might expect because I had to look up how to deal with what happens if you entered a string as well as entered the wrong quantity - Ben)
     
     if quantity.upper() == "CHECKOUT":
        break

     try:
         quantity = int(quantity)
         while quantity < 1:
             print('Invalid quantity. Please enter at least 1 of the item you want or type "CHECKOUT" to finish.')
             continue

     except ValueError:
         print('Invalid quantity. Please enter at least 1 of the item you want or type "CHECKOUT" to finish.')
         continue 

#Is doing everything inside one while block really the best method? I can't suggest anything better but it creates indentation issues further down the line with the 'quantity' variable - Ben

    selectedItem = shoppingDict[itemCode] # Gets item from dictionary (using the item code the user typed)
    shoppingCart.append((selectedItem[0], selectedItem[1], quantity))  # Populates the empty shopping cart list declared earlier
    print(f"{quantity} x {selectedItem[0]} added to shopping cart.") # Prints each item being added to the cart

# Main Shopping loop | Complete nathan code and adam test 
receipt = open("finalreceipt.txt", "wt") # Creates and opens the text file
print("\nFinal Order Receipt:\n") # Prints the receipt header in the console 
receipt.write("Final Order Receipt:\n\n") # Prints a the recipet header in to the text file.
total = 0 # Sets total to zero to be updated in for loop below
for item in shoppingCart: # For loop to go through each item in the shoppingCart
    orderLine = item[1] * item[2] # Saves an order line total by working out price * qty
    total = total + orderLine # Updates the total each loop with itself + price*qty total
    print(f"{item[0]}(x{item[2]})                     £{orderLine:.2f}")            # Prints to terminal
    receipt.write(f"{item[0]} (x{item[2]})                     £{orderLine:.2f}\n") # Write to file

print(f"\nThe total amount is: £{total:.2f}\n") # Print total amount to console
receipt.write(f"\nThe total amount is: £{total:.2f}\n") # Write total amount to file

print(today.strftime("%d-%m-%Y %H:%M:%S")) # Print time to console
receipt.write(today.strftime("%d-%m-%Y %H:%M:%S")) # Write time to file
receipt.close() # Close the text file



