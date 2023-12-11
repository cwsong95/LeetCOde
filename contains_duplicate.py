# Given an array of integers, find if the array contains any duplicates.
#	return true if any value appears at least twice in the array, otherwise it should return false
# for example,  
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    d = {}
    for num in nums:
      if(num in d):
        return True
      d[num] = 1

    return False