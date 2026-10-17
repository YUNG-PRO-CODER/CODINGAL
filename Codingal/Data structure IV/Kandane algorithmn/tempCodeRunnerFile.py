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