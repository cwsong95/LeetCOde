# Given a non-empty array of integers, every element appears twice except for one, find it
# For example, Input: [2, 2, 1, 1, 4]
# Consider this formula: 2*(a+B+c) - (a + a + b+ b + c) = c ****** MEMORIZE!!
# 2*Uniq_sum - sum = ans
# set(input_ = [2, 1, 4] 7 - 10
class Solution:
  def single(self, nums):
    return 2*sum(set(nums)) - sum(nums)