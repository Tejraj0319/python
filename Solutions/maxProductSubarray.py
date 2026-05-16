def maxProductSubarray(nums):
    max_val = nums[0]
    min_val = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_val, min_val = min_val, max_val
        max_val = max(nums[i], max_val * nums[i])
        min_val = min(nums[i], min_val * nums[i])
        result = max(result, max_val)
    return result
print(maxProductSubarray([2, -3, -3, -2, 4]))
