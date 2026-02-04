

import numpy as np
# print("Question 1: ",np.__version__)

# # 2. Create a 1D array of numbers from 0 to 9. Desired output:
# # #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# arr_1d = np.arange(0, 10)
# print("Question 2: ",arr_1d)

# # loadtxt converts the dataset to an array
# # delimiter is set to ',' because that is what separates each element
# # converted all types to str, since arrays generated from np.loadtxt can only handle one type
# dataset = np.loadtxt("iris.data.txt", delimiter=',', dtype=str)

# print("Question 3:", dataset)

# # now, after creating the array, I can change the data types to what I want
# # variable float_data is taking all rows (:) and up to the fifth column (:4) from the dataset and converting it to float type
# # str_data is taking all rows (:) and only the fifth column (4) and keeping it as the original str type
# float_data = dataset[:, :4].astype(float)
# str_data = dataset[:, 4]

# # new variable petal_width is looking at the float_data, all rows (:), and only the fourth column (3)
# petal_width = float_data[:, 3]
# # creating a boolean mask of where the value of the fourth column elements are greater than 1
# # print(petal_width > 1)
# first_value_over_one = np.where(petal_width > 1)[0][0]
# print("Question 4:", first_value_over_one)

# np.random.seed(100)
# a = np.random.uniform(1,50, 20)
# # first creating a boolean mask [a > 30]. where that is True, convert the value to 30
# # same thing for values less than 10
# a[a > 30] = 30
# a[a < 10] = 10
# print("Question 5: ", a)

a = np.array([1, 2, 3, 4, 5])

mask = a > 3

print(mask)