class Solution:
  def getLeftPosition(self, nums, target):
    left = 0
    right = len(nums)-1

    # loop while left is <= right
    while(left <= right):
      # find mid posisition
      mid = left+(right-left)//2

      # first condition: when current mid element is a target
      if(nums[mid] == target):
        # two condition to set mid
        # check if current element is starting target by 
        #	1.checking one before element is not target and that is >= 0
        #	2. current position is 0, which has to be starting index
        if( (nums[mid-1] != target and mid-1 >= 0) or mid == 0 ):
          return mid

        # another loop starting by setting right = mid-1
        right = mid-1
      # second condition: when current mid element greater than target
      elif(nums[mid] > target):
        # another loop starting by setting right = mid-1
        right = mid-1
      else:
        # another loop starting by setting left = mid+1
        left = mid+1
    return -1

  def getRightPosition(self, nums, target):
    left = 0
    right = len(nums)-1

    while(left <= right):
      mid = left+(right-left)//2
      if(nums[mid] == target):
        if(mid+1 < len(nums) and nums[mid+1] != target or mid == len(nums)-1):
          return mid
        left = mid+1
      elif(nums[mid] > target):
        right = mid-1
      else:
        left = mid+1
    return -1

  def searchRange(self, nums: List[int], target: int) -> List[int]:
    left = self.getLeftPosition(nums, target)
    right = self.getRightPosition(nums, target)

    return [left, right]