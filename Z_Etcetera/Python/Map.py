# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# output = [2, 4, 6, 8]