"""
4
2 1 3 2
3 2 4 2
5
"""
import copy
n=int(input())
w_str=input().strip()
w=[int(item) for item in w_str.split(" ")]
v_str=input().strip()
v=[int(item) for item in v_str.split(" ")]
total_w=int(input())

max_v=0

def dfs(i,sum_w,sum_v,package):
    if i==n:
        if sum_w<=total_w:
            print(package,sum_v)
            global max_v
            if sum_v>max_v:
                max_v=sum_v

        return
    package_first=copy.deepcopy(package)
    dfs(i+1,sum_w,sum_v,package_first)
    package_second=copy.deepcopy(package)
    package_second.append(i)
    dfs(i+1,sum_w+w[i],sum_v+v[i],package_second)
result=[]
dfs(0,0,0,result)
print(max_v)
