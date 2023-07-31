# Functions go here
def yes_no(question):
  to_check = ["yes", "no"]
  
  valid = False
  while not valid:
    response = input(question).lower()
    
    for var_item in to_check:
      if response == var_item:
       valid = True
       return response
      elif response == var_item[0]:
       valid = True
       return var_item

    print("Please enter either yes or no.\n")

def not_blank(question, error):
  valid = False
  while not valid:
    response = input(question)

    if response == "":
      print("{} \nPlease try again.\n".format(error))
      continue

    return response

def num_check(question, error, num_type):
  valid = False
  while not valid:
    try:
      response = num_type(input(question))
      if response <= 0:
        print(error)
      else:
        return response
    
    except ValueError:
      print(error)

def get_expenses(question, expense_type):
  # Lists defined, will be appended
  expense_list = []
  quantity_list = []
  price_list = []

# Loop to get expense name, quantity and price
  expense_name = ""
  while expense_name.lower() != "xxx":

    expense_name = not_blank(question, "Please enter a valid name.\n")
    if expense_name.lower() == "xxx":
      break

    if expense_type.lower() == "ingredient":
      quantity = num_check("Quantity (Number of Units): ", "\nPlease enter a valid quantity\n", float)
    else:
      quantity = 1

    unit_price = num_check("Price per Unit: $", "\nPlease enter a valid price\n", float)
    
    # Data collected is added to the lists
    expense_list.append(expense_name)
    quantity_list.append(quantity)
    price_list.append(unit_price)
  # Lists are returned to the main routine
  return expense_list, quantity_list, price_list

# Main routine goes here

# Asks if user has fixed costs and will either ask for them or not
have_fixed = yes_no("Do you have any fixed costs (eg. electricity)? ")
if have_fixed == "yes":
  fixed_details = get_expenses("\nFixed Cost Name: ", "fixed")
  print(fixed_details)

else:
  print()