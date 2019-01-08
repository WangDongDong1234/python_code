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
while 1:

    sdl = single_linked_list()
    str=input().strip()
    if len(str)==0:
        break
    array=str.split(" ")
    list=array[1::]
    for item in list:
        sdl.add(item)
    s=sdl.print_result()
    s_tmp=s[::-1]
    if s==s_tmp:
        #print('true')
        result.append('true')
    else:
        #print('false')
        result.append('false')


for item in result:
    print(item)
