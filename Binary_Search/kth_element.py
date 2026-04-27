# Problem Statement:
"""Given 2 sorted array a and b of size m and n respectively. Find the kth element of the final sorted array.
Example:
a = [2,3,6,7,9], b = [1,4,8,10], k = 5
Output: 6
"""


def kthElement(a, b, k):
    m, n = len(a), len(b)

    # Ensure a is smaller
    if m > n:
        return kthElement(b, a, k)

    low = max(0, k - n)
    high = min(k, m)

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1

        l1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else b[cut2 - 1]
        r1 = float('inf') if cut1 == m else a[cut1]
        r2 = float('inf') if cut2 == n else b[cut2]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)

        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
arr1 = [2,3,6,7,9]
arr2 = [1,4,8,10]
k = 5
print(kthElement(arr1,arr2,k))