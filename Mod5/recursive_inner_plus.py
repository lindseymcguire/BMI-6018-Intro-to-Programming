# Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
# This is to be done with recursion. Note: the input will contain only integers or lists. 

input_list = [1,2,3,4,[5,6,7,[8,9]]]

# the parameter is the input list
def innermost_list_plus_one(input_list):
    # this first if statement is the base case
    # this is checking if any item in the input list is a list
    # "if not", so that if there are no lists, the statement is True and proceeds
    if not any(isinstance(item, list) for item in input_list):
        # creating an empty list to add the ints from the innermost list to
        adding_one = []
        # adding 1 to each item in the innermost list
        for item in input_list:
            adding_one.append(item + 1)
        # this is what will be returned at the end of the function
        return adding_one
    # this is what will run when nested lists still exist
    for item in input_list:
        if isinstance(item, list):
            # this is calling the original function
            return innermost_list_plus_one(item)

print(innermost_list_plus_one(input_list))
    