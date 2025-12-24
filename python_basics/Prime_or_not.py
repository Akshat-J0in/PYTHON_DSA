#problem statement:
"""Given a integer N, return true if the number is prime else return false.
for example:
we have a number N = 11
output: true"""

# Approach 1
# number = int(input("Enter a number: "))
# if number <= 1:
#     print("The number is NOT prime prime")
# else:
#     for i in range(2, number):
#         if number % i == 0:
#             print("The number is not prime")
#             break
#     else:
#         print("The number is prime")
"""
Here i have used the basic approach where first we take the number from the user.
If the number is less than or equal to 1 then we print it as not prime number.
else we run a loop here from the range of 2 to number - 1.
Inside the loop we check a condition if the remainder of number after dividing it by i will be zero or not.
If not zero then the number will be not prime and we will break the loop.
if its zero then we will continue with the loop and see if any other number is not divisible by zero. If not divisible then it is a prime number.
"""


# Approach 2:
# number = int(input("Enter a number: "))
# if number <= 1:
#     print("Not a prime number")
# else:
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")
"""Here for this approach i have used a flag variable.
the start is the same as above that we first take a number then we see if the number is greater than or equal to 1.
then i have used a variable which is 'is_prime' and this is true initially.
then we run the loop same as above. If the number is not divisible by i then we continue and see for other number as well and if not divisible by all the number then its a prime.
If the number is divisible then we make the 'is_prime' false and then we get out of the loop and print its not a prime number."""


# Approach 3:
# import math
# number = int(input("Enter a number: "))
# if number <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2,int(math.sqrt(number))+1):
#         if number % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
"""This is the most optimal method that i have used.
Here the initial condition remain the same.
The main difference is when we run the loop, now we are only taking half of the values. as we are doing the square root.
For example i have a number 5, its square root will be 2.23+1 which is 3. so we divide the number by 1,2,3 and see if it is divisible by it or not.
If not then its a prime number else its a prime number.
This is the optimal approach because here the number for which we are running the loop becomes less than half hence it becomes faster.
"""


# Approach4:
# import math
# number = int(input("Enter a number: "))
#
# if number > 1 and all(number%i != 0 for i in range(2,int(math.sqrt(number))+1)):
#     print("Prime number")
# else:
#     print("Not a prime number")
"""This is a interesting approach. Here i have taken a number first from the user.
then i have used a if condition, that is if the number is greater than 1 AND if no number is divisible by the number for which we ran the loop then its a prime number else its not a prime number.
Lets see the if in more detail:
here all is the function that returns true if all the value inside is true. if any one value is also false then the entire condition becomes false
so here we ran a loop from 2 to sqrt of the number. Then we check for each number if its divisible by the number or not.
if not then its a prime number else its not a prime number."""


# Approach 5:
number = int(input("Enter a number: "))
if number > 1 and len([i for i in range(2, number) if number%i==0]) == 0:
    print("The number is prime.")
else:
    print("The number is not prime.")
"""Here i have used a list comprehension method. Here we used the length of the list as condition if the length of the list is zero and if number is greater than 1 then its a prime number. Else its not a prime number."""
