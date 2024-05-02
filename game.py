#This a Rock, paper , scissor game 

import random

list = ["Rock", "Paper", "Scissor"]

def Comp_Choice(list):                                  #Function for the computer to make the choice
    Comp_Choice = random.choice(list)
    print(Comp_Choice)
    return Comp_Choice

def Usr_Choice():                                       #Function to get the choce from user
    Usr_Choice = str(input("Enter one of the following Rock, Paper , Scissor : "))
    return Usr_Choice


def Compare(user ,computer):                            #Functions to compare the results and assign points
    score = 0                     
    if ((user == "Rock") and (computer == "Paper")):
        print("User won")
        score = score + 1
    elif (user == "Rock" and computer == "Scissor"):
        print("User won")   
        score = score + 1 
    elif (user == "Paper" and computer == "Rock"):
        print("User won")
        score = score + 1
    elif (user == "Paper" and computer == "Scissor"):
        print("Computer won")
    elif (user == "Scissor" and computer == "Paper"):
        print("User won")
        score = score + 1
    elif (user == "Scissor" and computer == "Rock"):
        print("Computer won")
    elif ((computer == "Rock") and (user == "Paper")):
        print("User won")
        score = score + 1
    elif ((computer == "Rock") and (user == "Scissor")):
        print("Computer won")
    elif (computer == "Paper" and user == "Rock"):
        print("Computer won")
    elif (computer == "Paper" and user == "scissor"):
        print("User won")
        score = score + 1
    elif (computer == "Scissor" and user == "Paper"):
        print("Computer won")
    elif (computer == "Scissor" and user == "Rock"):
        print("User won")
        score = score + 1
    elif (user == computer):
        print("Its a tie")


computer = Comp_Choice(list)
user = Usr_Choice()
Compare(user, computer)


