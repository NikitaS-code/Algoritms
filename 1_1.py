class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1+i, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j

print(Solution().twoSum([2, 7, 11, 15], 9))