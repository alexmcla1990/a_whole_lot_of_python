
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res



















#class Solution:
 #   def lengthOfLongestSubstring(self, s: str) -> int:
    #    if s == "":
    #        return 0

#start = 0
#end = 0
#maxLength = 0
#unique_characters = set()

  #      while end < len(s):
    #        if s[end] not in unique_characters:
     #           unique_characters.add(s[end])
       #         end =+ 1
       #         maxLength = max(maxLength, len(unique_characters))
        #    else:
          #      unique_characters.remove(s[start])
          #      start =+ 1
           # return maxLength