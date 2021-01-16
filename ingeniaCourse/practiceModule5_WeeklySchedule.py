# Weekly Schedule
# Module 5 Practice
schedule = {
    "M": {
        6: "Mate", 8: "no-class", 10: "no-class", 12: "no-class", 14: "Technics", 16: "A-computer", 18: "no-class",
        20: "no-class", 22: "no-class"
    },
    "T": {
        6: "no-class", 8: "no-class", 10: "no-class", 12: "no-class", 14: "no-class", 16: "A-computer", 18: "no-class",
        20: "no-class", 22: "no-class"
    },
    "W": {
        6: "logic II", 8: "Technics", 10: "no-class", 12: "calculus", 14: "no-class", 16: "no-class", 18: "English V",
        20: "no-class", 22: "no-class"
    },
    "J": {
        6: "no-class", 8: "no-class", 10: "no-class", 12: "no-class", 14: "Technics", 16: "A-computer", 18: "no-class",
        20: "no-class", 22: "no-class"
    },
    "F": {
        6: "logic II", 8: "Technics", 10: "no-class", 12: "calculus", 14: "no-class", 16: "no-class", 18: "English V",
        20: "no-class", 22: "no-class"
    },
    "S": {
        6: "no-class", 8: "Labor-1", 10: "no-class", 12: "no-class", 14: "Labor-2", 16: "no-class", 18: "no-class",
        20: "no-class", 22: "no-class"
    }
}
print()
print("------------------------------Welcome to D School Weekly Schedule-------------------------------")
endWhile = True
while endWhile:
    print()
    print("-------------------------------------------Menu-------------------------------------------------")
    print("1 to Add Class     2 to Modify class     3 to Delete Class     4 to print Schedule     0 to Exit")
    option = input()
