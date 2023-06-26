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
# Ask for the name of the recipe
recipe_name = not_blank("What is the name of your recipe? ", "Sorry, the recipe name cannot be blank.")

print(recipe_name)