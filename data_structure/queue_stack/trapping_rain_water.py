# 42. Trapping Rain Water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, res = 0, 0
        st = list()
        for i in range(len(height)):
            while st and height[i] >= height[st[-1]]:
                hmin = height[st.pop()]
                if st:
                    hl = st[-1]
                    res += max((min(height[i], height[hl]) - hmin) * (i - hl - 1), 0)
            st.append(i)
        return res
