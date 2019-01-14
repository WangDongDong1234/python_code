class GameRole:
    def __init__(self,name,ad,hp):
        self.name=name
        self.ad=ad
        self.hp=hp

    def attack(self,p):
        p.hp=p.hp-self.ad
        print("%s 攻击了%s,%s掉了%s,还剩%s" %(self.name,p.name,p.name,self.ad,p.hp))

p1=GameRole("亚瑟",20,500)
p2=GameRole("剑豪",50,300)
#p1.attack(p2)

class Weapon:
    def __init__(self,name,ad):
        self.name=name
        self.ad=ad
    def fight(self,p1,p2):
        p2.hp=p2.hp-self.ad
        print("%s用%s打%s,%s掉了%s血,还剩%s学" %(p1.name,self.name,p2.name,p2.name,p1.ad,p2.hp))

axe=Weapon("三板斧",2)
axe.fight(p1,p2)