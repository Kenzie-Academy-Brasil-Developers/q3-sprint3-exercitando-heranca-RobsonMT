from rpg_classes.villager import Villager


class Mage(Villager):
    def __init__(self, name):
        super().__init__(name)
        self.attack = 10
        self.mana = 100

    def fire_ball(self, target: "Villager"):
        manacost = 25
        damage = 30

        if not target.is_alive:
            return f"{target.name} ja esta morto!!"

        if self.mana < manacost:
            return "Mana insuficiente"

        dmg = damage - target.defense

        if dmg > 0:
            self.mana -= manacost
            target.check_health(dmg)

        if target.health > 0:
            return f"{target.name} ficou com {target.health} de vida"

        return f"{target.name} morreu !!"