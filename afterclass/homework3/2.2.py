class node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class single_linked_list:
    head=None
    size=0
    def __init__(self):
        self.size=0
        self.head=None

    def add(self,data):
        newnode=node(data,None)
        if self.size==0:
            self.head=newnode
            self.size+=1
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=newnode

    def print_result(self):
        s=""
        p=self.head
        while p!=None:
            s+=p.data
            p=p.next
        return s

result=[]
while True:
    try:
        # f = open('input.txt')
        # arr = [i for i in f.readline().strip().split(' ')]
        arr = [i for i in input().strip().split()]
        n = int(arr[0])
        sll=single_linked_list()
        for i in range(1,len(arr)):
            sll.add(arr[i])
        s=sll.print_result()
        if s==s[::-1]:
            #print('true')
            result.append('true')
        else:
            #print('false')
            result.append('false')
    except EOFError:
        break
for item in result:
    print(item)