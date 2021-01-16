# Using Regular Function (It creates a list with pair numbers)
def pares_function(range1):
    j = 0
    ini = 1
    list1 = []
    while j < range1:
        par = ini * 2
        list1.append(par)
        ini += 1
        j += 1
    return list1


print(pares_function(4))


# Function Using a Generator (it creates a generator with pair numbers)
def pares_generator(range1):
    k = 0
    ini = 1
    while k < range1:
        par = ini * 2
        yield par  # yield --> it creates an object where 1 by 1 are been stored elements
        ini += 1
        k += 1


impObject = pares_generator(4)  # Printing the generator
for i in impObject:
    print(i)

print(next(pares_generator(8)))  # "next" return the next number stored in the generator


# Using * with in the parameter camp allow you to introduce any amount of parameters
def function1(*parameter1):
    for element in parameter1:
        yield element


elementList = function1("34", 345, "name", 89)
print(next(elementList))
print(next(elementList))
print(next(elementList))


# Function that return internal elements from an iterable item
def function2(*parameter1):
    for element in parameter1:
        for internalElement in element:
            yield internalElement


elementList2 = function2("name", "moreName", "thirdName", "lastName")
print(next(elementList2))
print(next(elementList2))
print(next(elementList2))


# Same function as before but improved
def function3(*parameter1):
    for element in parameter1:
        # for internalElement in element:
        yield from element


elementList3 = function3("name", "moreName", "thirdName", "lastName")
print(next(elementList3))
print(next(elementList3))
print(next(elementList3))
