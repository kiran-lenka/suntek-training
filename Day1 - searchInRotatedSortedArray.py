class Solution:

# Bruteforce O(n) 
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        for i in range(len(nums)):
            if nums[i] == target:
                index = i
                break
        return index
                
