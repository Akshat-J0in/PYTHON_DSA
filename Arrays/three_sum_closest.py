

def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            # Update closest
            if abs(target - curr_sum) < abs(target - closest):
                closest = curr_sum

            # Move pointers
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return curr_sum  # exact match

    return closest

arr = [-1,2,1,-4]
target = 1
print(threeSumClosest(arr, target))