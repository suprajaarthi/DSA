# Recursive function to check if `str[low…high]` is a palindrome or not
def isPalindrome(str, low, high):
 
    # base case
    if low >= high:
        return True
 
    # return false if mismatch happens
    if str[low] != str[high]:
        return False
 
    # move to the next pair
    else:
        return isPalindrome(str, low + 1, high - 1)
    # isPalindrome("malayalam",0,8)  0!>=8
    # isPalindrome("alayala",)    1!>=7
    # layal 2 6 
    # ayal 3 5 
    # aya 4>=4  return True 
    
 
 
str = "malayalam"
 
if isPalindrome(str, 0, len(str) - 1):
    print("Palindrome")
else:
    print("Not Palindrome")
 


