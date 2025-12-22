#Problem Statement:
"""Given 2 integers N1 and N2, find there greatest common divisor. For example:
we have N1 = 9 and N2 = 12.
factors of 9 = 1,3,9
factors of 12 = 1,2,3,4,6,12
so the common factor is 1,3 and the greatest common divisor is 3.
hence the answer will be 3"""

# val1 = int(input("Enter the first number: "))
# val2 = int(input("Enter the second number: "))
# A = []
# B = []
# for divisor in range(1,val1+1):
#     if val1 % divisor == 0:
#         A.append(divisor)
# print("Divisor for the first number: ", A)
# for divisor in range(1,val2+1):
#     if val2 % divisor == 0:
#         B.append(divisor)
# print("Divisor for the second number: ", B)
# common = list(set(A) & set(B))
# print("common divisors: ", common)
# print("The GCD for the number is: ",max(common))
"""This is one of the method to find the greatest common divisor of two numbers.
Here we have created 2 variable to take input then we have used two empty list. In the first for loop we ran the loop from 1 to value 1.
if the number is divisible by the number 1 then we append it in one of the list.
similarly we did in second for loop with second number.
Then we have used the concept of sets. Where we have found the intersection to find the GCD for the two number."""

# val1 = int(input("Enter first number: "))
# val2 = int(input("Enter second number: "))
# while val2 != 0:
#     val1,val2 = val2, val1 % val2
#
# print("The GCD for the two number is: ",val1)
"""This is the most optimal approach for the code. THis type of method is called Euclidean algorithm.
we have first take 2 values from the user.
Then we have used while loop where till our second element becomes zero.
Now inside the loop we have used the concept of tuple unpacking.
Tuple unpacking is similar to:
temp = a%b
a = b
b = temp
And once the value 2 becomes zero, we are out of the loop.
"""