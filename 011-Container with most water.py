'''
    给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
    画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

    注意：你不能倾斜容器，n 至少是2。

'''
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==2:
            return min(height[0],height[1])
        else:
            # tmp= min(height[0],height[1])
            # for i in range(len(height)-1):
            #     for j in range (i+1,len(height)):
            #         area=(j-i)*min(height[i],height[j])
            #         if area>tmp:
            #             tmp=area
            # return tmp
            left=0
            right=len(height)-1
            area=0
            while(left<right):
                area=max(area,(right-left)*min(height[left],height[right]))
                if(height[left]<height[right]):
                    left=left+1
                else:
                    right=right-1
            return area
                