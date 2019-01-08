class node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class singleLinkedList:
    head=None
    size=0
    def __init__(self):
        self.head=None
        self.size=0

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
            self.size += 1
    def print_result(self,k):
        restult=[]
        p=self.head
        num=0
        re=[]
        while p!=None:
            # print(p.data)
            # p=p.next
            # self.size-=1
            re.append(p.data)
            p=p.next
            self.size-=1
            num+=1
            if num%k==0:
                restult.extend(re[::-1])
                re=[]
            if p==None:
                restult.extend(re)
        return restult
while 1:
    try:
        name=input().strip()
        list=[item for item in name.split(" ")]
        n=list[0]
        k=int(list[len(list)-1])
        array=list[1:len(list)-1]
        s=singleLinkedList()
        for item in array:
            s.add(item)
        resutl=s.print_result(k)
        print(resutl[0],end="")
        for i in range(1,len(resutl)):
            print(" "+resutl[i],end="")
        print()
    except EOFError:
        break
