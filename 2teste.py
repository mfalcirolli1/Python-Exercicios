#Basic Calculator
while True:
    print('Options')
    print('Enter "add" to add two numbers')
    print('Enter "mult" to multiply two numbers')
    print('Enter "sub" to subtract two numbers')
    print('Enter "div" to divide two numbers')
    num = input('Enter which operation you want to perform: ')
    if num == "quit":
        break
    elif num == "add":
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        result = float(n1 + n2)
        print('The result is {:.2f}'.format(result))

    elif num == "sub":
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        result = float(n1 - n2)
        print('The result is {:.2f}'.format(result))

    elif num == "mult":
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        result = float(n1 * n2)
        print('The result is {:.2f}'.format(result))

    elif num == "div":
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        result = float(n1 / n2)
        print('The result is {:.2f}'.format(result))

    else:
        print('Unknown number')
