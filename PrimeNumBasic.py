# n = int(input("Enter a num : "))


# for i in range (2, n):
#     if n % i == 0:
#       print("not PRIME")
#       break
# else:
#     print("prime")

#optimized solution for finding prime number in py

# import math
# n = int(input("Enter a num : "))

# for i in range(2, int(math.sqrt(n)) + 1 ):
#     if n % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

#prime number in an interval

s = int(input("Enter first number form the range (>=2): "))
n = int(input("Enter second number form the range : "))
prime = []

for i in range(s, n+1):
    for a in range(2, i):
        if i % a == 0:
            break
    else:
        prime.append(i)

print(prime)


 