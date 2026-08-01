class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        output = []
        ptr1, ptr2 = 0, 0

        while ptr1 < m and ptr2 < n:
            if nums1[ptr1] <= nums2[ptr2]:
                output.append(nums1[ptr1])
                ptr1 += 1
            else:
                output.append(nums2[ptr2])
                ptr2 += 1
        
        while ptr1 < m:
            output.append(nums1[ptr1])
            ptr1 += 1

        while ptr2 < n:
            output.append(nums2[ptr2])
            ptr2 += 1


        for i in range(n + m):
            nums1[i] = output[i]
        