class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        max_vol = 0
        while l < r:
            h = min(height[l],height[r])
            w = abs(l-r)
            v = h*w
            if v > max_vol:
                max_vol = v
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return max_vol





        
