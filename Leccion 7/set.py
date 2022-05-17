# set
from typing import Set

planets: set[str] = {'Mars', 'Jupyter', 'Venus'}

print(planets)

# length
print(len(planets))

# Check is element is present
print('Mars' in planets)

# Add elements
planets.add('Earth')

print(planets)

# Not support element duplicate but it says if there is an error
planets.add('Earth')
# No happen nothing
print(planets)

# Delete elements but it does not say if there is an error
planets.remove('Earth')
print(planets)
planets.discard('Mars')
print(planets)

# Clena set
planets.clear()
print(planets)