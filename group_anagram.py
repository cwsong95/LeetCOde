# Given an array of strings, group anagrams together
# example: [“eat”, “tea”, “tan”, “ate”, “nat”, “bat”]
# output:
# [
#	[“ate”, “eat”, “tea”],
#	[“nat”, “tan”],
#	[“bat”]
# ]
# Time Complexity : O(N * M * Log(M))
#	N : length of the input array
#	M : length of biggest string in the array 
#	M * Log(M) is due to the fact that we sort each string when we pass over it in the loop
class Solution:
  def findHash(self, s):
    return ‘’.join(sorted(s))

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    answer = []
    m = {}

    for s in strs:
      hashed = self.findHash(s)
      if (hashed not in m):
        m[hashed] = []
      m[hashed].append(s)

    for p in m.values():
      answers.append(p)

    return answers