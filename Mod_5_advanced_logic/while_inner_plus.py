# Write a python program that, given an input list of any level of complexity/nestedness, 
# will return the inner most list plus 1. 
# This is to be done with a while loop. Note: the input will contain only integers or lists. 
# As an example:

# input_list = [1,2,3,4,[5,6,7,[8,9]]]

# your_py_program.py input_list

# will produce:

# [9,10]

# That is [8, 9] (the inner most list) plus 1 -> [9, 10]

# for this problem, I did not create a way for the user to input the list. the input list is written into the code for this problem
# i feel like we haven't covered input well enough for me to know how to convert the input from a string back into lists and integers

input_list = [1,2,3,4,[5,6,7,[8,9]]]

# current is a container for the current item in the input list that I am assessing if it is a list or not
current = input_list

while True:
    # the first iteration is the items in input_list since that is what is stored in current
    # following iterations will be over nested lists, if any exist 
    for item in current:
        # checking if the next item in the list is a list
        if isinstance(item, list):
            # now, that nested list is the next thing we will asses for more nested lists
            current = item
            # break will take me back to the beginning of the FOR loop (still in while loop)
            break
    # if no items in the current list we are assessing are lists, we break out of the WHILE loop
    else:
        break
# testing that current is the innermost list
# print(current)

# final_list is the container for the list of items in the innermost list with 1 added to each item
# keeping it outside the for loop so each value is saved
final_list = []
for x in current:
    final_list.append(x + 1)

print(final_list)

