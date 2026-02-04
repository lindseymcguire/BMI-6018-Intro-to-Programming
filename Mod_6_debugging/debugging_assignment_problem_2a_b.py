print("Problem 2.a and 2.b")
def exception_add_function(arg1, arg2):
    # numeric section
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
    # i placed the try and except block entirely before the string section, to catch any input errors before anything starts
    try:
        # using index, value with enumerate() to keep track of the index and the value at the same time
        for index, value in enumerate(arg1):
           # using not to target things that are not strings
           if not isinstance(value, str):
               # inserting specific error message here tied to TypeError exception
               # using an f string to insert the specific index that the error is caught at
               raise TypeError(f"Your input argument 1 at index {index} is not of the expected type. Please change this and rerun")
        # same as above, but for argument 2
        for index, value in enumerate(arg2):
            if not isinstance(value, str):
               raise TypeError(f"Your input argument 2 at index {index} is not of the expected type. Please change this and rerun")
    except TypeError as e:
       print("Error:", e)
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
arg_str_2=['1','1', 1]
print(exception_add_function(arg_str_1, arg_str_2))