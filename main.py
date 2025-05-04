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

    if itemCode == "CHECKOUT" or itemCode == "checkout": # Safely handles closure of the infinite loop
        break # Breaks the loop
     # Nathan to insert checkout print statement here (element 5)
  
    if itemCode not in shoppingDict: # Checks if the user's input (itemCode) is in the dictionary
        print("Invalid product code, please try again.")
        continue # Go back to the top of the loop

    quantity = int(input("How many would you like? Type here: "))
    # Ben to insert quantity handling here (element 4)

    selectedItem = shoppingDict[itemCode] # Gets item from dictionary (using the item code the user typed)
    shoppingCart.append((selectedItem[0], selectedItem[1], quantity))  # Populates the empty shopping cart list declared earlier
    print(f"{quantity} x {selectedItem[0]} added to shopping cart.") # Prints each item being added to the cart

# Receipt handling | Nathan/Adam: Nathan to complete when the above code is complete
today = datetime.now() # Datetime variable setup for use in the receipt below, use: print(today)

receipt= open("finalreceipt.txt ", "x")
#This will create a text files called receipt 
receipt=write( veriable_of_receipt )
#This will type up the completed order in the text file. 
print (veriable_of_receipt)
#This will display the contents of the variable to the user in the conosole 
receipt.close()
#This will close the text files. 

