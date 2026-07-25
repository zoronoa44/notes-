import random as rd
import math

def guessno():
    game_level = int(input(" enter the no of level you wanna play \n  1. guess number between 10 to 10 \n 2. guess no between 1 to 100 "))
    if (game_level == 1):
        guessno_1()
    elif (game_level == 2):
        guessno_2()
    else:
        print("please enter a valid no")

def guessno_1():
    print("welcome to game ")
    lifes = 3
    i = 0 
    
    user_choice = int(input("please enter a number between 1 to 10  : "))
    while lifes != 0 :
        comp_choice = rd.randint(1,10)
        if (comp_choice == user_choice): 
            print("you win")
            i += 1
            print(f"total wins = {i} ")
            print(" remaning lifes:  ", lifes * "❤️")	
        else :
            lifes -= 1
            print(" remaning lifes:  ", lifes * "❤️")

def guessno_2():            
    print("welcome to game ")
    lifes = 3
    i = 0 
    user_choice = int(input("please enter a number between 1 to 100  : "))
    while lifes != 0 :
        comp_choice = rd.randint(1,100)
        if (comp_choice == user_choice): 
            print("you win")
            i += 1
            print(f"total wins = {i} ")
            print(" remaning lifes:  ", lifes * "❤️")
        else :
            lifes -= 1
			print("remaning lifes: ", lifes * "❤️")

def maths ():
    print("welcome to game ")
    game_level = int(input("enter the no of game you wanna play \n 1. add and subract  \n 2.multiply and divide  "))
    if (game_level == 1):
        addsub()
    elif (game_level == 2):
        muldiv()
    else:
        print("please enter a valid no")

def addsub():
    print("welcome to game ")
    lifes = 3
    i = 0 
    k = 0
    total = 0
    if lifes >0 :
        no_list =[]
        j = rd.randint (2,6)
        while j != 0 :
            comp_choice = rd.randint(10,1000)
            
            
            if (rd.choice[1,-1] == 1):
                total+=comp_choice
                print(f"+{comp_choice}")
    
            else:
                total -= comp_choice
                print(f"-{comp_choice}")
                
        user_choice = float(input())
            
        if (total == user_choice): 
            print("you win")
            i += 1
            print(f"total wins = {i} ")
            print(" remaning lifes:  ", lifes * "❤️")
        else :
            lifes -= 1
            print(" remaning lifes:  ", lifes * "❤️")
    else:
        print("you lose")
        
        
        
def muldiv():
	 print("welcome to game ")
    lifes = 3
    i = 0 
    k = 0
    mul = 1
    div = 1
    if lifes >0 :
        no_list =[]
        j = rd.randint (2,6)
        while j != 0 :
            comp_choice = rd.randint(10,100)
                   
                mul*=comp_choice
                print(f"*{comp_choice}") 
               
     

                 print ("÷")
    
		while j != 0 :
            comp_choice = rd.randint(10,1000)            
                div *= comp_choice
                print(f"{comp_choice}")
                
                
        total = mul / div
                
        user_choice = float(input())
            
        if (total == user_choice): 
            print("you win")
            i += 1
            print(f"total wins = {i} ")
            print(" remaning lifes:  ", lifes * "❤️")
        else :
            lifes -= 1
            print(" remaning lifes:  ", lifes * "❤️")
    else:
        print("you lose")


def rock():
	print("welcome to game ")
	
	user_choice = int(input("enter the no \n 1.rock\n 2. paper \n 3.scissors "))
	choice_list = ["rock", "paper","scissors"]
	
	consec_wins =0
	if (user_choice == choice_list[i]):
		print(f"computer choosed{choice_list[i]} ,game tied ")
	elif (user_choice == 1 and choice_list[i] == paper):
		print("computer choosed paper , you lose")
		consec_wins =0
	elif (user_choice == 1 and choice_list[i] == scissors):
		print("computer choosed paper , you win ")
		consec_wins += 1
		print (f"consecutive wins = {consec_wins")
	elif (user_choice == 2 and choice_list[i] == scissors):
		print("computer choosed paper ,you lose ")
		consec_wins =0
	elif (user_choice == 2 and choice_list[i] == rock):
		print("computer choosed rock , you win ")
		consec_wins += 1
		print (f"consecutive wins = {consec_wins")
	elif (user_choice == 3 and choice_list[i] == paper):
		print("computer choosed paper ,, you win ")
		consec_wins += 1
		print (f"consecutive wins = {consec_wins")
	elif (user_choice == 3 and choice_list[i] == rock):
		print("computer choosed paper ,, you lose")
		consec_wins =0
	






game = int(input("enter the game no you want to play\n  \n 1.guess the number \n 2.math \n  3.rock paper sccicors"))



if (game == 1):
    guessno()
elif (game ==2):
    maths()
elif(game == 3):
    rock()
else:
    print("please enter a valid game no")











