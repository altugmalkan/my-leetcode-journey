nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
nums = [3,3,3,3,3]
#Output : 2

def findDuplicate(nums: list[int]) -> int:
    nums.sort()
    
    for i in range(len(nums)-1):
        if (nums[i] == nums[i+1]):
            return nums[i]
        
print(findDuplicate(nums))

def findDuplicate(nums: list[int]) -> int: 
    list = []
    for num in nums:
        if num in list:
            return num
        list.append(num)

print(findDuplicate(nums))

def floydCycleDetection(nums: list[int]) -> int:
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast:
            break
    return slow

print(floydCycleDetection(nums))