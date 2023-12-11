class Solution:
    	def lengthOfLongestSubstring(self, s: str) -> int:
        seenChar = {}
        left = 0
        right = 0
        longest = 0
        n = len(s)

        while(left<n and right<n):
          currentChar = s[right]

          if(currentChar in seenChar):
            left = max(left, seenChar[currentChar]+1) 
                #seenChar[currentChar] = position/index
                #map[key] = value
                #key = char
                #value = position/index

          seenChar[currentChar] = right
          longest = max(longest,right-left+1)

          right+=1
        return longest