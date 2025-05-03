from datetime import datetime        # Imports the datetime module
today = datetime.now()               # Calls the now function, which gets the current time/date from the system clock --> 
print(today)                         # Print statement to display time --> Nathan to move this line of code into module 6 once tested

# """
# Module: 1 - Create dictionary
# Developer: Jess
# Tester: Ben
# Status: Needs attention, see Ben's GH comments 30/04/2025
# """

# #INITIAL DICTIONARY v1 - JESS

# #This code creates the key:value pairings for the 'itemDict', which, when displayed to the user offers all items available to purchase
# itemDict = {
#   "001M": "Margarita Pizza",
#   "001P": "Pepperoni Pizza",
#   "002B": "Beef Burger",
#   "002C": "Chicken Burger",
#   "003": "Chips",
#   "004": "Add Bacon",
#   "005": "Add Cheese",
#   "006T": "Hot Drink - Tea",
#   "006C": "Hot Drink - Coffee",
#   "007C": "Cold Drink - Coke",
#   "007F": "Cold Drink - Fanta",
#   "0077": "Cold Drink - 7up",
#   "008": "Ice Cream",
#   "009": "Wind Break",
#   "010": "Sun Umbrella",
#   "011": "Mini BBQ",
#   "012": "Portable TV"
# }
# #This code uses the 'print' function to display the dictionary on screen
# print(itemDict)

# #This code creates the key:value pairings for the 'priceDict', which, when displayed to the user offers the cost of each item
# priceDict = {
#   "001M": 10.00,
#   "001P": 10.00,
#   "002B": 5.00,
#   "002C": 5.00,
#   "003": 5.00,
#   "004": 1.50,
#   "005": 0.75,
#   "006T": 1.50,
#   "006C": 1.50,
#   "007C": 2.25,
#   "007F": 2.25,
#   "0077": 2.25,
#   "008": 0.99,
#   "009": 34.99,
#   "010": 22.50,
#   "011": 7.00,
#   "012": 154.97
# }
# #This code uses the 'print' function to display the dictionary on screen
# print(priceDict)

# #AMENDED DICTIONARY v2 - JESS

# #This code creates the key:value pairings for the 'itemDict', which, when displayed to the user offers all items available to purchase
# shoppingDict = {
#   "001": ("Margarita Pizza", 10.00),
#   "002": ("Pepperoni Pizza", 10.00),
#   "003": ("Beef Burger", 5.00),
#   "004": ("Chicken Burger", 5.00),
#   "005": ("Chips", 5.00),
#   "006": ("Add Bacon", 1.50),
#   "007": ("Add Cheese", 0.75),
#   "008": ("Hot Drink - Tea", 1.50),
#   "009": ("Hot Drink - Coffee", 1.50),
#   "010": ("Cold Drink - Coke", 2.25),
#   "011": ("Cold Drink - Fanta", 2.25),
#   "012": ("Cold Drink - 7up", 2.25),
#   "013": ("Ice Cream", 0.99),
#   "014": ("Wind Break", 34.99),
#   "015": ("Sun Umbrella", 22.50),
#   "016": ("Mini BBQ", 7.00),
#   "017": ("Portable TV", 154.97)
# }
# #This code uses the 'print' function to display the dictionary on screen
# print(shoppingDict)

# #AMENDED DICTIONARY v3 - JESS

# #This code creates the key:value pairings for the 'shoppingDict', which, when displayed to the user offers all items available to purchase
# shoppingDict = {
#   "001": ("Margarita Pizza", 10.00),
#   "002": ("Pepperoni Pizza", 10.00),
#   "003": ("Beef Burger", 5.00),
#   "004": ("Chicken Burger", 5.00),
#   "005": ("Chips", 5.00),
#   "006": ("Add Bacon", 1.50),
#   "007": ("Add Cheese", 0.75),
#   "008": ("Hot Drink - Tea", 1.50),
#   "009": ("Hot Drink - Coffee", 1.50),
#   "010": ("Cold Drink - Coke", 2.25),
#   "011": ("Cold Drink - Fanta", 2.25),
#   "012": ("Cold Drink - 7up", 2.25),
#   "013": ("Ice Cream", 0.99),
#   "014": ("Wind Break", 34.99),
#   "015": ("Sun Umbrella", 22.50),
#   "016": ("Mini BBQ", 7.00),
#   "017": ("Portable TV", 154.97)
# }
# #This code uses a FOR LOOP alongside a 'print' function to display the dictionary on screen, line by line for ease of viewing
# for key, values in shoppingDict.items():
#   print(key)
#   print (values)

