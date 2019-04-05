"""
分治法解最近对问题
1
1 1,2 2,3 3,4 4,5 5,1.5 1.5
0 1,3 2,4 3,5 1,1 2,2 1,6 2,7 2,8 3,4 5,9 0,6 4
"""
import math
n=int(input())
nodes_str=input().strip()
nodes=[item for item in nodes_str.split(',') ]
new_nodes=[]
for item in nodes:
    item_xy=item.strip().split(' ')
    item_x=float(item_xy[0])
    item_y=float(item_xy[1])
    new_nodes.append((item_x,item_y))
new_nodes.sort(key=lambda item:item[0])

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))



def closest(nodes,low,hight):
    if hight-low==2:
        return distance(nodes[low][0],nodes[low][1],nodes[hight-1][0],nodes[hight-1][1])
    if hight-low==3:
        d1=distance(nodes[low][0],nodes[low][1],nodes[low+1][0],nodes[low+1][1])
        d2=distance(nodes[low][0],nodes[low][1],nodes[hight-1][0],nodes[hight-1][1])
        d3=distance(nodes[hight-1][0], nodes[hight-1][1], nodes[low+1][0], nodes[low+1][1])
        return min(d1,d2,d3)
    mid=int((low+hight)/2)
    mx=nodes[mid][0]
    my=nodes[mid][1]
    dl=closest(nodes,low,mid)
    dr=closest(nodes,mid,hight)
    d_min=min(dl,dr)
    left=nodes[low:mid]
    right=nodes[mid:hight]
    #存放左右两侧ke能小于的两个点
    min_node=[]
    for ei in left:
        if mx-ei[0]<=d_min:
            for ej in right:
                if abs(ej[0]-mx)<=d_min and abs(ej[1]-my)<=d_min:
                    min_node.append([ei,ej])
    if len(min_node)>0:
        min_node_dist=[]
        for e in min_node:
            node1=e[0]
            node2=e[1]
            #dist=math.sqrt((node1[0]-node2[0])*(node1[0]-node2[0])+(node1[1]-node2[1])*(node1[1]-node2[1]))
            dist=distance(node1[0],node1[1],node2[0],node2[1])
            min_node_dist.append([e,dist])
        min_node_dist.sort(key=lambda e:e[1])
        tmp=min_node_dist[0][1]
        if d_min>tmp:
            d_min=tmp
    return d_min
d=closest(new_nodes,0,len(new_nodes))
print(d)





