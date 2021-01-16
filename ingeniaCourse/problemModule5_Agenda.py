# Agenda
# Problem Module 5
agenda1 = []
contactInfo = []
key1 = True
key2 = 0
print()
print("---------------Welcome to D Agenda---------------")
print()
while key1:
    print()
    print("Enter 1 to add a new contact    Enter 2 to delete a Contact     Enter 3 to print Agenda     "
          "Enter 0 to Exit")
    finish1 = input()
    if finish1 == "1":
        contactName = input("Enter Contact Name: ")
        contactNumber = input("Enter Contact Number: ")
        contactInfo = [contactName, contactNumber]
        agenda1 += contactInfo
        print()
        print(contactName, " Added Successfully")
        key2 += 1
        continue
    elif finish1 == "2":
        if len(agenda1) == 0:
            print("The Agenda is Empty")
        else:
            delete1 = input("Enter Contact Name to Delete: ")
            print()
            if delete1 in agenda1:
                indexName = agenda1.index(delete1)
                indexNumber = indexName
                del agenda1[indexName]
                del agenda1[indexNumber]
                print("Contact ", delete1, "Deleted Successfully.")
                continue
            else:
                print("The Contact Entered is not in the Agenda")
                continue
    elif finish1 == "3":
        if len(agenda1) == 0:
            print("The Agenda is Empty")
        else:
            print("Agenda -->", agenda1)
        continue
    elif finish1 == "0":
        key1 = False
        continue
    else:
        print("Wrong value!, try again.")
        continue
if key2 > 0:
    print("Agenda List: --> ", agenda1)
    print()
    print("Exit Successfully.")
else:
    print("No new contacts Added")
    print()
    print("Exit Successfully.")
