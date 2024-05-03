#A = [1, 2, 2, 3, 4] # increasing
#A = [6,4,2,2,1] # decreasing
A = [1,9,3] # normal
is_inc = 0
is_desc = 0

# check for monotone 
for i in range(len(A)-1):
    if A[i] < A[i+1]:
        is_inc = 1
    if A[i] > A[i+1]:
        is_desc = 1

if (is_inc == 1 and is_desc ==1):
    print("The Arr is Not Monotonic")
elif is_desc == 1:
    print("The Arr is monotonically decreasing")
elif is_inc == 1:
    print("The Arr is monotonically increasing")