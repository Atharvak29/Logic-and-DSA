import random
import time


Try_num = 2
print("This game is about picking a random number between 1 to 100 with clever hints")
time.sleep(2)                            #using sleep function to add dramatic effect to code

print("\nLet the game begin....")

print("\nPlayer what is your \"NAME\" : ")
Name = str(input())                      #getting a string input from user as theri name 


print("Enter a number for your first guess : ")                       
guess = int(input())                     #Getting an integer input from user as gussing value
    
                
Random_num = random.randint(1,101)
#print(Random_num)                       #printing the random number just to check

while True:
    if Random_num == guess:
        print("WOOHOO YOU GUESSED IT CORRECTLY!!!")
        break
    elif Try_num == 3:
        if guess%2 == 0:
            print("\"HINT\":The answer is Even number")
        else:
            print("\"HINT\":The answer is Odd number")  
    elif Try_num == 5:
        if Random_num > guess:
            print("\"HINT\":Answer is greater than {}".format(guess))
        else:
            print("\"HINT\":Answer is lesser than {}".format(guess))
    elif Try_num == 9:
        if Random_num > guess:
            print("Add {} to {}".format((Random_num-guess), guess))
        else:
            print("substract {} from {}".format((guess-Random_num), guess))
    else:
        guess = int(input("Enter a number for your {} guess : ".format(Try_num)))            


    Try_num = Try_num + 1               #To count the number of tried user makes

print("You guessed the number in {} trys".format(Try_num))