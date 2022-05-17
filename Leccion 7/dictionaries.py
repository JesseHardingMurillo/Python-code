dictionaries = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(dictionaries)

# length
print(len(dictionaries))

# Access an item (key)
print(dictionaries['IDE'])

# Other form to access an element
print(dictionaries.get('OOP'))

# Modified elements

dictionaries['IDE'] = 'integrated development environment'
print(dictionaries)

# loop element
# . Items allows you to separate the values
for d, v in dictionaries.items():
    print(d, v)

# Only keys
for k in dictionaries.keys():
    print(k)

# Only values

for v in dictionaries.values():
    print(v)

# Compare if there is an element
print('IDE' in dictionaries)

# Add element
dictionaries['PK'] = 'Primary Key'
print(dictionaries)

# Remove element
dictionaries.pop('DBMS')
print(dictionaries)

# Clear the dictionary
dictionaries.clear()
print(dictionaries)

# Delete the dictionary
del dictionaries
