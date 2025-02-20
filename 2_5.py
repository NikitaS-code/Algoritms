def maxthree(nums):

    nums.sort()

    maxx = max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    if maxx == nums[-1] * nums[-2] * nums[-3]:
        return nums[-1], nums[-2], nums[-3]
    else:
        return nums[0], nums[1], nums[-1]


a = input()
nums = list(map(int, a.split()))

res = maxthree(nums)

print(*res)