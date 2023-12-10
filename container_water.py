class Solution:
	def maxArea(self, height: List[int]) -> int:
		maxarea = 0
		left = 0
		right = len(height)-1

		while(left < right):
			maxarea = max(maxarea,
										min(height[left], height[right]) * (right-left))
			# min(height[left], height[right]) = height
			# (right-left) = width

			if(height[left] < height[right]):
				left += 1
		  else:
        right -= 1

    return maxarea