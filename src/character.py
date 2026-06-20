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
            self.class_type = class_type
            # max stats and regen
            self.max_health = self.health
            self.max_mana = self.mana
            # simple regen rates (per turn)
            self.regen_hp = max(1, int(self.max_health * 0.02))
            self.regen_mana = max(1, int(self.max_mana * 0.05))
            # progression
            self.level = 1
            self.xp = 0
            self.xp_to_next = 100
            # persistent inventory and cooldowns
            self.inventory = {"Small Potion": 2}
            self.cooldowns = {}

    def gain_xp(self, amount):
        self.xp += amount
        leveled = False
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()
            leveled = True
        return leveled

    def level_up(self):
        self.level += 1
        # interactive choice for stat increases
        hp_gain = 10 + (self.strength // 2)
        mana_gain = 5 + (self.intellect // 2)
        # default increases
        self.max_health += hp_gain
        self.max_mana += mana_gain
        # offer choices to the player
        try:
            choice = input(f"Level up! Choose bonus for {self.name}: \n1) +2 Strength\n2) +2 Intellect\n3) +10 Max HP\n4) +5 Max MP\nSelect (1-4, blank=default): ")
        except Exception:
            choice = ""
        if choice == "1":
            self.strength += 2
            extra = "+2 Strength"
        elif choice == "2":
            self.intellect += 2
            extra = "+2 Intellect"
        elif choice == "3":
            self.max_health += 10
            extra = "+10 Max HP"
        elif choice == "4":
            self.max_mana += 5
            extra = "+5 Max MP"
        else:
            # default: small balanced increases
            self.strength += 2
            self.intellect += 1
            extra = "+2 Str, +1 Int"

        # restore to full on level up
        self.health = self.max_health
        self.mana = self.max_mana
        # scale next level XP
        self.xp_to_next = int(self.xp_to_next * 1.5)
        print(f"*** Level up! {self.name} is now level {self.level}! ({extra}, +{hp_gain} HP, +{mana_gain} MP)")

    def to_dict(self):
        return {
            'name': self.name,
            'class_type': self.class_type,
            'level': self.level,
            'xp': self.xp,
            'xp_to_next': self.xp_to_next,
            'health': self.health,
            'max_health': self.max_health,
            'mana': self.mana,
            'max_mana': self.max_mana,
            'strength': self.strength,
            'speed': self.speed,
            'intellect': self.intellect,
            'inventory': self.inventory,
            'cooldowns': self.cooldowns,
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(data.get('name', 'Hero'), data.get('class_type', 'Warrior'))
        obj.level = data.get('level', obj.level)
        obj.xp = data.get('xp', obj.xp)
        obj.xp_to_next = data.get('xp_to_next', obj.xp_to_next)
        obj.health = data.get('health', obj.health)
        obj.max_health = data.get('max_health', obj.max_health)
        obj.mana = data.get('mana', obj.mana)
        obj.max_mana = data.get('max_mana', obj.max_mana)
        obj.strength = data.get('strength', obj.strength)
        obj.speed = data.get('speed', obj.speed)
        obj.intellect = data.get('intellect', obj.intellect)
        obj.inventory = data.get('inventory', obj.inventory)
        obj.cooldowns = data.get('cooldowns', obj.cooldowns)
        return obj