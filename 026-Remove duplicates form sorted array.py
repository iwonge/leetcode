'''
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        else:
            if nums[0]==nums[-1]:
                return 1
            else:
                global i
                i=0
                for j in range(1,len(nums)):
                    if nums[j]>nums[i]:
                        i=i+1
                        nums[i]=nums[j]
                return i+1

'''
    AC sulotion:
        nums[:] = sorted(list(set(nums)))
        return len(set(nums))
'''
