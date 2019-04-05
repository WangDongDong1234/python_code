"""
1
4
2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
"""
import copy
n=int(input())

for i in range(n):
    tasks = int(input())
    person_task_cost_str = input().strip()
    person_task_cost = [(int(item[0]), int(item[2]), int(item[4])) for item in person_task_cost_str.split(',')]

    # 按成本排序
    person_task_cost.sort(key=lambda item: item[2])
    # print(person_task_cost)
    """
    [(3, 3, 1), (1, 2, 2), (2, 3, 3), (2, 2, 4), 
    (4, 4, 4), (3, 1, 5), (2, 1, 6), (4, 2, 6), 
    (1, 3, 7), (2, 4, 7), (4, 1, 7), (1, 4, 8), 
    (3, 2, 8), (3, 4, 8), (1, 1, 9), (4, 3, 9)]
    """
    book = []
    for i in range(tasks + 1):
        book.append(0)
    result = []


    def dfs(result, person_task_cost, book):
        if len(result) == 4:
            result.sort(key=lambda item: item[0])
            for i in range(len(result)):
                if i == 0:
                    print(result[i][1], end='')
                else:
                    print('', result[i][1], end='')
            print()
            return

        tmp = person_task_cost[0][2]
        same_cost = filter(lambda item: item[2] == tmp, person_task_cost)
        for item in same_cost:
            if book[item[1]] == 0:
                new_result = copy.deepcopy(result)
                new_person_task_cost = copy.deepcopy(person_task_cost)
                new_result.append(item)
                # new_person_task_cost=filter(lambda e:e[2]==item[2],new_person_task_cost)
                new_person_task_cost_tmp = []
                for e in new_person_task_cost:
                    if e[1] != item[1] and e[0] != item[0]:
                        new_person_task_cost_tmp.append(e)

                new_book = copy.deepcopy(book)
                new_book[item[1]] = 1
                dfs(new_result, new_person_task_cost_tmp, new_book)


    dfs(result, person_task_cost, book)


