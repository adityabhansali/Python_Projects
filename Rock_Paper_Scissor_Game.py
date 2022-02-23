#Rock Paper Scissor Game
#By Aditya Bhansali Instagram Id @adis_cosmos
import random

cnt_usr,cnt_cmp=0,0
cmp=1

def totalscore():
    print("Total Score:\nYour Points: ",cnt_usr,"Computer Points: ",cnt_cmp)

print("Welcome To the Rock Paper Scissor Game\n")
while(1):
    print("Press 1 for the Rock")
    print("Press 2 for the paper")
    print("Press 3 for the scissor")
    usr=int(input("Enter your number"))
    cmp=random.randint(1,3)
    print(cmp)
    if((usr == 1 and cmp == 1)or(usr == 2 and cmp == 2)or(usr == 3 and cmp == 3)):
        print("draw")
    elif((usr == 1 and cmp == 3)or(usr == 2 and cmp == 1)or(usr == 3 and cmp == 2)):
        print("You Won")
        cnt_usr += 1
    elif((usr == 1 and cmp == 3)or(usr == 2 and cmp == 1)or(usr == 3 and cmp == 2)):
        print("Computer Won")
        cnt_cmp += 1
    else:
        print("You entered Incorrect value")
    check=int(input("Enter 0 to exit or any number button to restart"))
    if(check == 0):
        print("Exited Successfully")
        break
totalscore()
