class Solution:
	def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
		m = {}
    ans = 0
    lenA = len(nums1)
    lenB = len(nums2)
    lenC = len(nums3)
    lenD = len(nums4)

    for i in range(0, lenA):
      x = nums1[i]
      for j in range(0, lenB):
        y = nums2[j]
  
        if (x+y not in m):
          m[x+y] = 0
      
        m[x+y]+=1

    for i in range(0, lenC):
      x = nums3[i]
      for j in range(0, lenD):
        y = nums4[j]
        target = -(x+y)
  
        if (target in m):
          ans += m[target]
            
    return ans