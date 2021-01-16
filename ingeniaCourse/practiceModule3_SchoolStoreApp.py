# School Store App
# Module 3 Practice
print("")
print("----------Welcome to Vodka Store Manage Application----------")
print("")
iniCapital = input("Introduce the value (Number) of the capital for this week: ")
n = input("Introduce how many different products are going to be registered in this batch: ")
purchasedProducts = int(n)
i = 0
batchExpenses = .0
productsValue = .0
inventory = []
inventoryAmount = []
inventoryProductValue = []
inventoryProdsValue = []
inventorySalesValue = []
# Entering data products process
while i < purchasedProducts:
    productName = input("Enter Product Name: ")
    productQuantity = input("Enter Units Purchased: ")
    productQ = int(productQuantity)
    productValue = input("Enter Value per unit: ")
    productV = float(productValue)
    # Registering Inventory
    inventory.append(productName)
    inventoryAmount.append(productQ)
    if productQ >= 1:
        inventoryProductValue.append(productV)
        productsValue = productQ * inventoryProductValue[i]
        print("Product Value: " + productValue + " --> Products Purchased: " + productQuantity)
        saleValue = float(input("Enter Sale Value Per Unit: "))
        inventoryProdsValue.append(productsValue)
        inventorySalesValue.append(saleValue)
    else:
        print("No Products Added")
    batchExpenses += productsValue
    i += 1
# Printing results and final balance
print("")
print("----------------------Expenses Summary----------------------")
print("")
print("Expenses of this batch: " + str(batchExpenses))
remainingCapital = float(iniCapital) - batchExpenses
if remainingCapital < 0:
    print("Remaining Capital: " + str(remainingCapital))
    print("Negative Balance, consider reevaluating your investment.")
else:
    print("Remaining Capital: " + str(remainingCapital))
print(inventory, " Products Name")
print(inventoryAmount, " Products Quantity")
print(inventoryProductValue, " Product Value per Unit")
print(inventorySalesValue, " Product Sale Value")
print(inventoryProdsValue, " Product Costs")
print("")
print("------------------------------------------------------------")
print("")
print("-------------Second Section (Sales Register)----------------")
print("")
k = 0
print("Enter Data of Products Sold")
print("")
totalValueSales = .0
sValue = .0
while k < int(n):
    prodName = input("Enter Product Name: ")
    if prodName in inventory:
        prodAmount = int(input("Enter Product Amount: "))
        location = inventory.index(prodName)
        totalProductAmount = inventoryAmount[location] - prodAmount
        sValue = inventorySalesValue[location]*prodAmount
        print("Value of Sold Products: " + str(sValue))
        if totalProductAmount == 0:
            print("All Units Sold")
            print("Remaining Units in Storage: " + str(totalProductAmount))
            print("Sales Exceeded the Investment")
        elif totalProductAmount > 0:
            print("Remaining Units in Storage: " + str(totalProductAmount))
            if sValue > inventoryProdsValue[location]:
                print("Sales Exceeded the Product Investment")
            elif sValue < inventoryProdsValue[location]:
                print("Sales do not Exceeded the Product Investment")
    else:
        print("Product Entered not Available ")
        k -= 1
    totalValueSales += sValue
    k += 1
print("Total Value Sales: " + str(totalValueSales))
totalEarns = .0
if totalValueSales > batchExpenses:
    print("Product Sales Exceeded the Total Investment")
    totalEarns = totalValueSales - batchExpenses
    print("Total Earns: " + str(totalEarns))
elif totalValueSales < batchExpenses:
    print("Product Sales do not Exceeded the Total Investment")
    totalEarns = totalValueSales - batchExpenses
    print("Total Earns: " + str(totalEarns), " Negative balance")
finalCapital = remainingCapital + totalValueSales
if finalCapital >= remainingCapital:
    print("Final Capital: " + str(finalCapital))
else:
    print("Final Capital: " + str(finalCapital), "Negative Capital")
print("---------------------------------------------------------------------------------------------------")
