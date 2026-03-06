# Problem Statement:
"""Given 2 sorted array num1 and num2, merge both the arrays into a single array sorted in non decreasing order.
The final array should be sorted inside the array nums1 and it should be done in-place
for example:
Input: num1 = [-5,-2,4,5,0,0,0], num2 = [-3,1,8]
Output: [-5,-3,-2,1,4,5,8]
"""



# Approach 1:
# num1 = [0,2,7,8,0,0,0]
# num2 = [-7,-3,-1]
# arr_2_count = 0
#
# for i in range(len(num1)-1):
#     if num1[i] == 0 and num1[i+1] == 0:
#         num1[i] = num2[arr_2_count]
#         arr_2_count += 1
#     else:
#         continue
# num1[-1] = num2[-1]
# num1.sort()
# print(num1)
"""Here in this approach, i have created a for loop where it will run till second last element.
Inside the loop, i have set a condition where if the num is 0 and if the next number is also zero then we have insert the element of the second array in the first one.
Then we increase the count by 1.
Once this is done, there will the last index where we have not inserted the value so we will do it manually and then we will sort the array then print it.
"""



# Approach 2:
num1 = [0,2,7,8,0,0,0]
num2 = [-7,-3,-1]

m = 4
n = 3

i = m-1
j = n-1
k = m+n-1

while j>=0:
    if i >= 0 and num1[i] > num2[j]:
        num1[k] = num1[i]
        i -= 1
    else:
        num1[k] = num2[j]
        j -= 1
    k -= 1
print(num1)
"""Here in this approach, we have first set the value of m and n that is here m = 4 means that in array 1, we have 7 values but there are 3 position which needs to be filled by array 2 so they are zero.
Hence we make m = 4 and n = 3 as there are 3 element in the array 2.
now we set the value of i,j and k.
Here i is set at index 3 that is at value 8 and j is set at index 2 that is at value -1 and k is set at the index 6 that is the last value of array 1.
now we run a while loop till our j is greater than or equal to 0.
If i is greater than or equal to 0 and value of array 1 is greater than array 2 then we place the value of array 1 at the position of k and we decrement the count of i.
else we put the value of array 2 in the position of k and we decrement the count of j
and then we decrement the value of k
then print the value.
"""