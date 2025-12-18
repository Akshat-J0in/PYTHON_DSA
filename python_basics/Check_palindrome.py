#Problem Statement:
"""Given an integer N, return true if it is a palindrome or false otherwise.
WHAT IS PALINDROME?
In simple terms: if reversing something gives the same result then its a palindrome.
for example:
we have a number 121. if we reverse it, we get the same number 121. hence its a palindrome. Not just a number if we have a word:
'Madam' and we reverse it then it will be 'Madam' hence its also a palindrome."""

#Approach:
"""Here we can use the same approach as we used in reverse a number. Lets try using that + some new ways to solve the problem. """

# approach 1:
# num = int(input("Enter a number: "))
# temp = num
# rev = ""
# while temp > 0:
#     val = temp % 10
#     rev = rev + str(val)
#     temp = temp//10
# print(f"the reverse number is: {rev}")
#
# if num == int(rev):
#     print("Its a palindrome")
# else:
#     print("not palindrome")
"""In this method, we have used a temp variable to store the number. This is done so that we can use it in the while loop and the number does not get affected by the loop during the check.
Here inside the loop, we have done exactly same this as in the reverse the number approach 1. Once we have the reversed string, we convert it into integer then use if statement to compare if the reversed number and the actual number are same or not."""


# approach 2:
# number = int(input("Enter a number: "))
# rev = int(str(number)[::-1])
# print(f"The number is {number}")
# print(f"The reversed number is {rev}")
# if number == rev:
#     print("The number is palindrome.")
# else:
#     print("The number is not palindrome.")
"""Here we have used the slice operation to find the reverse of the number. first we have converted the number into string.
then we have reversed it using [::-1] once we have the reversed string, we have converted into the integer."""


#approach 3:
# number = int(input("Enter a number: "))
# temp = number
# rev = 0
# while temp > 0:
#     rev = rev *10 + temp % 10
#     temp = temp // 10
#
# print("The number is: ", number)
# print("The reversed number is: ", rev)
#
# if number == rev:
#     print("The number is palindrome.")
# else:
#     print("The number is not palindrome.")
"""The optimal approach as we discussed in the reverse a number code. as we have not used the string datatype. Hence no extra space is used."""

#approach 4:
# digits = []
# number = int(input("Enter a number: "))
# temp = number
# while temp > 0:
#     digits.append(str(temp % 10))
#     temp = temp // 10
#
# rev = int("".join(digits))
# print("The number is: ",number)
# print("The reverse of the number is: ",rev)
# if rev == number:
#     print("The number is palindrome.")
# else:
#     print("The number is not palindrome.")

"""Here we have used the concept of list and join just like we had used it in the reverse a number."""

#Approach 5:
number = int(input("Enter a number: "))
temp = number
rev = 0
while temp > rev:
    rev = rev * 10 + temp % 10
    temp = temp // 10

if temp == rev or (temp == rev//10):
    print("the number is palindrome")

else:
    print("the number is not palindrome")
"""This is the most optimal approach to find if the number is palindrome or not. here we have used the half reverse method.
In this method, we have used a loop condition where we run it till the temp variable is greater than rev.
So if the temp becomes equal or greater than number than we have to break the loop.
For example:
we have a number 121. If we run the loop,
temp = 121   rev = 0
temp = 12    rev = 1
temp = 1     rev = 12
now here rev > temp hence we break the loop.
once we are outside the loop, we check the condition if temp is equal to rev: which is false.
or if temp is equal to rev//10 which is 1 == 12/10 which is 1 == 1 which is true.
so false or true is true hence its a palindrome."""