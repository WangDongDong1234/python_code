"""
描述


给出一个正整数数组和许多关于可除性的查询。在每一个查询q[i]中，我们都得到一个整数k，我们需要计算数组中被k完全整除的所有元素。


约束条件：1<=t<=1001<=n，m<=1051<=a[i]，q[i]<=105


输入


输入的第一行包含一个整数t，表示测试用例的数量。接下来是T测试用例。每个测试用例由三行组成。每个测试用例的第一行包含两个整数n&m，第二行包含n个空格分隔的数组元素，第三行包含m个空格分隔的查询。


产量


对于每个测试用例，在新行中打印每个查询所需的计数q[i]。
"""


n=int(input())
last_resut=[]
for i in range(n):
    mn_array=input().strip()
    mn=[int(item) for item in mn_array.split(" ")]
    m_str=input().strip()
    m_list=[int(item) for item in m_str.split(" ")]
    n_str=input().strip()
    n_list=[int(item) for item in n_str.split(" ")]
    result=[]
    for j in range(mn[1]):
        count=0
        for t in range(mn[0]):
            if m_list[t]%n_list[j]==0:
                count+=1
        result.append(count)
    last_resut.append(result)

for item in last_resut:
    for w in range(len(item)):
        if w == 0:
            print(item[w], end="")
        else:
            print("",item[w],end="")
    print()



