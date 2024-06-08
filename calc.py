user_input = input("Enter number 1: ")

try:
    number = float(user_input)
    print(number + 1)
except ValueError:
    print('Ermm')
