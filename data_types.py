# Task 2
my_list = [1, 2, 3, 4, 5]
print(my_list, type(my_list))
my_list[0] = 5
print(my_list, type(my_list))

# Task 3
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple, type(my_tuple))
# Tuple is immutable. The following line would raise TypeError:
# my_tuple[0] = 5

# Task 4
my_set = {1, 2, 3, 4, 5}
print(my_set, type(my_set))

# Task 5
new_set = set(my_list)
print(new_set, type(new_set))

# Task 6
my_dict = {"June": 30, "July": 31, "August": 31}
print(my_dict, type(my_dict))

# Task 7
my_range = range(1, 11)
print(my_range, type(my_range))
print(list(my_range))

# Task 8
a = 15
b = "25"
sum_result = a + int(b)
print(sum_result, type(sum_result))
password_letters = "mypassword"
password_digits = 1234
password = password_letters + str(password_digits)
print(password, type(password))