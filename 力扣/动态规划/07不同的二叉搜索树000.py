"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def generate(start,end):
    list=[]
    if start>end:
        list.append("null")
        for e in list:
            if e!="null":
                print(e.val)
            else:
                print("null")
    for i in range(start,end+1):
        l=generate(start,i-1)
        r=generate(i+1,end)
        for t in range(len(l)):
            for m in range(len(r)):
                treeNode=TreeNode(i)
                treeNode.left=TreeNode(t)
                treeNode.right=TreeNode(m)
                list.append(treeNode)
    return

def generateTrees(n):
    list=[]
    if n==0:
        return list
    else:
        return generate(1,n)
l=generateTrees(5)
for e in l:
    print(e)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:


