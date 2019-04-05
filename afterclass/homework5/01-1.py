"""
1
4
2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
"""
import copy
n=int(input())
for t in range(n):
    tasks = int(input())
    person_task_cost_str = input().strip()
    person_task_cost = {(int(item[0]), int(item[2])): int(item[4]) for item in person_task_cost_str.split(',')}
    #print(person_task_cost)

    box = [0 for i in range(tasks + 1)]
    book = [0 for i in range(tasks + 1)]
    min = 99999999
    result = []


    def dfs(current):
        if current == tasks + 1:
            tmp = box[1:]
            #print(tmp)
            cost = 0
            for i in range(1, len(box)):
                cost += person_task_cost[(i,box[i])]
            global min, result
            if min > cost:
                min = cost
                result = tmp
            return
        for i in range(1, tasks + 1):
            if book[i] == 0:
                book[i] = 1
                box[current] = i
                dfs(current + 1)
                book[i] = 0


    dfs(1)
    result.reverse()
    for i in range(len(result)):
        if i == 0:
            print(result[i], end='')
        else:
            print('', result[i], end='')
    print()