#writing a code to fing the possible subspace of rolling dice where the sum of both the dies are 5
# v2 also find the probability if total sample space is 36

# find = int(input("Enter the num to find prob that the sum of num between 2 dice is : "))
# a= 0

# for i in range(1,7):
#     for j in range(1,7):
#         if i+j ==find:
#             a +=1
#             #print(i,j, 'num of iteration : ',a)

# prob =  (a/36)*100
# print(prob)

# def area(r):
#     pi = 3.14
#     a = pi * (r**2)
#     return a

# print(area(5))

# code to print the full star patten for odd numbs

# way to find midpoint print(7//2 +1)

n = 5
mid = ((n//2)+1)

for i in range(1, n+1, 2):
    print("_" *(n-mid), "*" *i, "_" *(n-mid))
    mid = mid +1
