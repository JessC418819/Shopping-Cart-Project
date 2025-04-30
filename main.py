"""
Module: 1 - Create dictionary
Developer: Jess
Tester: Ben
Status: Needs attention, see Ben's GH comments 30/04/2025
"""

#This code creates the key:value pairings for the 'itemDict', which, when displayed to the user offers all items available to purchase
itemDict = {
  "001M": "Margarita Pizza",
  "001P": "Pepperoni Pizza",
  "002B": "Beef Burger",
  "002C": "Chicken Burger",
  "003": "Chips",
  "004": "Add Bacon",
  "005": "Add Cheese",
  "006T": "Hot Drink - Tea",
  "006C": "Hot Drink - Coffee",
  "007C": "Cold Drink - Coke",
  "007F": "Cold Drink - Fanta",
  "0077": "Cold Drink - 7up",
  "008": "Ice Cream",
  "009": "Wind Break",
  "010": "Sun Umbrella",
  "011": "Mini BBQ",
  "012": "Portable TV"
}
#This code uses the 'print' function to display the dictionary on screen
print(itemDict)

#This code creates the key:value pairings for the 'priceDict', which, when displayed to the user offers the cost of each item
priceDict = {
  "001M": 10.00,
  "001P": 10.00,
  "002B": 5.00,
  "002C": 5.00,
  "003": 5.00,
  "004": 1.50,
  "005": 0.75,
  "006T": 1.50,
  "006C": 1.50,
  "007C": 2.25,
  "007F": 2.25,
  "0077": 2.25,
  "008": 0.99,
  "009": 34.99,
  "010": 22.50,
  "011": 7.00,
  "012": 154.97
}
#This code uses the 'print' function to display the dictionary on screen
print(priceDict)

"""
Module: 2 - User inputs for item code and QTY
Developer: Jess
Tester: Ben
Status: Needs attention, see Ben's GH comments
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
Module: 6 - Once user confirms transaction is complete, display all items
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
