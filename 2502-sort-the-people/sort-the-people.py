class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        min_index = 0
        while min_index < n:
            max_index = min_index
            for i in range(min_index, n):
                if heights[i] > heights[max_index]:
                    max_index = i
            
            heights[min_index], heights[max_index] = heights[max_index], heights[min_index]
            names[min_index], names[max_index] = names[max_index], names[min_index]
        
            min_index += 1
        
        return names

        