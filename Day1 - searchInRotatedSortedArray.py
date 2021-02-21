class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' 
        #Bruteforce O(n)
        index = -1
        for i in range(len(nums)):
            if nums[i] == target:
                index = i
                break
        '''
        #Follow up for achieving O(log n)
        
        left = 0
        right = len(nums)-1
        
        while (left<right):
            midpoint = left + int((right-left)/2)
            if(nums[midpoint]>nums[right]):
                left = midpoint+1
            else:
                right = midpoint
        
        start = left
        left = 0
        right = len(nums)-1
        
        if (target>=nums[start] and target<= nums[right]):
            left = start
        else:
            right = start
            
        while (left<= right):
            midpoint = left + int((right-left)/2)
            if(nums[midpoint]==target):
                return midpoint
            elif (nums[midpoint]<target):
                left = midpoint+1
            else:
                right = midpoint-1 
        return -1
