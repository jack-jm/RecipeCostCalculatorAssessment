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

# Functions go here
def not_blank(question, error):
  valid = False
  while not valid:
    response = input(question)

    if response == "":
      print("{}. \nPlease try again.\n".format(error))
      continue

    return response
    
# Main routine goes here

# Ask if user wants to see the instructions or not
show_instructions = yes_no("Hello, would you like to read the instrutions? (Yes/No): ")

if show_instructions == "yes":
  print("\n*Instructions to be added here*")

# Shows message about healthy eating after instructions so my program has positive social implications
print("\nRemember to make good choices about what you eat. A nutritious meal should include vegetables, protein and carbohydrates.\n")

# Ask for the name of the recipe
recipe_name = not_blank("What is the name of your recipe? ", "Sorry, the recipe name cannot be blank.")