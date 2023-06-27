# Functions go here
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
servings = num_check("How many servings will your recipe make? ", "Please enter a valid number of servings.\n", float)