# Adding Classes Code
    if option == "1":
        print("Enter M for Monday  T for Tuesday  W for wednesday  J for Thursday  F for Friday  S for Saturday")
        option2 = input().upper()
        if option2 == "M":
            # Code for Monday
            print("Enter Hour: 6, 8, 10, 12, 14, 16, 18 or 20 according to your needs.")
            option3 = input()
            if option3 == "6":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["M"].get(6) == "no-class":
                    schedule["M"][6] = newClass
                    print("New Class Added: ", schedule["M"].get(6), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["M"].get(6))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["M"][6] = newClass
                            print("New Class Added: ", schedule["M"].get(6), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 6 am
            if option3 == "8":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["M"].get(8) == "no-class":
                    schedule["M"][8] = newClass
                    print("New Class Added: ", schedule["M"].get(8), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["M"].get(8))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["M"][8] = newClass
                            print("New Class Added: ", schedule["M"].get(8), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 8 am
            if option3 == "10":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["M"].get(10) == "no-class":
                    schedule["M"][10] = newClass
                    print("New Class Added: ", schedule["M"].get(10), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["M"].get(10))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["M"][10] = newClass
                            print("New Class Added: ", schedule["M"].get(10), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 10 am
            if option3 == "12":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["M"].get(12) == "no-class":
                    schedule["M"][12] = newClass
                    print("New Class Added: ", schedule["M"].get(12), " Hour: ", option3 + ":00 m")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["M"].get(12))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["M"][12] = newClass
                            print("New Class Added: ", schedule["M"].get(12), " Hour: ", option3 + ":00 m")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 12 m
            if option3 == "14":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["M"].get(14) == "no-class":
                    schedule["M"][14] = newClass
                    print("New Class Added: ", schedule["M"].get(14), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["M"].get(14))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["M"][14] = newClass
                            print("New Class Added: ", schedule["M"].get(14), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 14 pm
            if option3 == "16":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["M"].get(16) == "no-class":
                    schedule["M"][16] = newClass
                    print("New Class Added: ", schedule["M"].get(16), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["M"].get(16))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["M"][16] = newClass
                            print("New Class Added: ", schedule["M"].get(16), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 16 pm
            if option3 == "18":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["M"].get(18) == "no-class":
                    schedule["M"][18] = newClass
                    print("New Class Added: ", schedule["M"].get(18), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["M"].get(18))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["M"][18] = newClass
                            print("New Class Added: ", schedule["M"].get(18), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 18 pm
            if option3 == "20":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["M"].get(20) == "no-class":
                    schedule["M"][20] = newClass
                    print("New Class Added: ", schedule["M"].get(20), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["M"].get(20))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["M"][20] = newClass
                            print("New Class Added: ", schedule["M"].get(20), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            else:
                print("Enter a valid hour:")
                continue
            # End hour 20 pm
        if option2 == "T":
            # Code for Tuesday
            print("Enter Hour: 6, 8, 10, 12, 14, 16, 18 or 20 according to your needs.")
            option3 = input()
            if option3 == "6":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["T"].get(6) == "no-class":
                    schedule["T"][6] = newClass
                    print("New Class Added: ", schedule["T"].get(6), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["T"].get(6))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["T"][6] = newClass
                            print("New Class Added: ", schedule["T"].get(6), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 6 am
            if option3 == "8":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["T"].get(8) == "no-class":
                    schedule["T"][8] = newClass
                    print("New Class Added: ", schedule["T"].get(8), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["T"].get(8))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["T"][8] = newClass
                            print("New Class Added: ", schedule["T"].get(8), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 8 am
            if option3 == "10":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["T"].get(10) == "no-class":
                    schedule["T"][10] = newClass
                    print("New Class Added: ", schedule["T"].get(10), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["T"].get(10))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["T"][10] = newClass
                            print("New Class Added: ", schedule["T"].get(10), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 10 am
            if option3 == "12":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["T"].get(12) == "no-class":
                    schedule["T"][12] = newClass
                    print("New Class Added: ", schedule["T"].get(12), " Hour: ", option3 + ":00 m")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["T"].get(12))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["T"][12] = newClass
                            print("New Class Added: ", schedule["T"].get(12), " Hour: ", option3 + ":00 m")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 12 m
            if option3 == "14":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["T"].get(14) == "no-class":
                    schedule["T"][14] = newClass
                    print("New Class Added: ", schedule["T"].get(14), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["T"].get(14))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["T"][14] = newClass
                            print("New Class Added: ", schedule["T"].get(14), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 14 pm
            if option3 == "16":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["T"].get(16) == "no-class":
                    schedule["T"][16] = newClass
                    print("New Class Added: ", schedule["T"].get(16), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["T"].get(16))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["T"][16] = newClass
                            print("New Class Added: ", schedule["T"].get(16), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 16 pm
            if option3 == "18":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["T"].get(18) == "no-class":
                    schedule["T"][18] = newClass
                    print("New Class Added: ", schedule["T"].get(18), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["T"].get(18))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["T"][18] = newClass
                            print("New Class Added: ", schedule["T"].get(18), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 18 pm
            if option3 == "20":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["T"].get(20) == "no-class":
                    schedule["T"][20] = newClass
                    print("New Class Added: ", schedule["T"].get(20), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["T"].get(20))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["T"][20] = newClass
                            print("New Class Added: ", schedule["T"].get(20), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            else:
                print("Enter a valid hour:")
                continue
            # End hour 20 pm
        if option2 == "W":
            # Code for Wednesday
            print("Enter Hour: 6, 8, 10, 12, 14, 16, 18 or 20 according to your needs.")
            option3 = input()
            if option3 == "6":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["W"].get(6) == "no-class":
                    schedule["W"][6] = newClass
                    print("New Class Added: ", schedule["W"].get(6), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["W"].get(6))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["W"][6] = newClass
                            print("New Class Added: ", schedule["W"].get(6), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 6 am
            if option3 == "8":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["W"].get(8) == "no-class":
                    schedule["W"][8] = newClass
                    print("New Class Added: ", schedule["W"].get(8), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["W"].get(8))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["W"][8] = newClass
                            print("New Class Added: ", schedule["W"].get(8), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 8 am
            if option3 == "10":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["W"].get(10) == "no-class":
                    schedule["W"][10] = newClass
                    print("New Class Added: ", schedule["W"].get(10), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["W"].get(10))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["W"][10] = newClass
                            print("New Class Added: ", schedule["W"].get(10), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 10 am
            if option3 == "12":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["W"].get(12) == "no-class":
                    schedule["W"][12] = newClass
                    print("New Class Added: ", schedule["W"].get(12), " Hour: ", option3 + ":00 m")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["W"].get(12))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["W"][12] = newClass
                            print("New Class Added: ", schedule["W"].get(12), " Hour: ", option3 + ":00 m")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 12 m
            if option3 == "14":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["W"].get(14) == "no-class":
                    schedule["W"][14] = newClass
                    print("New Class Added: ", schedule["W"].get(14), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["W"].get(14))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["W"][14] = newClass
                            print("New Class Added: ", schedule["W"].get(14), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 14 pm
            if option3 == "16":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["W"].get(16) == "no-class":
                    schedule["W"][16] = newClass
                    print("New Class Added: ", schedule["W"].get(16), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["W"].get(16))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["W"][16] = newClass
                            print("New Class Added: ", schedule["W"].get(16), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 16 pm
            if option3 == "18":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["W"].get(18) == "no-class":
                    schedule["W"][18] = newClass
                    print("New Class Added: ", schedule["W"].get(18), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["W"].get(18))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["W"][18] = newClass
                            print("New Class Added: ", schedule["W"].get(18), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 18 pm
            if option3 == "20":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["W"].get(20) == "no-class":
                    schedule["W"][20] = newClass
                    print("New Class Added: ", schedule["W"].get(20), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["W"].get(20))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["W"][20] = newClass
                            print("New Class Added: ", schedule["W"].get(20), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            else:
                print("Enter a valid hour:")
                continue
            # End hour 20 pm
        if option2 == "J":
            # Code for Thursday
            print("Enter Hour: 6, 8, 10, 12, 14, 16, 18 or 20 according to your needs.")
            option3 = input()
            if option3 == "6":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["J"].get(6) == "no-class":
                    schedule["J"][6] = newClass
                    print("New Class Added: ", schedule["J"].get(6), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["J"].get(6))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["J"][6] = newClass
                            print("New Class Added: ", schedule["J"].get(6), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 6 am
            if option3 == "8":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["J"].get(8) == "no-class":
                    schedule["J"][8] = newClass
                    print("New Class Added: ", schedule["J"].get(8), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["J"].get(8))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["J"][8] = newClass
                            print("New Class Added: ", schedule["J"].get(8), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 8 am
            if option3 == "10":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["J"].get(10) == "no-class":
                    schedule["J"][10] = newClass
                    print("New Class Added: ", schedule["J"].get(10), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["J"].get(10))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["J"][10] = newClass
                            print("New Class Added: ", schedule["J"].get(10), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 10 am
            if option3 == "12":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["J"].get(12) == "no-class":
                    schedule["J"][12] = newClass
                    print("New Class Added: ", schedule["J"].get(12), " Hour: ", option3 + ":00 m")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["J"].get(12))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["J"][12] = newClass
                            print("New Class Added: ", schedule["J"].get(12), " Hour: ", option3 + ":00 m")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 12 m
            if option3 == "14":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["J"].get(14) == "no-class":
                    schedule["J"][14] = newClass
                    print("New Class Added: ", schedule["J"].get(14), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["J"].get(14))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["J"][14] = newClass
                            print("New Class Added: ", schedule["J"].get(14), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 14 pm
            if option3 == "16":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["J"].get(16) == "no-class":
                    schedule["J"][16] = newClass
                    print("New Class Added: ", schedule["J"].get(16), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["J"].get(16))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["J"][16] = newClass
                            print("New Class Added: ", schedule["J"].get(16), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 16 pm
            if option3 == "18":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["J"].get(18) == "no-class":
                    schedule["J"][18] = newClass
                    print("New Class Added: ", schedule["J"].get(18), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["J"].get(18))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["J"][18] = newClass
                            print("New Class Added: ", schedule["J"].get(18), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 18 pm
            if option3 == "20":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["J"].get(20) == "no-class":
                    schedule["J"][20] = newClass
                    print("New Class Added: ", schedule["J"].get(20), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["J"].get(20))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["J"][20] = newClass
                            print("New Class Added: ", schedule["J"].get(20), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            else:
                print("Enter a valid hour:")
                continue
            # End hour 20 pm
        if option2 == "F":
            # Code for Friday
            print("Enter Hour: 6, 8, 10, 12, 14, 16, 18 or 20 according to your needs.")
            option3 = input()
            if option3 == "6":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["F"].get(6) == "no-class":
                    schedule["F"][6] = newClass
                    print("New Class Added: ", schedule["F"].get(6), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["F"].get(6))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["F"][6] = newClass
                            print("New Class Added: ", schedule["F"].get(6), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 6 am
            if option3 == "8":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["F"].get(8) == "no-class":
                    schedule["F"][8] = newClass
                    print("New Class Added: ", schedule["F"].get(8), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["F"].get(8))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["F"][8] = newClass
                            print("New Class Added: ", schedule["F"].get(8), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 8 am
            if option3 == "10":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["F"].get(10) == "no-class":
                    schedule["F"][10] = newClass
                    print("New Class Added: ", schedule["F"].get(10), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["F"].get(10))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["F"][10] = newClass
                            print("New Class Added: ", schedule["F"].get(10), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 10 am
            if option3 == "12":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["F"].get(12) == "no-class":
                    schedule["F"][12] = newClass
                    print("New Class Added: ", schedule["F"].get(12), " Hour: ", option3 + ":00 m")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["F"].get(12))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["F"][12] = newClass
                            print("New Class Added: ", schedule["F"].get(12), " Hour: ", option3 + ":00 m")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 12 m
            if option3 == "14":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["F"].get(14) == "no-class":
                    schedule["F"][14] = newClass
                    print("New Class Added: ", schedule["F"].get(14), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["F"].get(14))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["F"][14] = newClass
                            print("New Class Added: ", schedule["F"].get(14), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 14 pm
            if option3 == "16":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["F"].get(16) == "no-class":
                    schedule["F"][16] = newClass
                    print("New Class Added: ", schedule["F"].get(16), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["F"].get(16))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["F"][16] = newClass
                            print("New Class Added: ", schedule["F"].get(16), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 16 pm
            if option3 == "18":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["F"].get(18) == "no-class":
                    schedule["F"][18] = newClass
                    print("New Class Added: ", schedule["F"].get(18), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["F"].get(18))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["F"][18] = newClass
                            print("New Class Added: ", schedule["F"].get(18), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 18 pm
            if option3 == "20":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["F"].get(20) == "no-class":
                    schedule["F"][20] = newClass
                    print("New Class Added: ", schedule["F"].get(20), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["F"].get(20))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["F"][20] = newClass
                            print("New Class Added: ", schedule["F"].get(20), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            else:
                print("Enter a valid hour:")
                continue
            # End hour 20 pm
        if option2 == "S":
            # Code for Saturday
            print("Enter Hour: 6, 8, 10, 12, 14, 16, 18 or 20 according to your needs.")
            option3 = input()
            if option3 == "6":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["S"].get(6) == "no-class":
                    schedule["S"][6] = newClass
                    print("New Class Added: ", schedule["S"].get(6), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["S"].get(6))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["S"][6] = newClass
                            print("New Class Added: ", schedule["S"].get(6), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 6 am
            if option3 == "8":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["S"].get(8) == "no-class":
                    schedule["S"][8] = newClass
                    print("New Class Added: ", schedule["S"].get(8), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["S"].get(8))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["S"][8] = newClass
                            print("New Class Added: ", schedule["S"].get(8), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 8 am
            if option3 == "10":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["S"].get(10) == "no-class":
                    schedule["S"][10] = newClass
                    print("New Class Added: ", schedule["S"].get(10), " Hour: ", option3 + ":00 am")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["S"].get(10))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["S"][10] = newClass
                            print("New Class Added: ", schedule["S"].get(10), " Hour: ", option3 + ":00 am")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 10 am
            if option3 == "12":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["S"].get(12) == "no-class":
                    schedule["S"][12] = newClass
                    print("New Class Added: ", schedule["S"].get(12), " Hour: ", option3 + ":00 m")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["S"].get(12))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["S"][12] = newClass
                            print("New Class Added: ", schedule["S"].get(12), " Hour: ", option3 + ":00 m")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 12 m
            if option3 == "14":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["S"].get(14) == "no-class":
                    schedule["S"][14] = newClass
                    print("New Class Added: ", schedule["S"].get(14), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["S"].get(14))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["S"][14] = newClass
                            print("New Class Added: ", schedule["S"].get(14), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 14 pm
            if option3 == "16":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["S"].get(16) == "no-class":
                    schedule["S"][16] = newClass
                    print("New Class Added: ", schedule["S"].get(16), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["S"].get(16))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["S"][16] = newClass
                            print("New Class Added: ", schedule["S"].get(16), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 16 pm
            if option3 == "18":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["S"].get(18) == "no-class":
                    schedule["S"][18] = newClass
                    print("New Class Added: ", schedule["S"].get(18), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["S"].get(18))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["S"][18] = newClass
                            print("New Class Added: ", schedule["S"].get(18), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            # End hour 18 pm
            if option3 == "20":
                print("Enter New Class Name: ")
                newClass = input()
                if schedule["S"].get(20) == "no-class":
                    schedule["S"][20] = newClass
                    print("New Class Added: ", schedule["S"].get(20), " Hour: ", option3 + ":00 pm")
                    continue
                else:
                    print("This hour already has a class scheduled: ", schedule["S"].get(20))
                    print("Do you want to overwrite it?. Y/N")
                    option4 = input().upper()
                    intCic = True
                    while intCic:
                        if option4 == "Y":
                            schedule["S"][20] = newClass
                            print("New Class Added: ", schedule["S"].get(20), " Hour: ", option3 + ":00 pm")
                            intCic = False
                            continue
                        elif option4 == "N":
                            print("Schedule Not Modified")
                            intCic = False
                            continue
                        else:
                            print("Incorrect Option, Type Y or N")
            else:
                print("Enter a valid hour:")
                continue
            # End hour 20 pm
# Modifying class Code
    elif option == "2":
        print("here goes modifying code")
# Delete Class Code
    elif option == "3":
        print("----------------------------------Deleting Menu---------------------------------------- ")
        print()
        print("Enter: 1 to delete a specific class     2 to clear schedule     any to go Main Menu")
        loopEnd = True
        while loopEnd:
            delOption = input()
            if delOption == "1":
                print("Enter day: M, T, W, J, F, S." )
                dayOption = input().upper()
                if dayOption == "M":
                    print("Enter Hour: 6, 8, 10, 12, 14, 16, 18, 20.")
                    hourOption = input()
                    if hourOption == "6":
                        delOption1 = input("Enter the Class you want to delete: ")
                        if delOption1 in schedule["M"][6]:
                            schedule["M"][6] = "no-class"
                        else:
                            print("The class do not exist.")
            elif delOption == "2":
                print("Deleting.....")
            else:
                loopEnd = False
# Printing Schedule Code
    elif option == "4":
        schMonday = []
        schTuesday = []
        schWednesday = []
        schThursday = []
        schFriday = []
        schSaturday = []
        for i in schedule["M"]:
            if schedule["M"][i] != "no-class":
                schMonday.append(schedule["M"][i])
                if i < 12:
                    schMonday.append(i)
                    schMonday.append(":00 am")
                elif i == 12:
                    schMonday.append(i)
                    schMonday.append(":00 m")
                else:
                    schMonday.append(i)
                    schMonday.append(":00 pm")
        for i in schedule["T"]:
            if schedule["T"][i] != "no-class":
                schTuesday.append(schedule["T"][i])
                if i < 12:
                    schTuesday.append(i)
                    schTuesday.append(":00 am")
                elif i == 12:
                    schTuesday.append(i)
                    schTuesday.append(":00 m")
                else:
                    schTuesday.append(i)
                    schTuesday.append(":00 pm")
        for i in schedule["W"]:
            if schedule["W"][i] != "no-class":
                schWednesday.append(schedule["W"][i])
                if i < 12:
                    schWednesday.append(i)
                    schWednesday.append(":00 am")
                elif i == 12:
                    schWednesday.append(i)
                    schWednesday.append(":00 m")
                else:
                    schWednesday.append(i)
                    schWednesday.append(":00 pm")
        for i in schedule["J"]:
            if schedule["J"][i] != "no-class":
                schThursday.append(schedule["J"][i])
                if i < 12:
                    schThursday.append(i)
                    schThursday.append(":00 am")
                elif i == 12:
                    schThursday.append(i)
                    schThursday.append(":00 m")
                else:
                    schThursday.append(i)
                    schThursday.append(":00 pm")
        for i in schedule["F"]:
            if schedule["F"][i] != "no-class":
                schFriday.append(schedule["F"][i])
                if i < 12:
                    schFriday.append(i)
                    schFriday.append(":00 am")
                elif i == 12:
                    schFriday.append(i)
                    schFriday.append(":00 m")
                else:
                    schFriday.append(i)
                    schFriday.append(":00 pm")
        for i in schedule["S"]:
            if schedule["S"][i] != "no-class":
                schSaturday.append(schedule["S"][i])
                if i < 12:
                    schSaturday.append(i)
                    schSaturday.append(":00 am")
                elif i == 12:
                    schSaturday.append(i)
                    schSaturday.append(":00 m")
                else:
                    schSaturday.append(i)
                    schSaturday.append(":00 pm")
        print("-------------------------------Actual Schedule----------------------------")
        print()
        print("Monday: ", schMonday)
        print("Tuesday: ", schTuesday)
        print("Wednesday: ", schWednesday)
        print("Thursday: ", schThursday)
        print("Friday: ", schFriday)
        print("Saturday: ", schSaturday)
# Exiting/Invalid Option code
    elif option == "0":
        endWhile = False
        print("Exit Successfully")
        continue
    else:
        print("Invalid Option")
        continue

# print(schedule["M"])
# print(schedule.get("M").get(6))
# schedule["M"] = {6: "mate"}
# print(schedule.get("M").get(6))
# print(schedule["M"])
# print(schedule["W"])
# print(schedule["W"].get(8))
# schedule["S"][22] = "matte321"
# print(schedule["S"])
