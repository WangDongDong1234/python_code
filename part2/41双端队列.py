

# import queue
# #先进先出
# q=queue.Queue()
# q.put(1)
# q.put('a')
# q.put((123))
# q.put(({'k':'v'}))
# print(q)#<queue.Queue object at 0x000000F538B31E10>
# print(q.get())#1
# print(q.qsize())

from collections import deque

dq=deque()
dq.append(2)
dq.append(5)
print(dq)#deque([2, 5])
dq.appendleft('a')
dq.append('A')
print(dq)#deque(['a', 2, 5, 'A'])
print(dq.pop())#A
print(dq.popleft())#a
print(dq.remove('a'))
print(dq.insert(2,'123'))
dq.e