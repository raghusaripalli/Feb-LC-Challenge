class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        
        # base case
        if l == 1:
            return 1
        
        i, j = 0, 1
        
        while i < j and j < l:
            while j < l and nums[i] == nums[j]:
                j+=1
            
            if j-1-i == 1:
                i = j
                j += 1
            elif j-1-i > 1:
                nums[:] = nums[:i+1] + nums[j-1:]
                i += 2
                j  = i + 1
                l = len(nums)
            else:
                i = j
                j += 1
        
        return len(nums)
