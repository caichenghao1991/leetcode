# 84. Largest Rectangle in Histogram     need rework
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res, st = 0, [0]
        heights.insert(0, 0)
        heights.append(0)
        for i in range(1, len(heights)):
            while st and heights[i] < heights[st[-1]]:
                top = heights[st[-1]]
                st.pop()
                if st:
                    res = max(res, top * (i - st[-1] - 1))
            st.append(i)
        return res
