class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()

    def get_nodenum(self):
        return len(self.maps)

    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0:
                    count += 1
        return count

    def insert_node(self):
        for i in range(len(self.maps)):
            self.maps[i].append(-1)
        self.maps.append([-1] * (self.nodenum) + [0])
        self.nodenum += 1

    def insert_edge(self, x, y, weight):
        if x < 0 or x >= self.nodenum or y < 0 or y > self.nodenum or weight <= 0 or x == y:
            return
        else:
            self.maps[x][y] = self.maps[y][x] = weight
            self.edgenum += 1

    def breath_first_search(self):
        queue = []
        visited = [False] * self.nodenum
        res = []

        def bfs():
            while len(queue) > 0:
                i = queue.pop(0)
                for j in range(self.nodenum):
                    if self.maps[i][j] > 0 and visited[j] == False:
                        res.append(j)
                        visited[j] = True
                        queue.append(j)

        if self.nodenum <= 0:
            return res
        else:
            queue.append(0)  # index, value
            visited[0] = True
            res.append(0)
            bfs()

        for i in range(self.nodenum):
            if visited[i] == False:
                res.append(i)
                visited[i] = True
                queue.append(i)
                bfs()

        return res

    def depth_first_search(self,startNode):
        res = []
        visited = [False] * self.nodenum

        def dfs(i):
            res.append(i)
            global depth
            depth=depth+1
            visited[i] = True
            for j in range(self.nodenum):
                if self.maps[i][j] > 0 and visited[j] == False:
                    dfs(j)
            global maxdepth
            global isStartNode
            if self.maps[startNode][i] > 0:
                if depth > maxdepth:
                    maxdepth = depth
                depth = 1

        if self.nodenum > 0:
            dfs(startNode)
        for i in range(self.nodenum):
            if visited[i] == False:
                isStartNode=0
                dfs(i)
        # return res
        return maxdepth

depth=0
maxdepth=0
isStartNode=1
caseNum=int(input())
for i in range(caseNum):
    maxdepth=0
    depth=0
    str1=input().split()
    nodeNum=int(str1[0])
    firstNode=str1[1]
    nodes=input().split()
    for j in range(nodeNum):
        if nodes[j]==firstNode:
            startNode=j
    maps=[]#maps为邻接矩阵
    for j in range(nodeNum):
        temp=input().split()
        list1=list(map(int,temp[1:nodeNum+1]))#截取索引为1到nodeNum的字符
        maps.append(list1)
    graph = Graph(maps)

    print(graph.depth_first_search(startNode))
