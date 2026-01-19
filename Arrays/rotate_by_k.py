# Problem Statement:
"""Given an array of integers, rotating array of elements by k elements either left or right.
For example:
Input: Nums = [1,2,3,4,5,6,7], k = 2,right
Output: [6,7,1,2,3,4,5]

Input: Nums = [1,2,3,4,5,6], k=2,left
Output: [3,4,5,6,1,2]"""



arr = [1,2,3,4,5,6,7]
rotate = int(input("Enter the rotation number: "))
where = input("Where do you want to rotate 'left' or 'right'?: ")
if where == 'right':
    new_arr = arr[::-1]
    rot_arr=new_arr[0:rotate]
    remain_arr = new_arr[rotate:]
    final_arr = rot_arr[::-1] + remain_arr[::-1]
    print(final_arr)

else:
    print(arr[rotate:] + arr[:rotate])

"""Here i have used the concept of slicing.
Here first i have taken the user input for the side you want to rotate and how many position you want to rotate.
then i the user wants to rotate right then first we reverse the entire array then we slice the array into 2 half.
First take array till the position we want to rotate and the second will be the remaining array.
then we reverse the both and merge them.
For the left its easy.
we divide the array into 2 parts. first we print the part from the rotation position till the end then we print the start till the rotational position.
"""