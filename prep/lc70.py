# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        one , two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one
    
print(Solution().climbStairs(45))

# explanation:

# 1. we use two variables to store the number of ways to reach the current step
# 2. we use a for loop to iterate through the steps
# 3. we update the variables based on the number of ways to reach the current step
# 4. we return the number of ways to reach the top of the staircase

# in a array [0, 1, 2, 3, 4 , 5] -> index 5 has 1 way to reach the top

# index 4 has 1 way to reach the top
# index 3 has one step to 4 and two steps to 5, but we know that index 4 has 1 way to reach the top
# so index 3 has value of index 4 + index 5 = 1 + 1 = 2
# index 2 has one step to 3 and two steps to 4, but we know that index 3 has 2 way to reach the top
# so index 2 has value of index 3 + index 4 = 2 + 1 = 3
# index 1 has one step to 2 and two steps to 3, but we know that index 2 has 3 way to reach the top
# so index 1 has value of index 2 + index 3 = 3 + 2 = 5
# index 0 has one step to 1 and two steps to 2, but we know that index 1 has 5 way to reach the top
# so index 0 has value of index 1 + index 2 = 5 + 3 = 8
# so the total number of ways to reach the top is 8