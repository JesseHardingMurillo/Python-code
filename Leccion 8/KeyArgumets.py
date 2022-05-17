# Dictionary **
def list_terms(**term):
    for t, v in term.items():
        print(f'{t}:{v}')


list_terms(IDE='Integrated Development Environment', PK='Primary key')


def unfold_names(name):
    for n in name:
        print(n)


names = ['Juan', 'Karla', 'Guillermo']

unfold_names(names)
# The word or name will be iterated
unfold_names('Pepe')
# Iterate a tuple
unfold_names((10, 11))
# Iterate a list
unfold_names([10, 11])
