'''
	给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

	不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

	元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #mine
        i=0
        while i < len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
        
'''
        res=0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[res] = nums[i]
                res+=1
        return res
'''        