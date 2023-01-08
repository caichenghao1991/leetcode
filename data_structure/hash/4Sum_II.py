# 454. 4Sum II
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        res, s = 0, {}
        for i in nums3:
            for j in nums4:
                s[i + j] = 1 if (i + j) not in s else s[i + j] + 1
        for i in nums1:
            for j in nums2:
                if -(i + j) in s:
                    res += s.get(-(i + j))
        return res
