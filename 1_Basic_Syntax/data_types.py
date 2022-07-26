# Numbers

nums = 10
print(nums)

decimals = 10.5
print(decimals)

complex_no = 3 + 5.5j

print(complex_no, complex_no.real, complex_no.imag)
print(isinstance(nums, int))
print(isinstance(decimals, float))
print(isinstance(complex_no, complex))

# Lists

list_1 = [1, 2, 3, 4, 5]
list_2 = ['1', '2', '3', '4', '5']

print(type(list_1))
print(type(list_2))

for i in list_1:
    print(type(i))

for i in list_2:
    print(type(i))

# Tuple

my_tuple = (1,2,3,4,5)

print(isinstance(my_tuple,tuple))

# Strings

my_string = 'This'

print(type(my_string))
print(isinstance(my_string,str))

# Set

my_set = {1,2,3,4,5}

print(type(my_set))

# print(my_set[1])

# Dictionary

my_dict = {'name': 'Mayank',
           'age': 30,
           'location': 'Bengaluru'}

print(my_dict.keys())
print(my_dict.values())

for i in my_dict.items():
    print(i)
