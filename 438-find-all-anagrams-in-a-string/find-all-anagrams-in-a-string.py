class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # if len(p) > len(s) ... invalid
        if len(p) > len(s):
            return []

        target = defaultdict(int)
        for c in p:
            target[c] += 1
        
        window = defaultdict(int)
        for i in range(len(p)):
            window[s[i]] += 1
        
        start_idx = []
        for i in range(1, len(s) - len(p) + 1):
            if window == target:
                start_idx.append(i - 1)
            
            prev = s[i - 1]
            new = s[i + len(p) - 1]
            window[prev] -= 1
            window[new] += 1

            if window[prev] == 0:
                window.pop(prev)
        
        if window == target:
            start_idx.append(len(s) - len(p))
        
        return start_idx

            

