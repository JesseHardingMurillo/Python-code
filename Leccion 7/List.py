# The list is a data set
# The index of the list starts from 0

names = ['Juan', 'Karla', 'Ricardo', 'Maria']
# all the list
print(names)
# One element
print(names[0])
print(names[1])
# Call the element list by inverse form
print(names[-1])
print(names[-2])

# Range in the list
print(names[0:2])

# At start of the list
print(names[:3])

# from index to end
print(names[1:])

# change the value of an index
names[3] = 'Ivonne'
print(names)
# iterate the list
for n in names:
    print(n)
else:
    print("The aren't more elements")

# Asking the length of a ready
print(len(names))

# add new element
names.append('Lorenzo')
print(names)

# Insert an element in specific index
names.insert(1, 'Octavio')
print(names)

# Remove element
names.remove("Octavio")
print(names)

# Remove the last added element
names.pop()
print(names)

# Delete element in selection index
del names[0]
print(names)

# Clear the all of list
names.clear()
print(names)

# Delete list
del names
print(names)
