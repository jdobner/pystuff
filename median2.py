from typing import List

class Li : List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    l1 = len(nums1)
    l2 = len(nums2)
    totalLen = l1 + l2
    isOdd = totalLen % 2 != 0
    p1, p2, = 0, 0
    num = None
    for i in range(totalLen // 2):
        if nums1[p1] >= nums2[p2]:
            p1 += 1
        else:
            p2 += 1
        




    
    