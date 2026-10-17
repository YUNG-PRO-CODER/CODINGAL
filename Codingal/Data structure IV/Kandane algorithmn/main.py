#kadane algorithm


def maxSubArray(nums):
    max_sum = float('-inf')
    cu_sum = 0

    for m in range(len(nums)):
        cu_sum += nums[m]
        max_sum = max(max_sum, cu_sum)

        if cu_sum < 0:
            cu_sum = 0

    return max_sum

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
