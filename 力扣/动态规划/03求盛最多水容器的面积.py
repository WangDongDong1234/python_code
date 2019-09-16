"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。
思路：
第二种贪心

很巧妙的一个解法，假设先选取的是两端之间的两条线段，这样这两条线段之间的距离是最大的，
长度是给定数组的长度减1。那么在这种情况下要容纳更多的水，由于宽度已经是最大的了，
只能想法提高线段的高度，这种情况下如果两端是左边比右边高，那么只有可能是将右边的指针左移，否则将左边边的指针右移，然后7回到了初始的问题，这样不断移动下去到左右指针相等为止。



"""



class Solution:
    def maxArea(self, height):
        i=0
        j=len(height)-1
        max_area=0
        while i<j:
            max_area=max(max_area,min(height[i],height[j])*(j-i))
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        return max_area

array_str=input().strip()
array=[int(item) for item in array_str.split(' ')]
s=Solution()
print(s.maxArea(array))

