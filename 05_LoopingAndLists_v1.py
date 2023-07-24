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
      print("{}. \nPlease try again.\n".format(error))
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

# Main routine goes here

ingredient_list = []
quantity_list = []
price_list = []

ingredient_name = ""

while ingredient_name != "xxx":
  print()
  
  ingredient_name = not_blank("Ingredient Name: ", "Please enter a valid ingredient name.\n")
  if ingredient_name.lower() == "xxx":
    break

  quantity = num_check("\nQuantity (Number of Units): ", "Please enter a valid quantity.", float)

  unit_price = num_check("\nPrice per Unit: $", "Please enter a valid price.", float)

  ingredient_list.append(ingredient_name)
  quantity_list.append(quantity)
  price_list.append(unit_price)