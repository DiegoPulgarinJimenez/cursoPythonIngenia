# Practice module 5


def add_contact():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    phone_number = input("Enter Phone Number: ")
    mail = input("Enter E-Mail: ")
    global nameList
    global mailList
    global phoneNumberList
    global ageList
    nameList.append(name)
    ageList.append(age)
    phoneNumberList.append(phone_number)
    mailList.append(mail)
    print("Contact Added Successfully.")
    print()


def delete_contact():
    print("Enter Contact to delete: ")
    contact_delete = input()
    global nameList
    global mailList
    global phoneNumberList
    global ageList
    if contact_delete in nameList:
        location_name = nameList.index(contact_delete)
        # nameList.remove(contact_delete)
        print("Are you sure? Y/N")
        resolution = input().upper()
        if resolution == "Y":
            del nameList[location_name]
            del mailList[location_name]
            del phoneNumberList[location_name]
            del ageList[location_name]
            print("Contact Deleted Successfully.")
        else:
            return
    else:
        print("Contact Not Found.")
    print()


def mod_contact():
    print("Enter Contact to Modify: ")
    contact_modify = input()
    global nameList
    global mailList
    global phoneNumberList
    global ageList
    if contact_modify in nameList:
        print("Contact to Modify Info: ")
        search_contact(contact_modify)
        print("Are you sure? Y/N")
        resolution1 = input().upper()
        if resolution1 == "Y":
            print(" Modify name: 1", " Modify Age: 2", " Modify Phone Number: 3", " Modify E-mail: 4", " Cancel: 0")
            resolution2 = input()
            location_mod = nameList.index(contact_modify)
            if resolution2 == "1":
                new_name = input("Enter New Name: ")
                nameList[location_mod] = new_name
                print("Contact Modified Successfully")
                print("Contact New Info: ")
                search_contact(contact_modify)
            elif resolution2 == "2":
                new_age = input("Enter New Age: ")
                ageList[location_mod] = new_age
                print("Contact Modified Successfully")
                print("Contact New Info: ")
                search_contact(contact_modify)
            elif resolution2 == "3":
                new_phone_number = input("Enter New Phone Number: ")
                phoneNumberList[location_mod] = new_phone_number
                print("Contact Modified Successfully")
                print("Contact New Info: ")
                search_contact(contact_modify)
            elif resolution2 == "4":
                new_mail = input("Enter New E-Mail: ")
                mailList[location_mod] = new_mail
                print("Contact Modified Successfully")
                print("Contact New Info: ")
                search_contact(contact_modify)
            else:
                print("Modified Canceled")
                return
        else:
            print("Exiting to menu..")
            print()
            return
    else:
        print("Contact Not Found.")
    print()


def search_contact(par1="-9999"):
    global nameList
    global mailList
    global phoneNumberList
    global ageList
    if par1 == "-9999":
        print("Enter Contact Name: ")
        contact_search = input()
        if contact_search in nameList:
            location_search = nameList.index(contact_search)
            print("Name: " + nameList[location_search], "Age: " + ageList[location_search],
                  "Phone Number: " + phoneNumberList[location_search], "E-Mail: " + mailList[location_search])
            print()
        else:
            print("Contact Not Found.")
            print()
    else:
        location_search = nameList.index(par1)
        print("name: " + nameList[location_search], "Age: " + ageList[location_search],
              "Phone Number: " + phoneNumberList[location_search], "E-Mail: " + mailList[location_search])
    return


def exit_app():
    pass


def print_note_book():
    pass


nameList = []
mailList = []
phoneNumberList = []
ageList = []
loopEnd = True
print()
print("-------------------------------------Welcome to D Contacts Info Tool--------------------------------------")
print()
while loopEnd:
    print("---------------------------------------------Main Menu----------------------------------------------------")
    print("1 to add contact    2 to delete contact     3 to search contact     4 to modify contact      0/any to exit")
    print("----------------------------------------------------------------------------------------------------------")
    option = input()
    if option == "1":
        add_contact()
    elif option == "2":
        delete_contact()
    elif option == "3":
        search_contact()
    elif option == "4":
        mod_contact()
    else:
        print("Exit Successfully.")
        loopEnd = False
