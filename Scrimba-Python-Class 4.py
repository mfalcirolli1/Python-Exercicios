# Functions


def greeting(nome='User', age='None', color='None'):
    print(f'Hello, {nome.capitalize()}! You are {age}.')
    print(f'We hear you like the color {color.lower()}')


name = input('Name: ')
idade = input('Age: ')
color = input('Color: ')

greeting(name, idade, color)


# Return

def value_added_tax(amount):
    tax = amount * 0.25
    total = amount * 1.25
    return f'Tax is equal to {tax} and total price is equal to {total}'


print(value_added_tax(100))
