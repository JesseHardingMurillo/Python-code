# Immutable
fruits = ('Orange', 'Banana', 'Guava')
print(fruits)
# Tuple length
print(len(fruits))

# access an item
print(fruits[0])

# reverse navigation
print(fruits[-3])

# access range of values
print(fruits[0:2])

# loop through the elements of a tuple
for f in fruits:
    print(f, end=' ')  # In one line
    print(f)

# Change the value in tuple
fruitslist = list(fruits)

fruitslist[0] = 'Pear'

fruits = tuple(fruitslist)

print(fruits)

# Delete the all of the tuple
del fruits