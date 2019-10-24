form random import randint
import os

def deck(): ##Function for define de card
    Value=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    Tipo=["C","D","T","P"]
    card=[]

    for i in Tipo:
        for j in Value:
            card.append(j+ "of" +i)
        return card


def value(cardvalue): ## Function for define de card value
    if cardvalue[:1] in ("J","Q","K"):
        return int(10)
    elif cardvalue[:1] in ("2","3","4","5","6","7","8","9","10"):
        return int(cardvalue[:1])
    elif cardvalue[:1] == A
        print(str(cartavalue))
        num = input("Chose the value of your card 1 or 11")
        while num != "1" or num != "11"
            if num =="1":
                return int(1)
            elif num == "11":
                return int(11)
            else:
                num = input("Elija el valor de su carta 1 o 11")

def new_card(card):
    return card[randint(0,len(deck)-1)]

def remove_card(card,cardvalue):
    return card.remove(cardvalue)

def first_hand(player)
    new_deck=card_deck()
    card1=new_card(new_deck)
    remove_card(new_deck,card1)
    card2 = new_card(new_deck)
    remove_card(new_deck,card2)
    V[player]=[]

a={}
def num_players():
    players= int (input ("Number of players"))

    for i=0;i<players;i++ :
        key=
        
    

def menu():

    print (

while True:

    menu()

    Players= input ("Ingrese el numero de jugadores >> ")


    playerList = []
    for i in range(Players):
        playerList[i] = ["Jugador"+i]

    #Primera Mano
    for i in range(Players)
        player=
    





    
