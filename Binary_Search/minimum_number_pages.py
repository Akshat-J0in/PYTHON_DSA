# Problem Statement:
"""Given an array 'arr of integers number, 'arr[i]' represents the number of pages in the 'i-th' book.
There are 'm' number of students, and the task is to allocate all the books to the students.
You have to allocate the books to 'm' students such that the maximum number of pages assigned to a student is minimum.
If the allocation of the books is not possible then return -1
"""



def countStudents(arr,pages):
    n = len(arr)
    total_pages = 0
    students = 1
    for i in range(n):
        if total_pages + arr[i] <= pages:
            total_pages += arr[i]
        else:
            students += 1
            total_pages = arr[i]
    return students

def findPages(arr, n, m):
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)

    while low <= high:

        mid = (low+high)//2

        students = countStudents(arr,mid)

        if students > m:
            low = mid + 1
        else:
            high = mid-1
    return low

arr = [25,46,28,49,24]
m = 4
n = 4
ans = findPages(arr,n,m)
print(ans)