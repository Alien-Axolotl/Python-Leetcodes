class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        n = len(nums)
        
        for i in range(n):
            hashmap[nums[i]] = i
       
        for i in range(n):
            difference = target - nums[i]
            if difference in hashmap and hashmap[difference] != i:
                return [i, hashmap[difference]]

<<<<<<< HEAD
        return [] # If no solution is found , return an empty list        
=======
        return [] # If no solution is found , return an empty list
>>>>>>> 24faea970d8325d393933fda630457c939d6f54a
