# Write a python program that, given an input list, will filter the input above a user defined threshold. 
# This is to be done with a standard function.
# That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]

# the parameters are the list the user gives, and their threshold
def filter_list(input_list, max_value):
    # an empty list to store the values under the threshold
    filtered_list = []
    for i in input_list:
        # sorting through each item and grabbing the items less than or equal to the threshold
        if i <= max_value:
            filtered_list.append(i)
    # returns a list of integers less than or equal to the threshold
    return filtered_list

# setting the input to a variable, and using the input instructions to achieve integers and spaces only
user_input = input("Enter a list of whole numbers separated by spaces: ")
# the input is automatically a string, so I am using int() and split() to turn each item between the spaces to an integer
user_list = (int(x) for x in user_input.split())
# converting the threshold from a string to an integer
max_value = int(input("Enter a whole number: "))
# the arguments are the list that i converted to integers, and the users defined threshold
filtered_list = filter_list(user_list, max_value)
print(filtered_list)