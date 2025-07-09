# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# idea here is that we use a two pointer approach to check if the string is a palindrome
# we use a left pointer to check the first character and a right pointer to check the last character
# we move the left pointer to the right and the right pointer to the left
# if the characters at the left and right pointers are not the same, we return false
# if the characters at the left and right pointers are the same, we move the left pointer to the right and the right pointer to the left
# if we reach the middle of the string, we return true

def isPalindrome(s: str) -> bool:
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    
    left = 0
    right = len(clean_s) - 1

    while left < right:
        if clean_s[left] != clean_s[right]:
            return False
        left += 1
        right -= 1
    return True

