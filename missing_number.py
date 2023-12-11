class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    currentSum = sum(nums)
    n = len(nums)
    intendedSum = n*(n+1)/2 ****** MEMORIZE!!

    return int(intendedSum - currentSum)