class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs[0] == "":
            return ""

        for i in range(len(strs[0])):
            ch = strs[0][i]
            for word in strs:
                if len(word) <= i or word[i] != ch:
                    return strs[0][:i]

        return strs[0]      
