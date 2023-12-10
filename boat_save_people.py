class Solution:
	def numRescueBoats(self, people: List[int], limit: int) -> int: 
    people.sort()

    left = 0                  #two pointers method beginning
    right = len(people) - 1   #two pointers method end   
    boats_number = 0          #output, counter

    while(left <= right):
      if(left == right):      #edge case
        boats_number += 1
      break

      if(people[left] + people[right] <= limit): 
        boats_number += 1
        left += 1 
        right -= 1
      else:
        boats_number += 1
        right -= 1

      return boats_number