from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        smallest = len(nums) + 1
        current = 0

        for right in range(0, len(nums)):
            # if smallest > 0 and right - left >= smallest:
            #     #move to the left
            #     current -= nums[left]
                
            current += nums[right]
            while(current >= target and left <= right):
                smallest = min(smallest, right - left + 1)
                if smallest == 1:
                    return 1
                current -= nums[left]
                left += 1
        return 0 if smallest > len(nums) else smallest
    


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))




