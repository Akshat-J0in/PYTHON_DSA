#problem statement:
""" Given an integer N, return the number of digits in N. that is we have to find the number of digits present in the given number."""

""" For example we have a input:
N = 12345
OUTPUT = 5
Explanation: the number 12345 has 5 digits
"""

# Approach 1: where i will use the concept of loops:

# num = int(input("Enter a number: "))
# i = 0
# count = 0
# while i < num:
#     count += 1
#     num = int(num / 10)
#
# print(count)

""" Explanation: here i have used the while loop where i have created a variable 'i' to track the number and set a 
condition where, if the number becomes less than 0, we exit the loop. then we have set a count variable will will increment itself by 1 every time when the loop runs.
after that we have divided the number by 10 to make it smaller so that the loop does not run again and again(infinite loop)
IMPORTANT NOTE: WE HAVE TO DIVIDE THE NUMBER IN FORM OF INT ELSE WE WILL GET THE NUMBER IN FLOAT AND THUS WE WILL GET A WRONG OUTPUT.
"""
""" The time complexity is: O(logn) where n is the value of the input variable. and the number of digit in n is logn to the base 10
space complexity is O(1) as there is no additional variable.
"""

# Approach 2: where i have used the Mathematical division
# num = int(input("Enter a number: "))
# i = 0
# count = 0
# while i < num:
#     count += 1
#     num //= 10
#
# print(count)

"""This is also same as the above approach. as it has same approach, time and space complexity. the only difference is that we have used a mathematical division '//' which helps convert the number divided into int directly. so here we dont have to convert the float number into int."""

#Approach 3: using the log10 which is the most optimal approach:
# import math
# num = int(input("Enter a number: "))
# count = int(math.log10(num))+1
# print(count)

"""This is the most optimal approach where we have used the logarithmic function. Hence the time complexity is O(1) and the space complexity is O(1).
So how does the log10() function work: the number can be written as 10^k−1≤num<10^k that is TO WHAT POWER MUST 10 BE RAISED TO GET NUM.
For example we have a number 1000. log10(1000) = 3. that is 10 should to raised to 3 to get the number.
Using this i have written a code where we have num = 12345. thus we get answer in 4.091 thus we converted into int to get 4 then we incremented it by 1 to get '5'
"""

#Approach 4: Using String Conversion
# num = input("Enter a number: ")
# print(len(num))

"""this is the most simple method where we have used the inbuild len function of the python. here we have taken the input as the string.
then we have used the len function to count the number of character in the string."""

