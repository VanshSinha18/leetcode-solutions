# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# idea here is that we use a two pointer approach to find the maximum profit
# we use a left pointer to buy the stock and a right pointer to sell the stock
# we move the right pointer to the right and calculate the profit
# if the profit is greater than the maximum profit, we update the maximum profit
# if the profit is less than the maximum profit, we move the left pointer to the right
# we return the maximum profit

def maxProfit(prices: List[int]) -> int:
    lowest_price = 100000000
    max_profit = 0

    for price in prices:
        if price < lowest_price:
            lowest_price = price
        elif price - lowest_price > max_profit:
            max_profit = price - lowest_price

    return max_profit

print(maxProfit([7,1,5,3,6,4]))