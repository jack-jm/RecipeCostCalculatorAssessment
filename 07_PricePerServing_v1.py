# Functions go here

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
servings = 20

ingredient_details = ["flour", "milk", "sugar"], [2, 2, 0.5], [2, 2, 3]

fixed_details = ["electricity", "new equipment"], [1, 1], [3, 10]

# Totals for ingredients and fixed costs are calculated using function and then printed.
ingredients_total = get_totals(ingredient_details)
fixed_total = get_totals(fixed_details)
print("The total cost of ingredients is ${:.2f}".format(ingredients_total))
print("The total cost of fixed costs is ${:.2f}".format(fixed_total))

# Final total calculated by adding ingredients and fixed costs
final_total = ingredients_total + fixed_total

print("Your total cost is ${:.2f}".format(final_total))

# Serving price calculated and printed
serving_price = final_total / servings
print("Your recipe will cost ${:.2f} per serving.".format(serving_price))