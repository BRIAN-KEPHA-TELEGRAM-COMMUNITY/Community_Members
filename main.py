pickupCost = 0
deliveryCost = 5

running = True #Loop
import re

global pizzaMenu
global pizzaPrice
#LISTS
pizzaMenu = [ "Pepperoni", "Hawaiian", "Cheese", "Italian", "Margherita", "Apricot Chicken", "BBQ Meatlovers", "Chicken and Cranberry" ]
pizzaPrice = [ 9, 9, 9, 9, 9, 13, 13, 13 ]
cost = []
customerOrder = []


def pick_or_deli():
  global delivery
  delivery = raw_input("P - pick up / D - delivery:")
  delivery = delivery.upper() #Changes the letter inputted to an uppercase 

  if delivery == "D":
    while running == True:
      global customer_name #This can be called when printing out final order and details
      customer_name = raw_input("Name:")
      if not re.match("^[a-zA-Z ]*$", customer_name): #Checks whether input is letters only
        print("Please use letters only")
      elif len(customer_name) == 0: #User has not inputted anything, therefore invalid input
        print("Please enter a valid input")
      else:
        customer_name = customer_name.title()
        break #Breaks the loop when valid input has been entered
    while running == True:
      global customer_telephone
      customer_telephone = raw_input("Telephone:")
      if not re.match("^[0-9 ]*$", customer_telephone): #Checks whether input is numbers only
        print("Please use numbers only")
      elif len(customer_telephone) == 0: #User has not inputted anything, therefore invalid input
        print("Please enter a valid input")
      else:
        break #Breaks the loop when valid input has been entered
    while running == True:
      global house_no
      house_no = raw_input("House number:")
      if not re.match("^[0-9 /]*$", house_no): #Checks whether input is numbers only
        print("Please use numbers only")
      elif len(house_no) == 0: #User has not inputted anything, therefore invalid input
        print("Please enter a valid input")
      else:
        break #Breaks the loop when valid input has been entered
    while running == True:
      global street_name
      street_name = raw_input("Street name:")
      if not re.match("^[a-zA-Z ]*$", street_name): #Checks whether input is letters only
        print("Please use letters only")
      elif len(street_name) == 0: #User has not inputted anything, therefore invalid input
        print("Please enter a valid input")
      else:
        street_name = street_name.title()
        break #Breaks the loop when valid input has been entered
    while running == True:
      global suburb
      suburb = raw_input("Suburb:")
      if not re.match("^[a-zA-Z ]*$", suburb): #Checks whether input is letters only
        print("Please use letters only")
      elif len(suburb) == 0: #User has not inputted anything, therefore invalid input
        print("Please enter a valid input")
      else:
        suburb = suburb.title()
        break #Breaks the loop when valid input has been entered
    while running == True:
      global city
      city = raw_input("City:")
      if not re.match("^[a-zA-Z ]*$", city): #Checks whether input is letters only
        print("Please use letters only")
      elif len(city) == 0: #User has not inputted anything, therefore invalid input
        print("Please enter a valid input")
      else:
        city = city.title()
        break #Breaks the loop when valid input has been entered
    while running == True:
      global post_code
      post_code = raw_input("Postcode:")
      if not re.match("^[0-9 /]*$", post_code): #Checks whether input is numbers only
        print("Please use numbers only")
      elif len(post_code) == 0 or len(post_code) > 4: #No input, or excess digits
        print("Please enter a valid input")
      else:
        break #Breaks the loop when valid input has been entered
  elif delivery == "P":
    while running == True:
      global customer_name
      customer_name = raw_input("Name:")
      if not re.match("^[a-zA-Z ]*$", customer_name): #Checks whether input is letters only
        print("Please use letters only")
      elif len(customer_name) == 0: #User has not inputted anything, therefore invalid input
        print("Please enter a valid input")
      else:
        customer_name = customer_name.title()
        break #Breaks the loop when valid input has been entered
    while running == True:
      global customer_telephone
      customer_telephone = raw_input("Telephone:")
      if not re.match("^[0-9 ]*$", customer_telephone): #Checks whether input is numbers only
        print("Please use numbers only")
      elif len(customer_telephone) == 0: #User has not inputted anything, therefore invalid input
        print("Please enter a valid input")
      else:
        break #Breaks the loop when valid input has been entered  
  else:
    print("Please enter P or D")
    pick_or_deli()

pick_or_deli()

