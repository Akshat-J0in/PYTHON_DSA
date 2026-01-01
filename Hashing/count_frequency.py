#Problem Statement:
"""Given an array, we have to find the number of occurrences of each element in the array.
For example:
input:arr[] = {10,5,10,15,10,5}
output: 10 -> 3, 5 -> 2, 15 -> 1
"""



# Approach 1:
# arr = list(map(int, input("Enter the array element: ").split()))
#
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
#
# for key,val in freq.items():
#     print(f"{key} -> {val}")
"""This is the approach 1 for hashing.
Here first i have taken a array as input from the user.
then i have created a empty dictionary where we will store the values.
Then i have run a loop where we iterate the array.
Here the first condition is that if num in freq then we increment its corresponding value(key) by 1(value)
if the num(key) is new that is, the num is not present in the freq then we add the num in the dictionary by assigning it with the value 1.
once our dictionary is complete, we iterate using .items() function which helps get the key, value pair."""



# Approach 2
# from collections import Counter
# arr = list(map(int, input("Enter the array element: ").split()))
# freq = Counter(arr)
# for key,value in freq.items():
#     print(f"{key} -> {value}")
"""Here for this approach, i have used the inbuild collection library in which i have used the sub class Counter.
Counter works similar to what for loop i had written in the approach 1 to fill the dictionary with values.
then i have used the .items() function which helps get the key, value pair."""



# Approach 3
arr = list(map(int, input("Enter the array element: ").split()))
visited = []
for i in range(len(arr)):
    if arr[i] in visited:
        continue
    count = 1
    for j in range(i+1, len(arr)):
        if arr[j] == arr[i]:
            count += 1
    print(f"{arr[i]} -> {count}")
    visited.append(arr[i])
"""Here this is not at all the optimal approach for hashing.
here the time complexity is:O(n^2) which is not good.
Here first i have taken the user input for array then i have run the first for loop where i iterate it for the entire array.
inside the first for loop, i have set a condition where if arr[i] is in visited then we stop that perticular iteration and we move on to next i value.
if we go ahead of that condition then i have set a variable count which is 1 and run another nested for loop where it will iterated from i+1 to the last element of the array.
then i have checked a condition where if the arr[j] == arr[i] then we increment the count after that we come out of the loop and print the key, value pair.
"""