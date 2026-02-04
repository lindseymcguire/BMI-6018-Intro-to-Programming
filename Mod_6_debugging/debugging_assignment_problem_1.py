print("\nProblem 1.a")
def wrong_add_function(arg1,arg2):   
    arg1_index=0
    print("The error is in line 8 within the list comprehension")
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            # the list comprehension is adding each element of arg2 to the value at the given index of arg1 three times
            # first for loop iteration: [1 + 1] + [1 + 1] + [1 + 1] = 6
            # second for loop iteration: [2 + 1] + [2 + 1] + [2 + 1] = 9
            # third for loop iteration: [3 + 1] + [3 + 1] + [3 + 1] = 12
        print(f"The error in the loop is causing this output to be {arg_2_sum}")
        print(f"However, the correct output here should be {arg1[arg1_index] + arg2[arg1_index]}")
        arg1[arg1_index]=arg_2_sum 
        arg1_index+=1
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

print(wrong_add_function(arg1, arg2))
print("\nProblem 1.b")
def correct_add_function(arg1,arg2):   
    arg1_index=0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            # the change I made adds the value of arg1 and arg2 at the same index to each other
            arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
        arg1[arg1_index]=arg_2_sum  
        arg1_index+=1
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

print(correct_add_function(arg1, arg2))
