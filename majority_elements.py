# Given 

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    m = {}
    for num in nums:
      m[num] = m.get(num, 0) + 1   # from dictionary m, get value of `num` key, and if that is not existed get 0

    for num in nums:
      if(m[num] > len(nums)//2):
        return num