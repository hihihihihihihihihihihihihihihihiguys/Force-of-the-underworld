class Character():
    """Warrior
Heavy armor melee fighter.

Ranger
Bow specialist with survival bonuses.

Scholar
Reads ancient languages and uses support magic.

Priest
Healing and light magic.

Shadow Mage
Uses dangerous Underworld energy.

Alchemist
Crafts potions, bombs, toxins.

Tinker
Creates mechanical devices.

Warden
Anti-monster specialist.
    """
    def __init__(self, name, class_type):
        self.name = name
        healths = {"Warrior": 150, "Ranger": 100, "Scholar": 80, "Priest": 90, "Shadow Mage": 70, "Alchemist": 85, "Tinker": 95, "Warden": 120}
        manas = {"Warrior": 30, "Ranger": 50, "Scholar": 100, "Priest": 120, "Shadow Mage": 150, "Alchemist": 80, "Tinker": 60, "Warden": 40}
        strengths = {"Warrior": 20, "Ranger": 15, "Scholar": 10, "Priest": 12, "Shadow Mage": 18, "Alchemist": 14, "Tinker": 16, "Warden": 22}
        agilities = {"Warrior": 10, "Ranger": 20, "Scholar": 12, "Priest": 14, "Shadow Mage": 16, "Alchemist": 18, "Tinker": 22, "Warden": 8}
        intellects = {"Warrior": 5, "Ranger": 10, "Scholar": 25, "Priest": 30, "Shadow Mage": 28, "Alchemist": 22, "Tinker": 20, "Warden": 12}
        if class_type in ["Warrior", "Ranger", "Scholar", "Priest", "Shadow Mage", "Alchemist", "Tinker", "Warden"]:
            self.health = healths[class_type]
            self.mana = manas[class_type]
            self.strength = strengths[class_type]
            self.speed = agilities[class_type]
            self.intellect = intellects[class_type]