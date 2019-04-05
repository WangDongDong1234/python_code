import itertools


def per(n):
    lis = [i for i in range(n)]
    res = []
    for r in itertools.permutations(lis, n):
        res.append(r)
    return res


def f(m, n):
    res = per(n)
    s = []
    for r in res:
        c = 0
        for i in range(n):
            c += m[i][r[i]]
        s.append(c)
    min_v = min(s)
    result = []
    for i in range(len(s)):
        if min_v == s[i]:
            result.append(list(map(lambda x: x + 1, res[i])))

    return result


def g(n):
    s = ''
    for i in range(n):
        s += 'x[' + str(i) + ']' + ','
    return s[:len(s) - 1]


cases = int(input())
for _ in range(cases):
    n = int(input())
    m = [[0 for _ in range(n)] for _ in range(n)]
    nn = input().strip().split(',')
    for p in nn:
        people, task, value = p.split()
        m[int(people) - 1][int(task) - 1] = int(value)
    res = f(m, n)
    res = sorted(res, key=lambda x: (eval(g(n))), reverse=True)
    s = ''
    for r in res:
        s += ' '.join(list(map(str, r))) + ','
    print(s[:len(s) - 1])
