class Pokemon:
    def __init__(self,name,hp,ptype ): #,level,exp):
        self.name = name
        self._hp =hp
        self.ptype = ptype
        # self._level = level 
        # self.exp =exp
        
    @classmethod
    def from_dict(cls,data):
        return cls (data["name"], data["hp"],data["type"])


    
    def __str__(self):
        print(f"{self.name} : lv {self.level}")

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level <= other.level
    

    @property
    def hp(self):
        return self._hp

    @property
    def level (self):
        return self._level

    @hp.setter 
    def hp(self,new_value):
        if new_value <= 0:
            new_value=0
            self._hp = 0
            print(f"{self.name} fainted")
        self._hp = new_value

    def attack(self):
            print(f"{self.name} used flamethrower")

      
    def take_damage(self,dmg_amount):
        self.hp -= dmg_amount
        

    @level.setter
    def level(self,new_value):
        if  self.level >99 :
            self._level = 99
        self._level = new_value
            
        
    def change_level(self,level,exp):
        if exp>= 1000 :
            self.exp -= 1000
            self.level += 1
            print(f"{self.name} leveled up to {self.level}!")


class Fire(Pokemon):
    def __init (self,name,hp):
        super().__init__(name,hp,ptype ="fire")

    def attack(self):
        print(f"{self.name} used flamethrower")    

class water(Pokemon):
    def __init__(self, name, hp, ptype):
        super().__init__(name, hp, ptype = "water")


# charmander = Pokemon("charmander",80,"fire",32,11194)
# pikachu = Pokemon("pikachu",20,"electric",20,1003000000)
# pikachu.take_damage(10)
# print(pikachu.hp)

# print(pikachu < charmander) 

# team = sorted([pikachu, charmander])  # sorted() uses __lt__ automatically!

raw = {"name": "Squirtle", "hp": 44, "type": "Water"}
squirtle = Pokemon.from_dict(raw)