def print_menu():
  print ("""
  -----------------------------------------------
  |                 PIZZA MENU                  |
  |                                             |                       
  |              $9 classic pizzas              |
  |             -------------------             |
  |                1. Pepperoni                 |
  |                2. Hawaiian                  |
  |                3. Cheese                    |
  |                4. Italian                   |
  |                5. Margherita                |
  |                                             |
  |              $13 premium pizzas             |
  |             -------------------             |
  |              6. Apricot Chicken             |
  |              7. BBQ Meatlovers              |    
  |              8. Chicken & Cranberry         |
  |                                             |
  -----------------------------------------------
  """)
print_menu()
  
def order():
  global pizza_no
  while True:
    try: #Validating inputs
      pizza_no = int(raw_input("No. of pizzas (min 1 - max 5):"))
      if pizza_no < 1:
        print("Please order between 1 - 5 pizzas") #Checks whether input is between 1 and 5
        continue
      if pizza_no > 5:
        print("Please order between 1 - 5 pizzas")
        continue
      else:
        break #Breaks the loop when valid input has been entered
    except ValueError: #Validating inputs - accepts only numbers and can't be left blank 
      print("Please use numbers only")
      continue
order()

def Choice_of_pizza():
    for i in range(1,pizza_no+1): #Repeats a number of times (number user has inputted)
      while True:
        try: #Validating inputs
          pizza_kind = int(raw_input("Choice of pizza(s):"))
          if pizza_kind < 1:
            print("Refer to PIZZA MENU for pizza number")
            continue
          if pizza_kind > 8:
            print("Refer to PIZZA MENU for pizza number")
            continue
          else:
            pizza = pizza_kind - 1 #Makes the list start at 1
            cost.append(pizzaPrice[pizza])
            customerOrder.append(pizzaMenu[pizza])
            global total_cost
            total_cost = sum(cost) #Sum of the pizzas
            global grandTotal
            if delivery == "D": #Adds $5 dollars to the total cost if delivery
              grandTotal = total_cost + deliveryCost
            else: #Price stays the same if pick up 
              grandTotal = total_cost
            break
        except ValueError: #Validating inputs - accepts only numbers and can't be left blank 
          print("Please use numbers only")
          continue
Choice_of_pizza()

def customerDetails(): #Prints customer order and details
  if delivery == "D":
    print ("")
    print ("CUSTOMER and ORDER DETAILS")
    print ("")
    print ("Name:"), customer_name
    print ("Telephone:"), customer_telephone
    print ("Address:"), house_no, street_name
    print ("        "), suburb
    print ("        "), city
    print ("        "), post_code
    print ("ORDER:"), customerOrder
    print ("Total: $"), total_cost
    print ("Total + Delivery: $"), grandTotal
  else:
    print ("")
    print ("CUSTOMER and ORDER DETAILS")
    print ("")
    print ("Name:"), customer_name
    print ("Telephone:"), customer_telephone
    print ("ORDER:"), customerOrder
    print ("Total: $"), total_cost
customerDetails()

print ("")
def confirm(): #Confirms details of customer and order
  confirmation = raw_input("Y - confirm order / N - cancel order:")
  confirmation = confirmation.upper() #Changes the letter inputted to an uppercase 
  
  if confirmation == "Y": #if Y is entered, order is confirmed
    print("DETAILS CONFIRMED")
  elif confirmation == "N": #if N is entered, order is cancelled
    print("DETAILS CANCELLED - order has been reset")
    customerOrder[:] = []
    cost[:] = []
    print_menu()
    order()
    Choice_of_pizza()
    customerDetails()
    confirm()
  else:
    print("Please enter Y or N") #If anything other than Y or N is entered, it will ask again
    confirm()
    
confirm()

print ("")
def order_some_more(): #Placing another order
  order_more = raw_input("Z - order more / X - exit program:")
  order_more = order_more.upper() #Changes the letter inputted to an uppercase 
  '''cost[:] = []'''
  if order_more == "Z":
    print_menu() #Calls the functions - will run the code that the def defines
    order()
    Choice_of_pizza()
    customerDetails()
    confirm()
    print ("")
    print ("THANK YOU FOR YOUR ORDER")
    if delivery == "D":
      print ("Your order will be delivered in 25mins") #Ending statement 
    elif delivery == "P":
      print ("Your order will be ready to pick up in 20mins") #Ending statement 
  elif order_more == "X":
    print ("")
    print ("THANK YOU FOR YOUR ORDER")
    if delivery == "D":
      print ("Your order will be delivered in 25mins") #Ending statement 
    elif delivery == "P":
      print ("Your order will be ready to pick up in 20mins") #Ending statement 
  else:
    print ("Please enter X or Z") #If anything other than X or Z is entered, it will ask again
    order_some_more()
    
order_some_more()

#Made by Brian Ngugi
