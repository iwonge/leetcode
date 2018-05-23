'''

'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums:
            dic={}
            for i in range(len(nums)):
                if target-nums[i] in dic:
                    return(dic[target-nums[i]],i)
                else:
                    dic[nums[i]]=i
                    print(dic[nums[i]])
        else:
            return 0