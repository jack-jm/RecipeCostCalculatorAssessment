# Functions go here
def yes_no(question):
  to_check = ["yes", "no"]

  # Not valid until the user responds with either 'yes', 'no', or the first letters of them.
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
      print("{}".format(error))
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

    expense_name = not_blank(question, "Please enter a valid name.")
    if expense_name.lower() == "xxx":
      print()
      break

    if expense_type.lower() == "ingredient":
      quantity = num_check("Quantity (Number of Units): ", "Please enter a valid quantity\n", float)
    else:
      quantity = 1

    unit_price = num_check("Price per Unit: $", "Please enter a valid price\n", float)
    
    # Data collected is added to the lists
    expense_list.append(expense_name)
    quantity_list.append(quantity)
    price_list.append(unit_price)
  # Lists are returned to the main routine
  return expense_list, quantity_list, price_list

def get_totals(lists):
  # Lists of quantities and prices renamed to make it easier and neater
  final_quantities = lists[1]
  final_prices = lists[2]

  # Loop number and total cost defined as zero.
  loop_number = 0
  total_cost = 0

  # Loop will run while the loop number is less than the number of ingredients
  while loop_number < len(final_quantities):
    # The amount to be added to the total cost per expense is calculated.
    add_amount = final_quantities[loop_number] * final_prices[loop_number]
    total_cost += add_amount
    # 1 is added to the loop number after every loop
    loop_number += 1

  # Total cost is returned to the main routine
  return total_cost
    
# Main routine goes here

# Ask if user wants to see the instructions or not
show_instructions = yes_no("Hello and welcome to this program. Would you like to read the instrutions? (Yes/No): ")

if show_instructions == "yes":
  print("\n- INSTRUCTIONS -")
  print("You will be asked for your recipe's name and number of servings, then prompted to enter the ingredients in your recipe. Please enter the name, quantity and price per unit (price per quantity of one) of your first ingredient.")
  print("\nOnce that is done, you can continue with the rest of your ingredients, until you are finished. Type 'xxx' to finish. You will then be prompted to enter any fixed costs, which are just like ingredients, but with no variable quantity. The total cost and price per serving will then be displayed.")

# Shows message about healthy eating after instructions so my program has positive social implications
print("\nRemember to make good choices about what you eat. A nutritious meal should include vegetables, protein and carbohydrates.")

# Ask for the name of the recipe
recipe_name = not_blank("\nWhat is the name of your recipe?: ", "Sorry, the recipe name cannot be blank.")

# Ask how many people the recipe will serve
servings = num_check("\nHow many servings will your recipe make?: ", "Please enter a valid number of servings.", float)

print("\nPlease enter the ingredients in your recipe below. Type 'xxx' when you are finished.\n")

# Uses function to get ingredient details in lists
ingredient_details = get_expenses("\nIngredient Name: ", "ingredient")

# Asks if user has fixed costs and will either ask for them or not
have_fixed = yes_no("Do you have any fixed costs (eg. electricity)? ")
if have_fixed == "yes":
  fixed_details = get_expenses("\nFixed Cost Name: ", "fixed")

else:
  print()


print("\n-----------------------\n\n\nHere are the final costs of your recipe:")

ingredients_total = get_totals(ingredient_details)

if have_fixed == "yes":
 print("\nThe total cost of ingredients is ${:.2f}".format(ingredients_total))
 fixed_total = get_totals(fixed_details)
 print("\nThe total fixed costs are ${:.2f}".format(fixed_total))
 final_total = ingredients_total + fixed_total

else:
  final_total = ingredients_total

print("\nThe final total is ${:.2f}".format(final_total))
serving_price = final_total / servings
print("\nThe price per serving is ${:.2f}".format(serving_price))
print("\n- Thank you for using Recipe Cost Calculator! -")