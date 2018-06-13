

class character(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.previousDirection = ''
        self.alive = True
        self.hp = 0
        self.damage = 0
        self.heal = 0
        self.damageBoost = 4


    def setHP(self,hpValue):
        self.hp = hpValue

    def setDamage(self,damageValue):
        self.damage = damageValue

    def setHeal(self,healValue):
        self.heal = healValue

    def getHP(self):
       return self.hp

    def getDamage(self):
       return self.damage

    def getHeal(self):
        return self.heal

       


     

