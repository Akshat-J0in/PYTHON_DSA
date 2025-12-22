#problem statement:
"""Given an integer N, return true it is an Armstrong number otherwise return false.
What is an Armstrong number?:
It is an number that is equal to the sum of its digits each raised to the power of the number digits
for example:
we have a number:
N = 153.
so 1^3 + 5^3 + 3^3 = 153.
hence it is a armstrong number."""

# approach 1:
# number = int(input("Enter a number: "))
# temp = number
# total = 0
# digits = len(str(number))
# while temp > 0:
#     digit = temp % 10
#     total += digit ** digits
#     temp //= 10
#
# if total == number:
#     print("It is an Armstrong number")
# else:
#     print("It is not an Armstrong number")
"""This is the optimal solution where i have taken a number from the user. introduced a temp variable so that we can use it inside the loop.
we have taken the length of the digits that is how many digits are there in the number.
then we run a while loop till the temp variable becomes zero.
inside the loop, we find the remainder of the number first just how we did for the code reverse the number.
once we have the remainder, we add it in the total variable by raising it with the digits variable. for example we have a number 1325, we add 5^4 to the total
once that is done, we can compare it with the original number. if both of them are same then its a armstrong number else not.
"""

# Approach 2:
# number = input("Enter a number: ")
# digits = len(number)
# total = sum(int(d)**digits for d in number)
#
# if total == int(number):
#     print("It is an Armstrong number")
# else:
#     print("It is not an Armstrong number")

"""In this method, we have used the concept of strings. Here i have taken a input number in form of string.
then i have taken the length of the number just like done in approach 1.
then i have used the for loop to iterate every  character in the number using the 'in' keyword. 
i have taken every character then converted it into int and raised it to the length of the string that is digits.
for example i have a string '153', i have take '3' in first iteration then converted it into int then cubed it. 3^3
once that is is done, i have added each number of the iteration with the variable total using the sum operation."""

# Approach 3:
number = int(input("Enter a number: "))
digits = len(str(number))
total = sum([int(d)**digits for d in str(number)])
if number == total:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

"""In this approach we have used the list comprehension, where i have taken a input as int.
then i have taken the length of the number just like done in approach 1.
similar to approach 2, we have run the loop but the only different is we have created a list and then stored each number as individual just like in array.
if we have a number 153, then the list has [1,125,27] then we have taken the sum of this list."""