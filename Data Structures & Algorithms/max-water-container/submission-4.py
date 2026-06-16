
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = min(heights[start], heights[end]) * (end - start)

        while(end - start > 1):
            nstart = start + 1
            nend = end - 1
            if(heights[start] > heights[end]):
                end = nend
                max_area = max(max_area, min(heights[start], heights[end]) * (end - start))
            else:
                start = nstart
                max_area = max(max_area, min(heights[start], heights[end]) * (end - start))

        return max_area