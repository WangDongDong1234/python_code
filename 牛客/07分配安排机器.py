"""
小Q的公司最近接到m个任务, 第i个任务需要xi的时间去完成, 难度等级为yi。
小Q拥有n台机器, 每台机器最长工作时间zi, 机器等级wi。
对于一个任务,它只能交由一台机器来完成, 如果安排给它的机器的最长工作时间小于任务需要的时间, 则不能完成,如果完成这个任务将获得200 * xi + 3 * yi收益。

对于一台机器,它一天只能完成一个任务, 如果它的机器等级小于安排给它的任务难度等级, 则不能完成。

小Q想在今天尽可能的去完成任务, 即完成的任务数量最大。如果有多种安排方案,小Q还想找到收益最大的那个方案。小Q需要你来帮助他计算一下。


输入描述:
"""
jiqi_renwu_str=input().strip()
jiqi_renwu=[int(item) for item in jiqi_renwu_str.split(' ')]
jiqi=jiqi_renwu[0]
renwu=jiqi_renwu[1]
jiqi_array=[]
for i in range(jiqi):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(' ')]#第一个是时长，第二个是等级
    jiqi_array.append(tmp)
renwu_array=[]
re
for j in range(renwu):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(' ')]#第一个是任务时长，第二个是等级
    renwu_array.append(tmp)
#任务先按等级排序，在按时长排序
renwu_array.sort(key=lambda item:item[1])
renwu_array.sort(key=lambda item:item[0])
book=True
while len(renwu_array)>0 and book:

