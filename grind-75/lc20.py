# Problem 20: Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        # create a empty stack 
        stack = []

        # map the closing to open 
        bracket_map = {')':'(', '}':'{', ']':'['}

        # loop over each char in s
        for char in s:
            # if the char is a opening bracket, add to stack
            if char in bracket_map.values():
                stack.append(char)
            # else if the char is a closing bracket
            # check if the stack is empty -> return false
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
        return not stack
    
# test cases
sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))


