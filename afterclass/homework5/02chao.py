from sys import stdin
from time import time
from random import randint

from collections import namedtuple
from operator import itemgetter
from pprint import pformat

class Node:
    def __init__(self,_sa,_loc,_lc,_rc,_p):
        self.splitAttribute = _sa
        self.location = _loc
        self.left_child = _lc
        self.right_child = _rc
        self.parent = _p
        return
    def isLeft(self):
        if self.parent.left_child == self:
            return  True
        else:
            return  False
    def isRight(self):
        if self.parent.right_child == self:
            return True
        else:
            return False
    def isRoot(self):
        if self.parent == None:
            return True
        else:
            return False
    def neghbor(self):
        if self.isRight() == True:
            return  self.parent.left_child
        elif self.isLeft() == True:
            return  self.parent.right_child
        else:
            return None

def KDTree(point_list,depth=0):
    try:
        k = len(point_list[0])
    except IndexError as e:
        return  None
    axis = depth%k

    point_list.sort(key = itemgetter(axis))
    median = len(point_list) //2
    _left_child = KDTree(point_list[:median], depth + 1)
    _right_child = KDTree(point_list[median + 1:], depth + 1)
    node = Node(axis, point_list[median], _left_child, _right_child,None)
    if node.left_child != None:
        node.left_child.parent = node
    if node.right_child != None:
        node.right_child.parent = node
    return node


def distancePoint(pointA,pointB):
    if len(pointA) != len(pointB):
        return  -1
    d = len(pointA)
    count = 0
    for i in range(d):
        count += (pointA[i]-pointB[i])**2
    return  count**0.5

def searchKDTree(node,point):
    result = []
    if len(node.location) != len(point):
        return None
    axis = node.splitAttribute
    value = point[axis]
    nodeT = node
    while nodeT != None:
        if value <= node.location[axis]:
            node = nodeT
            nodeT = node.left_child
        else:
            node = nodeT
            nodeT = node.right_child

    #back
    curPoint = node
    curDis = distancePoint(curPoint.location,point)
    nodeT = node
    while node.isRoot() != True:
        if node.neghbor() != None:
            dis = distancePoint(point,node.neghbor().location)
            if dis<curDis:

                curPoint = node.neghbor()
                curDis = dis
        if node.isRoot() != True:
            dis = distancePoint(point,node.parent.location)
            if dis<curDis:
                curPoint = node.parent
                curDis = dis
        node = node.parent
    return curPoint

class Solution:
    def __init__(self,k):
        self.k = k
        self.knears ={}
        self.pointlist = []

    def search_k_nearest(self,node,aim):
        # 搜索树：输出目标点的近邻点
        # global pointlist  # 存储排序后的k近邻点和对应距离
        if node is None: return
        col = node.splitAttribute
        if aim[col] > node.location[col]:
            self.search_k_nearest(node.right_child, aim)
        if aim[col] < node.location[col]:
            self.search_k_nearest(node.left_child, aim)
        dis = distancePoint(node.location, aim)
        # print(self.knears,self.k)
        if len(self.knears) < self.k:
            self.knears.setdefault(node.location, dis)  # 列表不能作为字典的键
            self.pointlist = sorted(self.knears.items(), key=lambda item: item[1], reverse=True)

        elif dis <= self.pointlist[0][1]:
            self.knears.setdefault(node.location, dis)
            self.pointlist = sorted(self.knears.items(), key=lambda item: item[1], reverse=True)
        # print(self.pointlist)
        if node.right_child is not None or node.left_child is not None:

            # if abs(aim[node.splitAttribute] - node.location[node.splitAttribute]) < self.pointlist[0][1]:
                # if aim[node.splitAttribute] < node.location[node.splitAttribute]:
                #     self.search_k_nearest(node .right_child, aim)
                # if aim[node.splitAttribute] > node.location[node.splitAttribute]:
                #     self.search_k_nearest(node.left_child, aim)
            self.search_k_nearest(node.right_child, aim)
            self.search_k_nearest(node.left_child, aim)
        # print(self.pointlist)
        return self.pointlist

def transform( c ):
    if '.' not in c:
        return int(c)
    else:
        return float(c)

def main():
    test_case = int(stdin.readline())
    for index in range(test_case):
        point_list = []
        str_arr = stdin.readline().split(",")
        str_aim = stdin.readline().split()
        k = int(stdin.readline())
        for str_points in str_arr:
            str_point = str_points.split()
            x = transform(str_point[0])
            y = transform(str_point[1])
            point_list.append((x,y))
        # print(point_list)
        tree = KDTree(point_list)
        test_point =(transform(str_aim[0]),transform(str_aim[1]))
        S = Solution(k)
        pointlist = S.search_k_nearest(tree, test_point)
        # print(pointlist)
        tmpList = []
        for i in range(k):
            tmpList.append(pointlist[len(pointlist)-i-1][0])
        print(",".join(str(test[0]) + " " + str(test[1]) for test in tmpList))

if __name__ == '__main__':
    main()
"""
1
3 5,6 2,5 8,9 3,8 6,1 1,2 9
8.2 4.6
"""