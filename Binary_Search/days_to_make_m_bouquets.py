# Problem Statement:
"""You are given 'N’ roses and you are also given an array 'arr' where 'arr[i]' denotes that the 'ith' rose will bloom on the 'arr[i]th' day.
You can only pick already bloomed roses that are adjacent to make a bouquet.
You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet.
Find the minimum number of days required to make at least ‘m' bouquets each containing 'k' roses. Return -1 if it is not possible.
"""



def numberofbouquets(arr,days,m,k):
    bouquets = 0
    count = 0

    for value in arr:
        if value <= days:
            count += 1
            if count == k:
                bouquets += 1
                count = 0
        else:
            count = 0
    return bouquets >= m

def mindays(arr,m,k):
    low = min(arr)
    high = max(arr)
    ans = 0

    if m*k > len(arr):
        return -1

    while low <= high:
        mid = (low+high)//2

        if numberofbouquets(arr,mid,m,k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

arr = [7,7,7,7,13,11,12,7]
m = 2
k = 3
print(mindays(arr,m,k))
"""Here i have first set a condition where if the length of the array is less than the number of bouquets * number of rose, we will return -1.
Then we have set the max and min. In this, we will first find the mid then i have set a bool condition where if the number of bouquets are equal to m then we will store the mid in the ans
that is the number of days it took to make m of those and do high = mid - 1 as we want min number of days to make those bouquets.
Now in the bool condition, we have created a function where we check if the bouquet is created or not where we run a for loop and and set a counter.
If the k == counter, we make k+=1 and start from counter = 0 to see if the second k is formed or not and so on.
"""