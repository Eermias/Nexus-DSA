class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names) 

        for i in range(1, n):
            index = i
            
            while index > 0 and heights[index] > heights[index - 1]:
                heights[index], heights[index - 1] = heights[index - 1], heights[index]
                names[index], names[index - 1] = names[index - 1], names[index]
                index -= 1
        
        return names


            