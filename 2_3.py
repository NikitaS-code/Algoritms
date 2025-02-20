from collections import Counter
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = Counter(nums1)
        res = []
        for num in nums2:
            if check[num]>0:
                res.append(num)
                check[num] -= 1
        return res