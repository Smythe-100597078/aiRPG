from random import randint
import itertools
import copy

actions = {
    'attack',
    'heal',
    'damageBoost',
    }



class goapInteraction():
    def __init__(self,grid):
        self.grid = grid
        self.hero = self.grid.hero
        self.enemy = self.grid.enemy
        


    def update(self,action,attacker,defender):
        if action == 'attack':
            defender.setHP(defender.getHP() - attacker.getDamage())
        if action == 'heal': 
            attacker.setHP(attacker.getHP() + attacker.getHeal())
        if action == 'damageBoost':
            attacker.setDamage(attacker.getDamage()+attacker.damageBoost)
      


    def lookAhead(self,plan):
        copyPlayer = copy.deepcopy(self.hero)
        copyEnemy = copy.deepcopy(self.enemy)
       
        for p in plan:
            self.update(p, copyPlayer, copyEnemy)
            self.update('attack', copyEnemy, copyPlayer)
            if copyPlayer.getHP() <= 0 and copyEnemy.getHP() <= 0:
                return copyPlayer, copyEnemy
        return copyPlayer, copyEnemy

    def generate_possible_plans(self,depth):
        return list(itertools.product(actions, repeat=depth)) ## Equivilant to a nested for-loop, returns every possible action combination

    def call_best_move_player(self):
        plannedActions = self.generate_possible_plans(3) ## Repeat 3 times
       
        bestOption = None
        for p in plannedActions:
            if not bestOption:
                tempPlayer, tempEnemy = self.lookAhead(p)
                if tempPlayer.getHP() > 0:
                    bestOption = p
                continue
            tempPlayer, tempEnemy = self.lookAhead(p)
            playerTemp, enemyTemp = self.lookAhead(bestOption)
            if tempPlayer.getHP() > -5 and tempEnemy.getHP() < enemyTemp.getHP():
                bestOption = p
        print('>> Heroes best plan: ', bestOption)
        print(">> Hero chooses to do: "+str(bestOption[0]))
        return bestOption[0]

    def genereate_uninformed_enemy_move(self):
        action = ''
        if randint(1, 6) == 2:
            action = 'heal'
        elif randint(1,6) == 4:
            action = 'damageBoost'
        else:
            action = 'attack'
        print(">> Foe chooses to ", action)
        return action

    def run_game(self):
        HR = '-'*50
    
        print(">> The Hero and a Foe has entered a battle!")
        print(HR)
        running = True
        while running:
            print(">> Hero: "+"HP: "+str(self.hero.getHP())+" Damage: "+str(self.hero.getDamage())+" Heal: "+str(self.hero.getHeal())+" ")
            print(">> Foe: "+"HP: "+str(self.enemy.getHP())+" Damage: "+str(self.enemy.getDamage())+" Heal: "+str(self.enemy.getHeal())+" ")

          
            self.update(self.call_best_move_player(), self.hero, self.enemy)
            self.update(self.genereate_uninformed_enemy_move(), self.enemy, self.hero)
            

            if self.hero.getHP() <= 0 or self.enemy.getHP() <= 0:
                running = False
                print('>> The battle has ended.')
                if self.hero.hp <= 0:
                    self.hero.alive = False
                    
                    print(">> The foe has slain the hero!")
                else:
                    self.enemy.alive = False
                 
                    print(">> The foe has been slain!")
