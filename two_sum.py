# Given an array of integers and an integer target return indices of 2 numbers in the array that add up to the target number
# for example,   
# 	Target = 15
# 	Arr: 3 6 12 14
# 	Indices : 0, 2
# Keys: element
# Values: index
# x + y = target
# y = current number
# x = target - y
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    m = {}
    n = len(nums)

    for i in range(0, n):
      goal = target - nums[i]

      if(goal in m):
        return [m[goal], i]
            # m은 map object이고
            # m[key] = value
            # `key in m` 이 key가 map에 있는지 확인 가능
    m[nums[i]] = i
    # 새로운 key 셋 해주기