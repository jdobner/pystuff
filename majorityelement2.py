
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        min_count = len(nums) / 3
        nums.sort()
        current = None
        count = 0
        results = []
        added = False
        for n in nums:
            if n != current:
                current = n
                count = 1
                added = False
            else: 
                count += 1
            if (not added) & (count > min_count):
                results.append(n)
                added = True
        return results
    
if __name__ == '__main__':
    print(Solution().majorityElement([1]))