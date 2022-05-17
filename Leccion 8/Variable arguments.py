# You don't know how many arguments do you need.

def list_names(*names):
    for n in names:
        print(n)


list_names('Juan', 'Karla', 'María', 'Ernesto')
