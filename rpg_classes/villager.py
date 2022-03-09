class Villager:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True

    def check_health(self, target):
        if self.health - target <= 0:
            self.health = 0
            self.is_alive = False
        else:
            self.health -= target

    def normal_attack(self, target: "Villager"):
        if target.health == 0:
            return f"{target.name} ja esta morto!!"

        if self.attack - target.defense > 0:
            target.health = self.attack - target.defense

        if target.health > 0:
            return f"{target.name} ficou com {target.health} de vida"

        return f"{target.name} morreu !!"