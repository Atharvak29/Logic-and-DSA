# def longest_palindrome(h):
#   if len(h)==0:
#     return ""

#   max_length=1
#   start=0

#   for i in range(len(h)):
#     #check for odd length palindrome
#     left,right=i,i
#     while left>=0 and right<len(h) and h[left]==h[right]:
#         if right-left+1>max_length:
#           start=left
#           max_length=right-left+1
#         left-=1
#         right+=1
#     #check for even length palindrome
#     left,right=i,i+1
#     while left>=0 and right<len(h) and h[left]==h[right]:
#         if right-left+1>max_length:
#           start=left
#           max_length=right-left+1
#         left-=1
#         right+=1
#   return h[start:start+max_length]

# print(longest_palindrome("vivek"))

def is_palindrome(s):
    return s == s[::-1]

def find_palindromic_substrings(s):
    palindromes = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.append(substring)
    return palindromes



# Example usage:
given_string = "gerekaallaapqrsttsrq"
palindromes = find_palindromic_substrings(given_string)

# max = palindromes[0]
# for k in range(len(palindromes)):    
#     if (palindromes[k]) > max:
#         max = palindromes[k]3
# print(max)

max = palindromes[0]  
for k in palindromes:
    if len(k) > len(max):  
        max = k
print(max)



print("Palindromic substrings:", palindromes)
#print("Longest elemet is : ", len(palindromes))



