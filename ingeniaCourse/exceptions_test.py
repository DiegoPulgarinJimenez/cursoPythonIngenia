quantityFries = 243
quantityCola = 122
inventory = {"fries": quantityFries, "cola": quantityCola}
n = 10
i = 0
sale = 3
print(inventory)
while i < n:
    quantityFries -= sale
    quantityCola -= sale
    i += 1
inventory = {}
print(inventory)


# Capturing several exceptions
def divide():
    try:
        n1 = float(input("Enter number 1: "))
        n2 = float(input("Enter number 2: "))
        res = n1/2
        print("Result: ", n1, "/", n2, "=", res)
    except ValueError:
        print("Value Error, Enter a Number")
    except ZeroDivisionError:
        print("Over Zero Division is Undetermined")
    finally:
        print("Operation Finalized")


print(divide())
