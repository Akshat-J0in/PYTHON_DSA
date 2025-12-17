#Here we will be given a integer N, we have to return the reverse of the number. Note: if the number is trailing by zreo, it will not be included.

"""For example:
The input is: N = 12345
the output will be: 54321
here we have reversed the number.
"""

#approach1:
# flag = False
# num = int(input("Enter a number: "))
# rev = ""
# while num > 0:
#     val = num % 10
#     if val!=0 or flag:
#         rev = rev + str(val)
#         flag = True
#     num = num // 10
# print(rev)
"""Here we have used the wile loop and the concept of strings. Where we have made an empty string 'rev' and then we have used the while loop
which will iterate till our num is greater than 0. inside the while loop we have created a variable where it will store the last number temporary.
then we will covert the val into string and then append it inside our variable rev. then print it.
IMPORTANT NOTE: HERE I HAVE ADDED A FLAG TO CHECK IF WE HAVE A TRALLING ZERO. IF YES THEN THIS IF CONDITION HELPS IGNORE THAT ZERO IN THE OUTPUT.
FOR EXAPMPLE:
The input is: N = 1200
the output will be 21"""
"""The time complexity is:O((logn)^2) because string in python are immutable so every time rev is created as a new string again and again while coping the previous character.
the space complexity will be O(logn)"""


#approach 2 - optimal:
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num //= 10
#
# print(rev)
"""This approach is much better than the first one as we are not converting any variable into string thus no extra space is taken and it is much easy to understand as there is no flag used.
here we are using a variable num which will take the number then we have created a variable rev which has initial value as 0.
we used a while loop where we iterate the loop till the num is greater than 0.
the main logic is we use the remainder of the number(num%10)and add it with the rev which is multiplied by 10 so that the number is shifted to the left.
for example:
input: 1234
now we first do 1234 % 10 = 4
0(rev) * 10 = 0
0 + 4 = 4
now rev = 4
then 123 % 10 = 3
4*10 = 40
40+3 = 43 and so on..."""
"""The time complexity for this approach is O(logn) and the space complexity is O(1)"""


#Approach 3:
# num = int(input("Enter a number: "))
# rev = int(str(num)[::-1])
# print(rev)
"""In this approach, I have used the concept of slicing the string.
How does the slice work:
if i have a string name = 'akshat' and i write name[1:3], we will get the output as the ks as the index for the string starts from 0,1,2,...
so here we have written in example[1:3] in this the last index that is 3 is not included.
if i had written [1:] this means the output will be 'kshat' if we dont mention anythin before or after the colon, we take all the charater before or after the colon.
there is one more parameter in the slicing which is step. here if we have name[::1] this means that we take all the value from start to end with step 1 that is we are not ignoring any value.
hence the output will be 'akshat'. now if we want to access the last charater then we have a method in slicing called as negative indexing.
in this we can write name[-1] this will give us the last element. if we do name[::-1] then we will get the reverse of the name that is: 'tahska' """


#Approach 4:
num = int(input("Enter a number: "))
digits = []
while num > 0:
    digits.append(str(num % 10))
    num //= 10

rev = int("".join(digits))
print(rev)

"""In this approach we have used the join and the list method. Here we have created a empty list, then we are running the while loop till our num is greater than 0.
then we are taking the remainder of the num converting it into string and then appending it into the list.
here comes the most important part that is we are using the join operation with '"' and making it into int.
so how does join help:
if not join, we had to use the first approach that is we had to use loop and every time we had to create a new string which would take more space.
and this is not in case of join operation hence it is much more optimal than the first approach."""