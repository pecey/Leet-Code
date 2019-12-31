def twoSum(nums, target):
    num_to_idx = {}
    for i in range(0, len(nums)):
        num_to_idx[nums[i]] = i

    for i in range(0, len(nums)):
        diff = target - nums[i]
        diff_index = num_to_idx.get(diff)
        if diff_index != None and diff_index != i:
            return [i, diff_index]


print(twoSum([2,7,11,15], 9))