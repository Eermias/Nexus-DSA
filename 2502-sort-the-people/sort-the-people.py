class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)

        # worst case, I will have to do 'n' passes
        for i in range(n):
            # bubble sort
            swapped = False
            for j in range(n - 1):
                if heights[j] < heights[j + 1]:
                    swapped = True
                    # swap the heights
                    temp = heights[j]
                    heights[j] = heights[j + 1]
                    heights[j + 1] = temp

                    #swap the names
                    temp = names[j]
                    names[j] = names[j + 1]
                    names[j + 1] = temp
            
            if swapped == False:
                break


        return names
        

