# game 1 (guess the number)
# Problem Module 4
import random
print()
print("------------------------------Welcome to the game Guess the Number---------------------------------")
print()
print("Enter a number that represents how many attempts you want to have (bigger the number easy the game)")
try1 = int(input())
print("Enter a number for a range that you want: ")
range1 = int(input())
userNumber = int(input("Enter your guess: "))
randomNumber = random.randint(0, range1)
attempts = 0
try1 -= 1
if userNumber == randomNumber:
    attempts += 1
    print("Congrats! you got it at the first try!")
    print("Attempts: ", attempts)
    try1 -= 0
else:
    attempts += 1
    print("Wrong guess! ")
    while userNumber != randomNumber:
        attempts += 1
        try1 -= 1
        if try1 == 0:
            print("You lose!, your attempts are: 0")
            exit()
        userNumber = int(input("try it again: "))
        if userNumber == randomNumber:
            print()
            print("Congrats! you got it!")
            continue
        elif randomNumber > userNumber >= 0:
            print("Wrong guess! " + " !Hint! --> The number is bigger than yours.")
            continue
        elif userNumber > range1:
            print("Number range is from 0 to ", range1)
            continue
        elif userNumber > randomNumber:
            print("Wrong guess! " + " !Hint! --> The number is lower than yours.")
            continue
        elif userNumber < 0:
            print("Please enter a positive number.")
print("Remaining Attempts: ", try1)
print("It took you ", attempts, " attempts to guess it.")
print("Number: ", randomNumber)
