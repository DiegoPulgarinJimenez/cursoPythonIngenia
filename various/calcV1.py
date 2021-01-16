# Calculator v 1.0
def addition(n1, n2):
    res1 = n1 + n2
    return res


def subtraction(n1, n2):
    res2 = n1 - n2
    return res


def multiplication(n1, n2):
    res3 = n1 * n2
    return res


def division(numerator, denominator):
    try:
        res4 = numerator / denominator
        return res
    except ZeroDivisionError:
        print("Division over zero is not determined")
        print("Result: ", num1, "/", num2, " = ", "Undetermined")


print()
print("-----------------------------------Welcome to D Calc 1.0-----------------------------------")
print()
print("Type 1 for addition ", "Type 2 for subtraction ", "Type 3 for multiplication ", "Type 4 for division ")
option = input()
if option == "1":
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    res = addition(num1, num2)
    print("Result: ", num1, "+", num2, " = ", res)
elif option == "2":
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    res = subtraction(num1, num2)
    print("Result: ", num1, "-", num2, " = ", res)
elif option == "3":
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    res = multiplication(num1, num2)
    print("Result: ", num1, "*", num2, " = ", res)
elif option == "4":
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    res = division(num1, num2)
    print("Result: ", num1, "/", num2, " = ", res)
else:
    print("!Invalid Operation! ")
