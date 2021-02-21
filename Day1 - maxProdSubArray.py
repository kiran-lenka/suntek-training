#Solved using Dynamic Programming Approach

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        retVal = max(nums)
        currMax =1
        currMin = 1
        for i in nums:
            tempMax = currMax
            currMax = max(currMax*i, currMin*i, i)
            currMin = min(currMin*i, tempMax*i, i)
            retVal = max(retVal, currMax)
        return retVal
