#armstrong numbers with python

def len(n): # this function to return the value of length of a number
    length = 0
    while n > 0:
        n = n//10 #floor division so the (.) point part after the number gets dropped
        length = length + 1
    return length


def is_arm(length , number ):
    poo = 0
    while number > 0:
        t = number % 10
        poo = poo + (t**length)
        number = number // 10
    return poo



num = int(input("give a num for cheking : "))

n = len(num)

if num == is_arm(n, num):
    print("The number ",num," is a armstrong number" )
else:
    print("The number ",num," is not a armstrong number" )
