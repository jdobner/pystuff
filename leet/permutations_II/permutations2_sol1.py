from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def perm(start: int, res: List[List[int]], current: List[int]):
            if len(current) == len(nums):
                res.append(current)
                return
            
            for x in nums:
                pass
            return None
        
        rv = perm([])
        return rv
        