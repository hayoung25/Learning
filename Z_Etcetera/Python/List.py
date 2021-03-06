list = [0, 1, 2, 3, 4, 5]

# list[start:end] -> include "start", exclude "end"
print(list[0:5])

# list[start:]  -> include "start" until the end element
print(list[1:])

# list[:end] -> start from start and exclude end element
print(list[:4])

# list plus list
list_a = [1, 2, 3]
list_b = [3, 4, 5]
list_plus_list = list_a + list_b
print(list_plus_list) # returns [1, 2, 3, 3, 4, 5]