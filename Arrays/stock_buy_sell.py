# Problem Statement:
"""given an array of price where price[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single
day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
"""


# Approach 1:
prices = [7,1,5,3,6,4]

# max_profit = 0
# for i in range(len(price)):
#     for j in range(i+1, len(price)):
#         max_profit = max(max_profit, price[j] - price[i])
# print(max_profit)
"""Here in this approach, i have used the nested loops.
Here first i will iterate to the entire loop then the second loop will run from i+1 index to length of the array.
Inside the second loop, we use the maximum function to find the max between the max_profit and difference between price of index j and price of index i.
Once we iterate the entire loops, we print the max_profit.
"""



# Approach 2:
min_price = float('inf')
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        max_profit = max(max_profit, price - min_price)
print(max_profit)
"""This is the most optimal approach to solve the transaction.
Here we run a loop where we iterate through the entire loop until we find the max profit.
Inside the loop we have set a if-else condition where if the price that is the value in the array is less than the min_price which we have set to 100000 at the start so that the condition becomes true for the first element in the array.
then we make the min_price to the value of price.
If the price is not less then min_price then we enter the else condition where we find the max_profit.
Here we use the same maximum function to find the max_profit.
"""