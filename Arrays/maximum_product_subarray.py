# Problem Statement:
"""Given an array that contains both negative and positive integer, find the maximum product subarray.
For example:
Num = [1,2,-3,0,-4,-5]
Output = 20
"""



# Approach 1:
# arr = [1,2,-3,0,-4,-5]
#
# max_product = arr[0]
# min_product = arr[0]
# result = arr[0]
#
# for i in range(1, len(arr)):
#     num = arr[i]
#     temp = max(num,num*min_product,num*max_product)
#     min_product = min(num,num*min_product,num*max_product)
#     max_product = temp
#     result = max(result,max_product)
# print(result)
"""This is the optimal approach and easy to understand.
Here what i have done is created max_product, min_product, result.
Then in the for loop i have first found the max of the number, product between num and min_product and num num and max_product
similarly i have done to find the min_product.
then i have found the result by taking the max of result and max_product.
Here we have to monitor the min_product because we have negative number.
"""



# Approach 2:
arr = [1,2,-3,0,-4,-5]

max_product = float('-inf')

for i in range(len(arr)):
    product = 1
    for j in range(i,len(arr)):
        product *= arr[j]
        max_product = max(max_product, product)

print(max_product)
"""This is a brute force approach.
It is simple to understand.
"""