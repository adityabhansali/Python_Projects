#Number Guessing Game:
#Author: Aditya Bhansali Instagram Id: @adis_cosmos
import random
def isNumber(ran_no):
    if(ran_no <= 9 and ran_no >= 0):
        return 1
    else:
        return 0

while 1:
    inp_no = int(input("Enter Number of your Choice(between 0 to 9)?"))
    ran=(random.random())*10
    if(isNumber(inp_no)):
        if(inp_no == int(ran)):
            print("You guessed it correct.")
            break
        else:
            print("You didn't guessed it correct Try again","Number was %d"%(ran),sep="\n")
    else:
        print("Out of range:")
