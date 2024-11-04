# Solution 1: Brute Force Approach (ID: 1)
def containsDuplicate1(nums: list[int]) -> bool:
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] == nums[j]):
                return True
    return False


# Solution 2: Sorting Approach (ID: 2)
def containsDuplicate2(nums: list[int]) -> bool:
    nums.sort()
    for i in range(0,len(nums)-1):
        if (nums[i] == nums[i+1]):
            return True
    return False


# Solution 3: Using List to Store (ID: 3)
def containsDuplicate3(nums: list[int]) -> bool:
    store = list()

    for num in nums:
        if num in store:
            return True
        store.append(num)
    
    return False


# Solution 4: Using Set (ID: 4)
def containsDuplicate4(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)



        