class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxlongest = 0

        used = {}

        left = 0

        for right, char in enumerate(s):

            if char in used and used[char] >= left:
                left = used[char] + 1  
            maxlongest = max(maxlongest, right - left + 1)         
            used[char] = right          

        return maxlongest