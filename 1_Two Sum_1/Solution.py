def twoSum(nums: list[int], target: int) -> list[int]:
    seen = dict()

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i     

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
