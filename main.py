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
    
# Main routine goes here

# Ask if user wants to see the instructions or not
show_instructions = yes_no("Hello, would you like to read the instrutions? (Yes/No): ")

if show_instructions == "yes":
  print("\n*Instructions to be added here*")

# Shows message about healthy eating after instructions so my program has positive social implications
print("\nRemember to make good choices about what you eat. A nutritious meal should include vegetables, protein and carbohydrates.")

# Ask for the name of the recipe
recipe_name = not_blank("\nWhat is the name of your recipe?: ", "Sorry, the recipe name cannot be blank.")

# Ask how many people the recipe will serve
servings = num_check("\nHow many servings will your recipe make?: ", "Please enter a valid number of servings.\n", float)

print("\nPlease enter the ingredients in your recipe below. Type 'xxx' when you are finished.\n")

# Creating lists to hold data collected about ingredients
ingredient_list = []
quantity_list = []
price_list = []

# Ingredient name defined as blank in the beginning
ingredient_name = ""

# The next loop will only start if the last ingredient name was not 'xxx.' The first loop, ingredient name will be blank
while ingredient_name.lower() != "xxx":
  print()
  
  ingredient_name = not_blank("Ingredient Name: ", "Please enter a valid ingredient name.\n")
  # If ingredient name is 'xxx', loop will break
  if ingredient_name.lower() == "xxx":
    break

  quantity = num_check("\nQuantity (Number of Units): ", "Please enter a valid quantity.", float)

  unit_price = num_check("\nPrice per Unit: $", "Please enter a valid price.", float)

  # New data collected is added to the lists
  ingredient_list.append(ingredient_name)
  quantity_list.append(quantity)
  price_list.append(unit_price)