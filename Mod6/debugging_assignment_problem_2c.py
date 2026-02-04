print("Problem 2.c")
# here is the function that will be called if an element of the string list is not a string
def correction_add_function(arg):
    str_list = []
    # taking each element in the argument, and appending it to a new list as a string
    for a in arg:
         str_list.append(str(a))
    return str_list

#numeric section
def correct_add_function(arg1,arg2):  
    if sum([type(i)==int for i in arg1])==len(arg1) and \
        sum([type(i)==int for i in arg2])==len(arg2):
            arg1_index=0
            while arg1_index < len(arg1):
                arg_2_sum = 0
                for arg2_elements in arg2:
                    arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
                arg1[arg1_index]=arg_2_sum  
                arg1_index+=1
            return arg1
    #string section
    # added the try and except prior to the string section to catch any non strings before any actual code runs
    try:
        # this is checking if any element in the first argument is not a string
        for a in arg1:
            # if it is not a string...
            if not isinstance(a, str):
                # i send it to the except
                raise TypeError
        # same as above, but for the second argument
        for a in arg2:
            if not isinstance(a, str):
                raise TypeError
    except TypeError:
         # if the except was raised, it sends each argument to my new function that will return a list of strings
         arg1 = correction_add_function(arg1)
         arg2 = correction_add_function(arg2)
    if sum([type(i)==str for i in arg1])==len(arg1) and \
        sum([type(i)==str for i in arg2])==len(arg2):
            arg1_index=0
            while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                    arg_2_sum += arg2_elements
                arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
                arg1_index+=1
            return arg1
arg1 = [1, 2, 3]
arg2 = [1, 1, 1]
arg_str_1=['1','2','3']
arg_str_2=['1','1',1]

print(correct_add_function(arg_str_1,arg_str_2))
print(correct_add_function(arg1, arg2))
