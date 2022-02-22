#Rolling Dice Game
#Author: Aditya Bhansali Instagram: @adis_cosmos
import random
def isNumber(ran_no):
    if(ran_no < 7 and ran_no >= 1):
        return 1
    else:
        return 0
def RollDice():
    temp=int((random.random())*10)
    if(isNumber(temp)):
        print(temp,end=" ")
    else:
        RollDice()
no_of_dice=int(input("Select number of dices to roll."))
while (1):
    for i in range(no_of_dice):
        RollDice()
    print()
    print("Do you Want to roll again or exit?")
    inp_num=int(input("Press 0 to exit\nPress 1 to roll again"))
    if(inp_num == 0):
        print("Exited Successfully")
        break
    else:
        print("Again Rollong")
        
    
        
