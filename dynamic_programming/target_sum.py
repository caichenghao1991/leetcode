# 494. Target Sum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dic = {}
        #
        # def dfs(curr, nums):
        #     if not nums:
        #         return 1 if curr == target else 0
        #     if (curr, tuple(nums)) in dic:
        #         return dic[(curr, tuple(nums))]
        #     dic[(curr, tuple(nums))] = dfs(curr + nums[0], nums[1:]) + dfs(curr - nums[0], nums[1:])
        #     return dic[(curr, tuple(nums))]
        #
        # return dfs(0, nums)
        #

        # s = sum(nums)
        # if target > s or target < -s:
        #     return 0
        # till, l = 2 * s + 1, len(nums)
        #
        # dp = [[0] * till for _ in range(l)]
        # dp[0][s + nums[0]] += 1
        # dp[0][s - nums[0]] += 1
        #
        # for i in range(1, l):
        #     for j in range(till):
        #         if j - nums[i] >= 0:
        #             dp[i][j] += dp[i - 1][j - nums[i]]
        #         if j + nums[i] < till:
        #             dp[i][j] += dp[i - 1][j + nums[i]]
        #
        # return dp[l - 1][target + s]
        #

        # sumValue = sum(nums)
        # if abs(target) > sumValue or (sumValue + target) % 2 == 1: return 0
        # bagSize, l = (sumValue + target) // 2, len(nums)
        # dp = [[0] * (bagSize + 1) for _ in range(l)]
        # if nums[0] < bagSize + 1:
        #     dp[0][nums[0]] = 1
        # dp[0][0] += 1
        # for i in range(1, l):
        #     for j in range(bagSize + 1):
        #         if j - nums[i] >= 0:
        #             dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        #
        # return dp[l - 1][bagSize]



        sumValue = sum(nums)
        if abs(target) > sumValue or (sumValue + target) % 2 == 1: return 0
        bagSize, l = (sumValue + target) // 2, len(nums)
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(l):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[bagSize]
