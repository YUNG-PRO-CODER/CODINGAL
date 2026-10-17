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


#maximum circular array


def maxSubarraySumCircular(nums):
    total = 0
    cur_max = cur_min = 0
    max_sum = float('-inf')
    min_sum = float('inf')

    for n in nums:
        total += n

        cur_max = max(n, cur_max + n)
        max_sum = max(max_sum, cur_max)

        cur_min = min(n, cur_min + n)
        min_sum = min(min_sum, cur_min)

    if max_sum < 0:
        return max_sum

    return max(max_sum, total - min_sum)


print(maxSubarraySumCircular([5, -3, 5]))