# USE THIS - AMENDED DICTIONARY v4 - JESS 

#This code creates the key:value pairings for the 'shoppingDict', which, when displayed to the user offers all items available to purchase
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

#This code uses a FOR LOOP alongside the 'print' function to display the dictionary on screen, line by line for ease of viewing. It also uses an F STRING which allows the code to become dynamic i.e. if the value changes, the code will change with it
for key, values in shoppingDict.items():
  print(key)
  print(f"{values[0]}: £{values[1]:.2f}")


# """
# Module: 2 - User inputs for item code and QTY
# Developer: Jess
# Tester: Ben
# Status: Needs attention, see Ben's GH comments

# #USER INPUTS v1 - JESS

# #This code asks the user to select which item they would like to purchase
# input("Type the item code of the item you'd like to purchase here: ")

# #This code asks the user to confirm how many of the chosen item they'd wish to purchase. The IF ELSE selection statement has been placed in here to ensure the user chooses at least one or more 
# quantity = input("How many would you like? Type here: ")
  
# if quantity >= "1":
#   print("Do you want to add another item?")
#   input("Y or N: ")
# else:
#   print("Enter a valid input of either 1 or more"), input(" ")
#   print("Do you want to add another item?"), input("Y or N: ")
  

# #A WHILE LOOP is required to continue this cycle of questioning until the user decides 'N' they don't wish to add any more items to their shopping cart


#AMENDED USER INPUTS v2 INC. WHILE LOOP AND NESTED IF ELSE SELECTION - JESS

#Declare the List 'shoppingCart[]' but leave it empty to be called upon later after the user has chosen their items
shoppingCart = []

#The below WHILE LOOP asks the user to input the item code which corresponds to the product they wish to purchase. Followed by the nested IF ELSE selection statement gives the user the option to break out of the loop and go to their cart if they wish. If they choose not to, they will be asked to confirm the quantity of their chosen product
while True:
  itemCode = input("Enter the item code of the product you'd like to purchase here (CHECKOUT to go to cart): ")
  if itemCode == "CHECKOUT" or itemCode == "checkout":
    break
  else:
      quantity = int(input("How many would you like? Type here: "))

#Items chosen by the user need to be saved into the list 'shoppingCart' in order to be produced in receipt format later on


"""

#This code asks the user to select which item they would like to purchase and confirm the quantity
input("Which item would you like to buy? Type the item code here: ")
input("How many would you like? Type here: ")
#validation?

"""
Module: 3 - Input validation to make sure the item code is input correctly and QTY is above 0
Developer: Adam
Tester: Nathan
Status: Not started
"""

# Module 3 code to go here
# Module 3 code to go here
# Module 3 code to go here

"""
Module: 4 - Give the option to add another item
Purpose: 
Developer: Ben
Tester: Jess
Status: Not started
"""

# Module 4 code to go here
# Module 4 code to go here
# Module 4 code to go here

"""
Module: 5 - Once user confirms transaction is complete, display all items
Purpose: 
Developer: Nathan
Tester: Adam
Status: Not started
"""

# Module 5 code to go here
# Module 5 code to go here
# Module 5 code to go here

"""
Module: 6 - Print receipt file
Purpose: 
Developer: Nathan
Tester: Adam
Status: In progress (under review by Adam)
"""

receipt= open("finalreceipt.txt ", "x")
#This will create a text files called receipt 
receipt=write( veriable_of_receipt )
#This will type up the completed order in the text file. 
print (veriable_of_receipt)
#This will display the contents of the variable to the user in the conosole 
receipt.close()
#This will close the text files. 

