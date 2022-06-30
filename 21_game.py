#Player 21 Game
#it is fun for the people who want to play while coding
#whenever 21 comes on the player they gets eliminated can be between any positive number of players.




def starts():
    player=[]
    players=int(input("Enter number of players you want to play?"))
    if(players <= 21 and players >= 1):
        print("Lets Start Game\nNumber of players is",players)
        for i in range(players):
            name=input("Enter name of player" + str(i))
            player.append(name)

        print(player)
    else:
        starts()

game=True
while game:
    start=input("Do you want to play game?(Yes or No)")
    if start == 'Yes' or start == 'yes' or start == 'Y' or start == 'y':
        starts()
    elif start == 'No'or start == 'no' or start == 'N' or start == 'n':
        print("Thanks for using this game.")
        game=False
        exit(0)
    else:
        print("Wrong Choice")
    
    
    
