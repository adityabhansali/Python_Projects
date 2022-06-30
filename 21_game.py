#Player 21 Game
#it is fun for the people who want to play while coding
#whenever 21 comes on the player they gets eliminated can be between any positive number of players.




def start():
    player=[]
    players=int(input("Enter number of players you want to play?"))
    if(players >= 21 and players <= 1):
        print("Lets Start Game\nNumber of players is",players+1)
        for i in range(players+1):
            player.append()

    else:
        start()

game=True
while game:
    start=input("Do you want to play game?(Yes or No)")
    if start == 'Yes':
        start()
    elif start == 'No':
        print("Thanks for using this game.")
        game=False
        exit(0)
    else:
        print("Wrong Choice")
    
    
    
