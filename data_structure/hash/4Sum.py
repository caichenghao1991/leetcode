# 18. 4Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        s = set()
        if len(nums) < 4:
            return res
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                m, n = j + 1, len(nums) - 1
                while m < n:
                    req = target - nums[i] - nums[j]
                    if +nums[m] + nums[n] == req:
                        if ",".join([str(v) for v in [nums[i], nums[j], nums[m], nums[n]]]) not in s:
                            res.append([nums[i], nums[j], nums[m], nums[n]])
                            s.add(",".join([str(v) for v in [nums[i], nums[j], nums[m], nums[n]]]))
                        n -= 1
                    elif nums[m] + nums[n] < req:
                        m += 1
                    else:
                        n -= 1
        return res
