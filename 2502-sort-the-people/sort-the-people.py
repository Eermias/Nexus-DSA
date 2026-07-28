class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names) 

        count = [0 for i in range(10**5 + 1)] 
        for h in heights:
            count[h] += 1
        
        mapp = {heights[i]:names[i] for i in range(n)}
        result = []
        for i in range(10**5 + 1):
            if count[i] == 1:
                result.append(mapp[i])
        
        return result[::-1]


        # for i in range(1, n):
        #     index = i
            
        #     while index > 0 and heights[index] > heights[index - 1]:
        #         heights[index], heights[index - 1] = heights[index - 1], heights[index]
        #         names[index], names[index - 1] = names[index - 1], names[index]
        #         index -= 1
        
        # return names


            