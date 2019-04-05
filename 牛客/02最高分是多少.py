"""
输入包括多组测试数据。
每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
学生ID编号从1编到N。
第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。
"""
n_m_str=input().strip()
n_m=[int(item) for item in n_m_str.split(' ')]
n=n_m[0]
m=n_m[1]
grade_str=input().strip()
grade=[int(item) for item in grade_str.split(' ')]
result=[]
for i in range(m):
    input_str=input().strip()
    input_array=[item for item in input_str.split(' ')]
    c=input_array[0]
    start=int(input_array[1])
    end=int(input_array[2])
    if start>end:
        start,end=end,start
    if c=="Q":
        result.append(max(grade[start-1:end]))
    if c=="U":
        grade[start-1]=end
for item in result:
    print(item)