from random import randint
import os

def deck(): ##Function for define de card
    Value=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    Tipo=["C","D","T","P"]
    card=[]

    for i in Tipo:
        for j in Value:
            card.append(j+ "of" + i +" ")
    return card


def value(cardvalue): ## Function for define de card value
    if cardvalue[:1] in ("J","Q","K","1"):
        return int(10)
    elif cardvalue[:1] in ("2","3","4","5","6","7","8","9","10"):
        return int(cardvalue[:1])
    elif cardvalue[:1] == "A":
        print(str(cardvalue))
        num = input("Chose the value of your card 1 or 11 >>")
        while num != "1" or num != "11":
            if num =="1":
                return int(1)
            elif num == "11":
                return int(11)
            else:
                num = input("Chose the value of your card 1 or 11 >>")

def new_card(card): #Function for new card random
    return card[randint(0,len(card)-1)]

def remove_card(card,cardvalue): #Function for remove card of the deck
    return card.remove(cardvalue)

while True: #Inicio de programa

    print ("\n\n Bienvenido a Black-Jack online \n")
    
    Players= int (input ("Ingrese el numero de jugadores >> "))

    new_deck=deck()
    playerCards = {}
    playerValue = {}
    for i in range(Players): #First hand, two cards for all the players
        
        card1=new_card(new_deck)
        remove_card(new_deck,card1)
        card2 = new_card(new_deck)
        remove_card(new_deck,card2)

        value1=value(card1)
        value2=value(card2)
        
        totalv = value1+value2
        totalc = card1+card2
        
        playerCards[i] = totalc
        playerValue[i] = totalv
        
    for i in range(Players):
        print ("\n Player number ",i)
        print (playerCards[i])
        print (playerValue[i])

    ##Second Hand, the player decide how much cards he want
        
    for i in range(Players): ##Loop for more cards
        print ("\n The player ", i , " wants more cards?")
        m=int(input ("Press 1 for more cards or 0 for pass "))

        if m==1:
            while True: ##Loop for add the new cards
                extracard=new_card(new_deck)
                remove_card(new_deck,extracard)
                extravalue=value(extracard)

                totalv = playerValue[i]+extravalue
                totalc = playerCards[i]+extracard

                playerCards[i] = totalc
                playerValue[i] = totalv

                print ("The new card is ",extracard, "and you have a total of ",totalv)

                m=int(input ("\n Pres 1 for more cards or 0 for pass "))

                if m==1:
                    continue
                if m==0:
                    break
                
    plwin=0
    mx=0
    for i in range(Players): ##loop for define the winner
        if playerValue[i]<22:
            if mx<playerValue[i]:
                mx=playerValue[i]
                plwin=i

    print ("\n All the cards by player")
    
    for i in range(Players):
        print ("\n Player number ",i)
        print (playerCards[i])
        print (playerValue[i])
        
    print ("\n CONGRATULATIONS \n The winner is player number", plwin)    

