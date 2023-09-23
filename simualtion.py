#THIS PROJECT WAS MADE TO SIMULATE A GAME OF MONOPOLY, WITH ABILITY TO SIMULATE FRoM ANY GAME POSITION
#!PRICES ARE IN MILIONS
import random
from time import sleep as wait
players=[

]
players_dict={

}
wins_loses={

}
draws=0
class Player:
    def  __init__(self, money,name):
        self.money=money
        self.name=name
        self.owned_buildings=[]
        self.houses=0
        self.hotels=0
        self.jailcards=0
        self.current_position=0
        players.append(self)
        players_dict[self.name]=self
        self.wins=0
        self.loses=0

class Building:
    def __init__(self,number,price,name,color):
        self.number=number
        self.price=price
        self.name=name
        self.hotels=0
        self.houses=0
        self.color = color

class Game:
    def __init__(self, numberOfPlayers,board):
        self.numberOfPlayers= numberOfPlayers
        self.board=board
board=[
    Building(0,0,'Start','special'),
    Building(1,0.6,'Klementska ulice','brown'),
    Building(2,0,'Pokladna','special'),
    Building(3,0.6,'Revolucni ulice','brown'),
    Building(4,0,'Dan z prijmu', 'special'),
    Building(5,2,'Wilsonovo nadrazi', 'train'),
    Building(6,1,'Panska ulice', 'light_blue'),
    Building(7,0,'Sance','special' ),
    Building(8,1,'Jindriska ulice','light_blue'),
    Building(9,1.2,'Vinohradska ulice','light_blue'),
    Building(10,0,'Vezeni', "special"),
    Building(11,1.4,'Prvni ruzova', "pink"),
    Building(12,2,'Elektrarna', "energy"),
    Building(13,1.4,'Druha ruzova', "pink"),
    Building(14,1.6,'Treti ruzova', "pink"),
    Building(15,2,'Holesovice nadrazi', "train"),
    Building(16,1.8,'Prvni oranzova', "orange"),
    Building(17,0,'Sance', "special"),
    Building(18,1.8,'Druha oranzova', "orange"),
    Building(19,2,'Treti oranzova', "orange"),
    Building(20,0,'Parkovani', "special"),
    

]
def diceRoll(number_of_dices):
    total=0
    dice_rolls=[]
    previous_roll=0
    for i in range(number_of_dices):
        roll=random.randint(1,6)
        if previous_roll!=0:
            if previous_roll==roll:
                print("rolling again")
                roll=random.randint(1,6)
            total+=roll
            dice_rolls.append(roll)
        else:
            previous_roll=roll
            total+=roll
            dice_rolls.append(roll)
    #?print(f"Rolled {total} in {number_of_dices} rolls.")
    return total
  
def drawBoard(board_arg):
    board=''
    for i in range(len(board_arg)):
        board+=("[")
        for player in players:
            if player.current_position==i:
                board+=player.name[0]

            else:
                board+='.'

        board+=("]")
    return board

hrac_1=Player(15,"bali")
hrac_2=Player(15,"fofo")
hrac_3=Player(15,"kamil")

owned_buildings=[]

games=0
turns=0
for player in players:
    wins_loses[player.name]=0
def printBuildings(player):
    for i in player.owned_buildings:
        print(f"{board[i].name} | {board[i].price}")
while True:
    for player in players:
        roll = diceRoll(1)
        #*Rolling dice
        if player.current_position+roll<len(board):
            player.current_position+=roll
            
        else:
            fuzzyPosition=player.current_position+roll - len(board)
            player.current_position=0
            player.current_position+=fuzzyPosition
            #print(f"{player.name} passed the start, got 2M")
            player.money+=1

        #*Buying things
        if player.money>=board[player.current_position].price and player.current_position not in owned_buildings and board[player.current_position].color!='special':
            player.money-=board[player.current_position].price
            player.owned_buildings.append(player.current_position)
            owned_buildings.append(player.current_position)
            #print(f"{player.name} bought {board[player.current_position].name}, money remaining {player.money}")
        if player.current_position in owned_buildings  and player.current_position not in player.owned_buildings:

            for i in players:
                
                if player.current_position in i.owned_buildings:
                    player.money-=board[player.current_position].price/2#! TO BE REVISE LATER
                    i.money+=board[player.current_position].price/2
                    #print(f"{player.name} paid {board[player.current_position].price/2} for {board[player.current_position].name} to {i.name}")
                    pass
    turns+=1   
    if turns>1000:
        draws+=1
        games+=1

        turns=0
        owned_buildings=[]
        players=[

        ]
        players_dict={

        }
        hrac_1=Player(15,"bali")
        hrac_2=Player(15,"fofo")
        hrac_3=Player(15,"kamil")
    print(drawBoard(board))
    for player in players:
        #print(f"{player.name} has {player.money} M")
        if player.money<0 :

            print(f"Player {player.name} has lost!!!")
            #printBuildings(player)
            player.loses+=1
            
            for i in players:
                if i.name!=player.name:
                    i.wins+=1
                    wins_loses[i.name]+=1


            games+=1

            turns=0
            owned_buildings=[]
            players=[

            ]
            players_dict={

            }
            hrac_1=Player(15,"bali")
            hrac_2=Player(15,"fofo")
    
     
    if games>=1:
        print(f'simulated {games} games')
        with open("results.txt",'a') as f:
            for player in wins_loses:
                f.write(str(player)+str(wins_loses[player])+'\n')
            f.write("\ndraws"+str(draws))
        wait(1000)

    #continue_=input("press enter to continue")
"""
    if len(owned_buildings)>=6:
        print("ALL BUILDING BOUGHT")
        continue_=input("press enter to continue")
"""

    