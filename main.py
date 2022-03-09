from rpg_classes.mage import Mage
from rpg_classes.villager import Villager


if __name__ == "__main__":
    villager = Villager("Villager")
    mage = Mage("Mage")

    """
    A linha abaixo deve printar:
    {'name': 'Villager', 'health': 50, 'defense': 0, 'attack': 0, 'is_alive': True}
    """
    print(villager.__dict__)

    """
    A linha abaixo deve printar:
    {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 100}
    """
    print(mage.__dict__)

    battle_result = mage.fire_ball(villager)

    # Deve printar: Villager ficou com 20 de vida
    print(battle_result)

    # Deve printar: True
    print(villager.is_alive)

    # Deve printar: 75
    print(mage.mana)

    battle_result = mage.fire_ball(villager)

    # Deve printar: Villager morreu !!
    print(battle_result)

    # Deve printar: False
    print(villager.is_alive)

    # Deve printar: 50
    print(mage.mana)

    battle_result = mage.fire_ball(villager)

    # Deve printar: Villager ja esta morto!!
    print(battle_result)

    # Deve printar: 50
    print(mage.mana)
