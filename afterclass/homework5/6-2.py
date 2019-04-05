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


dict={}
def closest(nodes,low,hight):
    if hight-low==2:
        length=distance(nodes[low][0],nodes[low][1],nodes[hight-1][0],nodes[hight-1][1])
        if len(dict)>0:
            tmp_key=[]
            for key in dict.keys():
                if key>length:
                    tmp_key.append(key)
            for item in tmp_key:
                del dict[item]
        if dict.get(length)==None:
            dict[length]=[(nodes[low][0],nodes[low][1]),(nodes[hight-1][0],nodes[hight-1][1])]
        else:
            dict[length].append((nodes[low][0],nodes[low][1]))
            dict[length].append((nodes[hight-1][0],nodes[hight-1][1]))
        return length
    if hight-low==3:
        d1=distance(nodes[low][0],nodes[low][1],nodes[low+1][0],nodes[low+1][1])
        d2=distance(nodes[low][0],nodes[low][1],nodes[hight-1][0],nodes[hight-1][1])
        d3=distance(nodes[hight-1][0], nodes[hight-1][1], nodes[low+1][0], nodes[low+1][1])
        m_tmp=min(d1,d2,d3)
        if m_tmp==d1:
            if len(dict) > 0:
                tmp_key=[]
                for key in dict.keys():
                    if key > m_tmp:
                        tmp_key.append(key)
                for item in tmp_key:
                    del dict[item]
            if dict.get(m_tmp)==None:
                dict[m_tmp] = [(nodes[low][0], nodes[low][1]), (nodes[low+1][0], nodes[low+1][1])]
            else:
                dict[m_tmp].append((nodes[low][0], nodes[low][1]))
                dict[m_tmp].append((nodes[low+1][0], nodes[low+1][1]))
        if m_tmp==d2:
            if len(dict) > 0:
                tmp_key = []
                for key in dict.keys():
                    if key > m_tmp:
                        tmp_key.append(key)
                for item in tmp_key:
                    del dict[item]
            if dict.get(m_tmp)==None:
                dict[m_tmp] = [(nodes[low][0], nodes[low][1]), (nodes[hight - 1][0], nodes[hight - 1][1])]
            else:
                dict[m_tmp].append((nodes[low][0], nodes[low][1]))
                dict[m_tmp].append((nodes[hight - 1][0], nodes[hight - 1][1]))
        if m_tmp==d3:
            if len(dict) > 0:
                tmp_key=[]
                for key in dict.keys():
                    if key > m_tmp:
                        tmp_key.append(key)
                for item in tmp_key:
                    del dict[item]
            if dict.get(m_tmp)==None:
                dict[m_tmp] = [(nodes[low+1][0], nodes[low+1][1]), (nodes[hight - 1][0], nodes[hight - 1][1])]
            else:
                dict[m_tmp].append((nodes[low+1][0], nodes[low+1][1]))
                dict[m_tmp].append((nodes[hight - 1][0], nodes[hight - 1][1]))
        return m_tmp
    mid=int((low+hight)/2)
    mx=nodes[mid][0]
    my=nodes[mid][1]
    dl=closest(nodes,low,mid)
    dr=closest(nodes,mid,hight)
    d_min=min(dl,dr)
    if len(dict) > 0:
        tmp_key=[]
        for key in dict.keys():
            if key > d_min:
                tmp_key.append(key)
        for item in tmp_key:
            del dict[item]
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
            if len(dict) > 0:
                tmp_key = []
                for key in dict.keys():
                    if key > d_min:
                        tmp_key.append(key)
                for item in tmp_key:
                    del dict[item]
            if dict.get(d_min)==None:
                dict[d_min] = [min_node_dist[0][0],min_node_dist[0][1]]
            else:
                dict[d_min].append(min_node_dist[0][0])
                dict[d_min].append(min_node_dist[0][1])
    return d_min
d=closest(new_nodes,0,len(new_nodes))
print(d)
print(dict)





