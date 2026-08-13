class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        count = defaultdict(int)
        longest = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1

            # as long as there is a reapeating character ...
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            
            # we have a valid window
            longest = max(longest, r - l + 1)
        
        return longest
            
            
        