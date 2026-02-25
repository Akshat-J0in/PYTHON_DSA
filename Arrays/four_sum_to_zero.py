# Problem Statement:
"""Given an array of integers, your task is to find the unique quads that add up to a specific sum.
For example:
arr[] = [1,0,-1,0,-2,2]
output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""


arr = [1,0,-1,0,-2,2]
arr.sort()
result = []
target = 0

for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:
        continue
    for j in range(i+1, len(arr)):
        if j > i+1 and arr[j] == arr[j-1]:
            continue

        left = j+1
        right = len(arr)-1

        while left < right:
            total = arr[left] + arr[right] + arr[i] + arr[j]

            if total == target:
                result.append([arr[i], arr[j], arr[left], arr[right]])

                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
print(result)