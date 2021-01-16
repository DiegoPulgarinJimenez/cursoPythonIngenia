# School Farm 2.0
# Module 4 Practice
print()
print("---------------------------------Welcome to School Farm 2.0------------------------------------")
print()
condition = True
onionsMaintenance = ["Monday", "Tuesday", "8 am"]
onionsIrrigate = ["Sunday", "Friday", "6 am"]
onionsFertilize = ["Thursday", "Friday", "5 am"]
cilantroMaintenance = ["Wednesday", "Saturday", "18 pm"]
cilantroIrrigate = ["Tuesday", "Saturday", "12 m"]
cilantroFertilize = ["Thursday", "Sunday", "3 pm"]
option1 = ""
option2 = ""
while condition:
    print("Enter 1 to access onion's cultivation menu    Enter 2 to access cilantro's cultivation menu",
          "     Enter 0 to Exit")
    option1 = input()
    if option1 == "1":
        print("----------Onion's Cultivating Menu----------")
        print()
        print("Enter an option according to your needs")
        print("Maintenance Schedule: 1 ", "Irrigate Schedule: 2 ", "Fertilize Schedule: 3 ", "Cultivation Stages: 4 ",
              "Exit: 0")
        option2 = input()
        if option2 == "1":
            print("----------Maintenance Schedule----------")
            print()
            print(onionsIrrigate)
            print("To Modify Enter 1     Enter 0 to go main menu     Enter any to Exit")
            op1 = input()
            if op1 == "1":
                onionsMaintenance[0] = input("Enter Day1: ")
                onionsMaintenance[1] = input("Enter Day2: ")
                onionsMaintenance[2] = input("Enter Hour: ")
                print("New Schedule: ", onionsMaintenance)
                print("Enter 0 to go main menu     Enter any to Exit")
                op2 = input()
                if op2 == "0":
                    continue
                else:
                    condition = False
                    continue
            elif op1 == "0":
                continue
            else:
                condition = False
                continue
        elif option2 == "2":
            print("---------------Irrigate Schedule---------------")
            print("")
            print(onionsIrrigate)
            print("To Modify Enter 1     Enter 0 to go main menu     Enter any to Exit")
            op1 = input()
            if op1 == "1":
                onionsIrrigate[0] = input("Enter Day1: ")
                onionsIrrigate[1] = input("Enter Day2: ")
                onionsIrrigate[2] = input("Enter Hour: ")
                print("New Schedule: ", onionsIrrigate)
                print("Enter 0 to go main menu     Enter any to Exit")
                op2 = input()
                if op2 == "0":
                    continue
                else:
                    condition = False
                    continue
            elif op1 == "0":
                continue
            else:
                condition = False
                continue
        elif option2 == "3":
            print("----------Fertilize Schedule-----------")
            print(" ")
            print(onionsFertilize)
            print("To Modify Enter 1     Enter 0 to go main menu     Enter any to Exit")
            op1 = input()
            if op1 == "1":
                onionsFertilize[0] = input("Enter Day1: ")
                onionsFertilize[1] = input("Enter Day2: ")
                onionsFertilize[2] = input("Enter Hour: ")
                print("New Schedule: ", onionsFertilize)
                print("Enter any to Exit     Enter 0 to go Main Menu")
                op2 = input()
                if op2 == "0":
                    continue
                else:
                    condition = False
                    continue
            elif op1 == "0":
                continue
            else:
                condition = False
                continue
        elif option2 == "4":
            print()
            print("----------Cultivation Stages----------")
            print()
            stage1 = ["Vegetative Stage: ", "0 to 90 days"]
            stage2 = ["Flowering Stage: ", "0 to 15 days after Vegetative Stage Ended"]
            stage3 = ["Production Stage: ", "0 to 30 days after Flowering Stage Ended"]
            stage4 = ["Traviesa Stage: ", "0 to 60 days after Production Stage Ended"]
            print()
            print(stage1)
            print(stage2)
            print(stage3)
            print(stage4)
            print()
            print("Harvest Duration: 200 days approx.")
            print()
            print("Enter any to Exit     Enter 0 to go Main Menu")
            op2 = input()
            if op2 == "0":
                continue
            else:
                condition = False
                continue
        elif option2 == "0":
            condition = False
            continue
        else:
            print("Invalid value, please try it again.")
            continue
    elif option1 == "2":
        print("----------Cilantro's Cultivation Menu----------")
        print()
        print("Enter an option according to your needs")
        print("Maintenance Schedule: 1 ", "Irrigate Schedule: 2 ", "Fertilize Schedule: 3 ", "Cultivation Stages: 4 ",
              "Exit: 0")
        option2 = input()
        if option2 == "1":
            print("-----------Maintenance Schedule----------")
            print("")
            print(cilantroMaintenance)
            print("To Modify Enter 1     Enter 0 to go main menu     Enter any to Exit")
            op1 = input()
            if op1 == "1":
                cilantroMaintenance[0] = input("Enter Day1: ")
                cilantroMaintenance[1] = input("Enter Day2: ")
                cilantroMaintenance[2] = input("Enter Hour: ")
                print("New Schedule: ", cilantroMaintenance)
                print("Enter any to Exit     Enter 0 to go Main Menu")
                op2 = input()
                if op2 == "0":
                    continue
                else:
                    condition = False
                    continue
            elif op1 == "0":
                continue
            else:
                condition = False
                continue
        elif option2 == "2":
            print("-----------Irrigate Schedule------------")
            print()
            print(cilantroIrrigate)
            print("To Modify Enter 1     Enter 0 to go main menu     Enter any to Exit")
            op1 = input()
            if op1 == "1":
                cilantroIrrigate[0] = input("Enter Day1: ")
                cilantroIrrigate[1] = input("Enter Day2: ")
                cilantroIrrigate[2] = input("Enter Hour: ")
                print("New Schedule: ", cilantroIrrigate)
                print("Enter any to Exit     Enter 0 to go Main Menu")
                op2 = input()
                if op2 == "0":
                    continue
                else:
                    condition = False
                    continue
            elif op1 == "0":
                continue
            else:
                condition = False
                continue
        elif option2 == "3":
            print("----------Fertilize Schedule----------")
            print("  ")
            print(cilantroFertilize)
            print("To Modify Enter 1     Enter 0 to go main menu     Enter any to Exit")
            op1 = input()
            if op1 == "1":
                cilantroFertilize[0] = input("Enter Day1: ")
                cilantroFertilize[1] = input("Enter Day2: ")
                cilantroFertilize[2] = input("Enter Hour: ")
                print("New Schedule: ", cilantroFertilize)
                print("Enter any to Exit     Enter 0 to go Main Menu")
                op2 = input()
                if op2 == "0":
                    continue
                else:
                    condition = False
                    continue
            elif op1 == "0":
                continue
            else:
                condition = False
                continue
        elif option2 == "4":
            print()
            print("----------Cultivation Stages----------")
            print()
            stage1 = ["Vegetative Stage ", "0 to 30 days"]
            stage2 = ["Flowering Stage ", "0 to 20 days after Vegetative Stage Ended"]
            stage3 = ["Production Stage ", "0 to 10 days after Flowering Stage Ended"]
            stage4 = ["Traviesa Stage ", "0 to 30 days after Production Stage Ended"]
            print()
            print(stage1)
            print(stage2)
            print(stage3)
            print(stage4)
            print()
            print("Harvest Duration: 90 days approx.")
            print()
            print("Enter 0 or any to Exit     Enter 1 to go Main Menu")
            if input() == "1":
                continue
            else:
                condition = False
                continue
        elif option2 == "0":
            condition = False
            continue
        else:
            print("Invalid value, please try it again.")
            continue
    elif option1 == "0":
        condition = False
        continue
    else:
        print("Invalid value, please try again.")
        continue
print()
print("Exit Successfully.")
