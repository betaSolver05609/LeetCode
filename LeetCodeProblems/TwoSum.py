#Brute Force Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #constraints
        if len(nums)<2 or len(nums)>(10**3):
            return
        if target < -(10**9) or target >(10**9):
            return
        
        #code
        for i in range(len(nums)):
            if nums[i] < -(10**9) or nums[i] > (10**9):
                return
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
                
            
#One Pass Hash Table        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #constraints
        if len(nums)<2 or len(nums)>(10**3):
            return
        if target < -(10**9) or target >(10**9):
            return
        hashMap={}
        
        for index, value in enumerate(nums):
            if target-value in hashMap:
                return [hashMap[target-value], index]
            hashMap[value]=index
    