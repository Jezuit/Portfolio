def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error. You cannot divide by zero."
    return a / b


print("Choose operation:")
print("1. To add")
print("2. To subtract")
print("3. To multiply")
print("4. Tu divide")
print("-----------------")

while True:
    Choose = input("Decide what you want to do and enter the number from 1 to 4: ")

    if Choose in ('1', '2', '3', '4'):
        try:

            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Error. Please enter a number.")
            continue

        if Choose == '1':
            result = addition(number1, number2)
            print(f"{number1} + {number2} = {result}")

        elif Choose == '2':
            result = subtraction(number1, number2)
            print(f"{number1} - {number2} = {result}")

        elif Choose == '3':
            result = multiplication(number1, number2)
            print(f"{number1} * {number2} = {result}")

        elif Choose == '4':
            result = division(number1, number2)
            print(f"{number1} / {number2} = {result}")

        another_calculation = input("Do you want to continue? (yes/no): ")
        if another_calculation.lower() != 'yes':
            print("Thanks for using this calculator.")
            break
    else:
        print("Error. Please enter a number from 1 to 4.")
