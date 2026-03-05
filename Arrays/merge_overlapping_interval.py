# Problem Statement:
"""Given an array of interval where intercal[i] = [starti,endi], merge all overlapping intervals and return an array of non-overlapping intervals.
for example:
Interval = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""



arr = [[1,3],[2,6],[8,10],[15,18]]

arr.sort()

merged = []

for interval in arr:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
print(merged)
"""this is a simple one where first i have sorted the array then i have created a empty list called as merged.
then i have created a for loop where we iterate the first list that is 0 = [1,3], 1 = [2,6]
Then i have set a condition where if the interval is not in the list, and the last value of the last interval is less than the new interval's 1st element
Then we append it inside the list.
otherwise we will find the max of last element of the new interval and the interval present in the list and append it.
then we print the list.
"""