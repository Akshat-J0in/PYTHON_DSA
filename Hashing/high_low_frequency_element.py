#problem statement:
"""Given an array of size N. Find the highest and the lowest frequency element in the array.
for example:
input: {10,5,10,15,10,5}
output: 10,15"""



# Approach 1
# from collections import Counter
# arr = list(map(int, input().split()))
# freq = Counter(arr)
# for key, value in freq.items():
#     print(f"{key} -> {value}", end=", ")
# print()
# max_val,max_count = max(freq.items(), key = lambda x:x[1])
# max_val,max_count = freq.most_common(1)[0]
# print(f"The highest frequency element is {max_val}")
#
# min_val, min_count = min(freq.items(),key = lambda x:x[1])
# print(f"The lowest frequency element is {min_val}")
"""Here first i have created the hash map similar to the previous code(count frequency)
Then i have created two variable max_count and val and used the max() function.
inside the max function, we have two parameter, first is the iterable part that is the freq.items[10->3,5->2,15->1] part and the other is optional part that is the lambda function.
but here in this code it is important to mention how do we need to find the max element hence its important.
in the optional part, i have created a variable key which will store all the values that the function lambda iterate. in function lambda we have specified what element we want that is the key(3,2,1) and we will find the max element based on this.
if not this then there is another method to find the max element, we can use the .most_common() function.
Here in the most_common() we have mentioned 1 that is we want only the top 1 most common element.
the output that we get with this is [(10,3)] hence we use the [0] after the most_common(1).
for the min element i have done the same as max element."""



# Approach 2:
# from collections import Counter
# arr = list(map(int, input().split()))
# freq = Counter(arr)
# for key, value in freq.items():
#     print(f"{key} -> {value}", end=", ")
# print()
# max_ele = max(freq, key=freq.get)
# min_ele = min(freq, key=freq.get)
# print(f"The highest frequency element is {max_ele}")
# print(f"The lowest frequency element is {min_ele}")
"""Here we have created the hash map similar to the previous code(count frequency)
here i have taken the max element using the max function.
Inside the max function, the iterable part is the freq that is (10,5,15) and how do we want to iterate it is by freq.get method.
Here .get works the same way as that of lambda function that we had seen above.
it is more clean and more understandable code then the above."""



# Approach 3:
from collections import Counter
arr = list(map(int, input().split()))
freq = Counter(arr)
for key, value in freq.items():
    print(f"{key} -> {value}", end=", ")
print()

max_count = max(freq.values())
min_count = min(freq.values())

max_val = [k for k,v in freq.items() if v == max_count]
min_val = [k for k,v in freq.items() if v == min_count]

print("Highest frequency elements:", max_val, "->", max_count)
print("Lowest frequency elements:", min_val, "->", min_count)
"""This is the most optimal approach so far this can handle a case were if we have 2 similar element with same frequency.
Here i have first taken the maximum and the minimum value corresponding to their key that is(3,1)
Now we find the max value by running a for loop that will iterate freq.items() and inside the loop, we have a if condition.
That if condition will check if v == max_count that is if value is equal to what we found earlier in this code.
if v==max_count then we include that value in the list.
we did the similar thing for the min element."""