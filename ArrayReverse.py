# #arr = [1,2,3,4,5,6]

# # def highest(arr , n):
# #     ret = arr[0]
# #     for i in range(1, n):
# #         if ret < arr[i]:
# #             ret = arr[i]
# #     return ret

# # n = len(arr)
# # print("The highest num is : ", highest(arr, n))

# #### To reverse the array from left side for n number of steps
# arr = [1,2,3,4,5,6]
# length = len(arr)
# step = 3
# temp = []
# for i in range(0, step): #Save step number of elements in temp array
#     temp.append( arr[i] ) 

# for j in range(step, length): # shift remaining elements to the left side
#     arr[j - step] = arr[j]

# for k in range(length-step , length): #coping temp[] element into the right side of arr 
#     arr[k] = temp[k - (length-step)]

# print(arr)

given_string = "gerekaallaapqrsttsrq"
print(given_string[0:1])