# Problem Statement:
"""Given a integer N, return all divisor of N. A divisor of N is a positive integer that divides N without leaving a remainder.
Example:
N = 36
output: [1,2,3,4,6,9,12,18,36]"""

# Approach 1:
# number = int(input("Enter a number: "))
# divisors = [val for val in range(2,number) if number%val==0]
# divisors.append(1)
# divisors.append(number)
# print(divisors)
"""This is an easy approach where i have taken a number as input whose divisor we need to find.
then i have used the list comprehension method to find the divisor.
I have created a list where in i have used a for loop which runs from 2 to the number-1.
Inside the loop, if the number % iteration becomes zero then the number is divisor and we add that number in the list.
"""


# Approach 2:
# import math
# number = int(input("Enter a number: "))
# divisors = []
# for val in range(1,int(math.sqrt(number))+1):
#     if number % val == 0:
#         divisors.append(val)
#         if val != number // val:
#             divisors.append(number // val)
# divisors.sort()
# print(divisors)

"""This is the most optimal approach where i have taken a number and created a empty list.
Then i have created a loop running from 1 to root of number. this is done because after a certain point the number are repeated in reverse order.
Lets say we have number 36, its divisor will be:
1 x 36
2 x 18
3 x 12
4 x 9
6 x 6
after 6 x 6 the number will be repeated in reverse order. so here inside the loop first we have taken the number whose remainder is 0 when divided by the number.
if the remainder is zero, we append that number as it is a divisor and then we check other condition which is if the value is not equal to the number divided by the value.
if they are not equal then we append that as well. So like this we get the entire pair. we repeat this till we reach the repeatation.
this is the most optimal solution because the approach 1 time complexity was O(n) and the time complexity for this is O(root(n))"""


#Approach 3:
import math
number = int(input("Enter a number: "))
divisors = set()
for i in range(1,int(math.sqrt(number))+1):
    if number % i == 0:
        divisors.add(i)
        divisors.add(number // i)

print(sorted(divisors))

"""This is also similar approach to the above one. the only difference is that here i have used the sets and above i had used lists.
Rest the time complexity will remain the same."""