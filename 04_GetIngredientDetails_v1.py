# Functions go here
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
print("Please enter the ingredients in your recipe below.\n")

ingredient_name = not_blank("Ingredient Name: ", "Please enter the ingredient name")

quantity = num_check("Quantity (Number of units): ", "Please enter a valid number", float)

unit_price = num_check("Price per unit: ", "Please enter a valid number", float)

price = quantity * unit_price

print("\nThe cost of this ingredient is ${:.2f}.".format(price))