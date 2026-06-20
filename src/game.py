import random
import argparse
from .character import Character
import json
import os

# Autosave configuration
AUTOSAVE_ENABLED = True
AUTOSAVE_NAME = 'autosave_latest'

# Prompt each turn configuration (can be toggled in-game)
PROMPT_SAVE_EACH_TURN = False


class Enemy:
    def __init__(self, name, health, strength, speed):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed

    def is_alive(self):
        return self.health > 0


class Item:
    def __init__(self, name, heal=0, mana=0):
        self.name = name
        self.heal = heal
        self.mana = mana


def make_random_enemy(level=1):
    base = 50 + level * 10
    hp = base + random.randint(-5, 10)
    e = Enemy("Underling", hp, 8 + level * 2, 5 + level)
    # XP value scales with enemy HP/level
    e.xp = max(5, hp // 2)
    return e


def attack(attacker, defender):
    dmg = max(1, attacker.strength + random.randint(-3, 3))
    defender.health -= dmg
    return dmg


# Define a small spellbook of 10 spells with different mana costs and base power
SPELLS = [
    {"name": "Spark", "cost": 5, "power": 2},
    {"name": "Flame Bolt", "cost": 8, "power": 4},
    {"name": "Ice Shard", "cost": 10, "power": 6},
    {"name": "Lightning", "cost": 12, "power": 8},
    {"name": "Shadow Bolt", "cost": 15, "power": 11},
    {"name": "Mind Spike", "cost": 18, "power": 14},
    {"name": "Arcane Blast", "cost": 20, "power": 18},
    {"name": "Devouring Flame", "cost": 25, "power": 23},
    {"name": "Oblivion", "cost": 30, "power": 30},
    {"name": "World Tear", "cost": 40, "power": 45},
]


def cast_spell(caster, target, spell=None):
    """Cast a spell. If spell is None, use a default weak spell (10 mana)."""
    if spell is None:
        cost = 10
        power = 5
        name = "Basic Spell"
    else:
        cost = spell.get("cost", 10)
        power = spell.get("power", 5)
        name = spell.get("name", "Spell")

    if caster.mana < cost:
        return 0, f"No mana for {name} (cost {cost})"
    caster.mana -= cost
    dmg = max(1, caster.intellect + power + random.randint(-3, 6))
    target.health -= dmg
    # clamp target health
    if hasattr(target, 'max_health'):
        target.health = max(0, min(target.health, getattr(target, 'max_health')))
    else:
        target.health = max(0, target.health)
    return dmg, name


def use_spell(caster, target, spell):
    """Handle offensive, healing, and special spells."""
    cost = spell.get("cost", 10)
    if caster.mana < cost:
        return 0, f"No mana for {spell.get('name','Spell')} (cost {cost})"
    caster.mana -= cost

    # Healing spell
    if spell.get("type") == "heal" or spell.get("heal"):
        base = spell.get("heal", 20)
        amount = base + caster.intellect // 2 + random.randint(-3, 6)
        caster.health += amount
        # clamp to max
        if hasattr(caster, 'max_health'):
            caster.health = min(caster.health, caster.max_health)
        return amount, f"Healed {amount} with {spell.get('name')}"

    # Offensive / damage spell
    power = spell.get("power", 5)
    dmg = max(1, caster.intellect + power + random.randint(-3, 6))
    # Some specials might cost life to cast (sacrifice)
    if spell.get("self_cost"):
        caster.health -= spell.get("self_cost")
    target.health -= dmg
    if hasattr(target, 'max_health'):
        target.health = max(0, min(target.health, target.max_health))
    else:
        target.health = max(0, target.health)
    # apply cooldown to caster if defined
    cd = spell.get('cooldown')
    if cd:
        caster.cooldowns[spell.get('name')] = cd
    return dmg, spell.get("name", "Spell")


def save_game(path, player: Character, overwrite: bool = False):
    # ensure saves folder
    save_dir = os.path.join(os.getcwd(), 'saves')
    os.makedirs(save_dir, exist_ok=True)

    if not path:
        # auto-name using timestamp
        from datetime import datetime
        name = datetime.now().strftime('save_%Y%m%d_%H%M%S')
        filename = name + '.GAMESAVE'
    else:
        name = path
        if not name.lower().endswith('.gamesave'):
            filename = name + '.GAMESAVE'
        else:
            filename = name

    full = os.path.join(save_dir, filename)
    # if file exists and overwrite requested, just overwrite; otherwise append a counter to avoid overwrite
    if os.path.exists(full) and not overwrite:
        base, ext = os.path.splitext(filename)
        i = 1
        while True:
            candidate = f"{base}_{i}{ext}"
            full = os.path.join(save_dir, candidate)
            if not os.path.exists(full):
                filename = candidate
                break
            i += 1

    data = player.to_dict()
    with open(full, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Saved game to {full}")


def load_game(path):
    # accept either filename in saves/ or full path
    save_dir = os.path.join(os.getcwd(), 'saves')
    candidate = path
    if not os.path.isabs(candidate):
        candidate = os.path.join(save_dir, candidate)
    if not candidate.lower().endswith('.gamesave') and os.path.exists(candidate + '.GAMESAVE'):
        candidate = candidate + '.GAMESAVE'
    if not os.path.exists(candidate):
        print(f"Save file not found: {candidate}")
        return None
    with open(candidate, 'r', encoding='utf-8') as f:
        data = json.load(f)
    player = Character.from_dict(data)
    print(f"Loaded game from {candidate}")
    return player


def list_saves():
    save_dir = os.path.join(os.getcwd(), 'saves')
    if not os.path.exists(save_dir):
        return []
    files = [f for f in os.listdir(save_dir) if f.lower().endswith('.gamesave')]
    files.sort()
    return files


def play_encounter(player, enemy):
    # inventory as counts so we can tell how many potions the player has
    inventory = {"Small Potion": 2}
    turn = 1
    while player.health > 0 and enemy.health > 0:
        print(f"--- Turn {turn} ---")
        # per-turn save/load prompt
        if PROMPT_SAVE_EACH_TURN:
            p = input("Save/load this turn? (s=save, l=load, enter=continue): ").strip().lower()
            if p == 's':
                name = input("Save name (blank=auto): ").strip()
                save_game(name, player)
                continue
            elif p == 'l':
                files = list_saves()
                if not files:
                    print("No save files found.")
                else:
                    print("Available saves:")
                    for i, f in enumerate(files, 1):
                        print(f"{i}. {f}")
                    sel = input("Choose number to load (or name, blank to cancel): ").strip()
                    if sel:
                        try:
                            idx = int(sel) - 1
                            fname = files[idx]
                        except Exception:
                            fname = sel
                        newp = load_game(fname)
                        if newp:
                            player = newp
                            print(f"Player is now {player.name} (Level {player.level})")
                continue
        # show bars
        def bar(val, mx, length=20):
            filled = int((val / mx) * length) if mx>0 else 0
            return '[' + '#' * filled + '-' * (length - filled) + f"] {val}/{mx}"

        print(f"{player.name}: HP={bar(player.health, player.max_health)} MP={bar(player.mana, player.max_mana)}")
        print(f"{enemy.name}: HP={enemy.health}")
        actions = ["attack", "potion", "cast", "flee", "inventory", "prompt"]
        choice = input(f"Choose action {actions}: ").strip().lower()
        if choice == "attack":
            dmg = attack(player, enemy)
            print(f"You attack and deal {dmg} damage.")
        elif choice == "potion":
            count = inventory.get("Small Potion", 0)
            print(f"You have {count} Small Potion(s).")
            if count > 0:
                use = input("Use one? (y/n): ").strip().lower()
                if use == "y":
                    heal_amount = 30
                    player.health += heal_amount
                    inventory["Small Potion"] = count - 1
                    print(f"You drink a potion and heal {heal_amount} HP.")
            else:
                print("No potions left.")
        elif choice == "inventory":
            print("Inventory:")
            for k, v in inventory.items():
                print(f" - {k}: {v}")
        elif choice == "prompt":
            # toggle per-turn prompt via module globals to avoid local/global issues
            current = globals().get('PROMPT_SAVE_EACH_TURN', False)
            globals()['PROMPT_SAVE_EACH_TURN'] = not current
            print(f"Per-turn save/load prompt set to {globals()['PROMPT_SAVE_EACH_TURN']}")
            continue
        elif choice == "save":
            print("Save options: [list] to show saves, blank for auto, or type a name.")
            path = input("Save name (blank for auto): ").strip()
            if path.lower() == 'list':
                files = list_saves()
                print("Saves:")
                for f in files:
                    print(" - ", f)
                continue
            if path:
                # check if the exact name exists in saves
                save_dir = os.path.join(os.getcwd(), 'saves')
                if not path.lower().endswith('.gamesave'):
                    check_name = path + '.GAMESAVE'
                else:
                    check_name = path
                existing = os.path.join(save_dir, check_name)
                if os.path.exists(existing):
                    ans = input(f"Save '{check_name}' already exists. Overwrite? (y)es/(n)o/(a)uto-rename: ").strip().lower()
                    if ans == 'y':
                        save_game(path, player, overwrite=True)
                        continue
                    elif ans == 'a':
                        # fall through to save_game which will auto-rename
                        save_game(path, player)
                        continue
                    else:
                        print("Save cancelled.")
                        continue
            # blank path or non-existing name
            save_game(path, player)
            continue
        elif choice == "load":
            files = list_saves()
            if not files:
                print("No save files found.")
                continue
            print("Available saves:")
            for i, f in enumerate(files, 1):
                print(f"{i}. {f}")
            sel = input("Choose number to load (or name, blank to cancel): ").strip()
            if not sel:
                continue
            try:
                idx = int(sel) - 1
                fname = files[idx]
            except Exception:
                fname = sel
            newp = load_game(fname)
            if newp:
                player = newp
                print(f"Player is now {player.name} (Level {player.level})")
            continue
        elif choice == "cast":
            # Build combined menu: offensive spells, healing spells, and class-specific specials
            HEAL_SPELLS = [
                {"name": "Minor Heal", "cost": 6, "heal": 25, "type": "heal"},
                {"name": "Major Heal", "cost": 14, "heal": 60, "type": "heal"},
            ]

            CLASS_SPECIALS = {
                "Warrior": [{"name": "Raging Strike", "cost": 6, "power": 15}],
                "Ranger": [{"name": "Snipe", "cost": 8, "power": 12}],
                "Scholar": [{"name": "Arcane Insight", "cost": 12, "power": 10}],
                "Priest": [{"name": "Holy Light", "cost": 12, "heal": 40, "type": "heal"}],
                "Shadow Mage": [{"name": "Corrupt Drain", "cost": 15, "power": 25, "self_cost": 5}],
                "Alchemist": [{"name": "Toxic Cloud", "cost": 10, "power": 10}],
                "Tinker": [{"name": "Shock Trap", "cost": 12, "power": 14}],
                "Warden": [{"name": "Monster Bane", "cost": 10, "power": 20}],
            }

            available = []
            # offensive spells
            for s in SPELLS:
                available.append(s)
            # healing spells
            for s in HEAL_SPELLS:
                available.append(s)
            # class specials if any
            specials = CLASS_SPECIALS.get(getattr(player, 'class_type', ''), [])
            for s in specials:
                available.append(s)

            print("Spells and abilities:")
            for i, s in enumerate(available, 1):
                desc = s.get('name') + f" (cost {s.get('cost', '?')})"
                if s.get('heal'):
                    desc += f" heal {s.get('heal')}"
                elif s.get('power'):
                    desc += f" dmg {s.get('power')}"
                print(f"{i}. {desc}")

            sel = input("Choose number (blank to cancel): ").strip()
            if not sel:
                print("Spell casting cancelled.")
            else:
                try:
                    idx = int(sel) - 1
                    spell = available[idx]
                except Exception:
                    print("Invalid selection.")
                    spell = None
                if spell:
                    val, msg = use_spell(player, enemy, spell)
                    # If the spell healed, use_spell returns a heal message already
                    if spell.get('heal') or spell.get('type') == 'heal' or msg.startswith('Healed'):
                        print(msg)
                    else:
                        # Offensive spell: val is damage, msg is spell name
                        print(f"You cast {msg} and deal {val} damage.")
        elif choice == "flee":
            if random.random() < 0.5:
                print("You fled the encounter!")
                return False
            else:
                print("Failed to flee!")
        else:
            print("Unknown action, turn wasted.")

        if enemy.health > 0:
            edmg = attack(enemy, player)
            print(f"{enemy.name} hits you for {edmg} damage.")

        # Apply regen at end of turn
        if hasattr(player, 'regen_hp'):
            before_hp = player.health
            player.health = min(player.max_health, player.health + player.regen_hp)
            if player.health != before_hp:
                print(f"{player.name} regenerates {player.health - before_hp} HP.")
        if hasattr(player, 'regen_mana'):
            before_mp = player.mana
            player.mana = min(player.max_mana, player.mana + player.regen_mana)
            if player.mana != before_mp:
                print(f"{player.name} regenerates {player.mana - before_mp} MP.")
        # decrement cooldowns
        for k in list(player.cooldowns.keys()):
            player.cooldowns[k] -= 1
            if player.cooldowns[k] <= 0:
                del player.cooldowns[k]
            else:
                print(f"{k} cooldown: {player.cooldowns[k]} turns remaining")

        turn += 1

    if player.health > 0:
        print("You won the encounter!")
        # award XP if enemy has xp
        xp_gain = getattr(enemy, 'xp', 0)
        if xp_gain:
            print(f"You gain {xp_gain} XP.")
            leveled = player.gain_xp(xp_gain)
            if leveled:
                print(f"{player.name} is now level {player.level}.")
                # autosave on level up
                if AUTOSAVE_ENABLED:
                    save_game(AUTOSAVE_NAME, player, overwrite=True)
                    print("Autosaved (level up)")
            else:
                # still autosave on victory even if no level up
                if AUTOSAVE_ENABLED:
                    save_game(AUTOSAVE_NAME, player, overwrite=True)
                    print("Autosaved (victory)")
        return True
    else:
        print("You were defeated...")
        return False


def interactive_game():
    print("Welcome to Force of the Underworld (Prototype)")
    name = input("Enter your character name: ") or "Hero"
    classes = ["Warrior", "Ranger", "Scholar", "Priest", "Shadow Mage", "Alchemist", "Tinker", "Warden"]
    print("Choose a class:")
    for i, c in enumerate(classes, 1):
        print(f"{i}. {c}")
    idx = input("Class number: ")
    try:
        class_type = classes[int(idx) - 1]
    except Exception:
        class_type = "Warrior"

    player = Character(name, class_type)
    print(f"Created {player.name} the {class_type} (HP={player.health} MP={player.mana})")

    level = 1
    while True:
        enemy = make_random_enemy(level)
        print(f"An enemy appears: {enemy.name} (HP={enemy.health})")
        survived = play_encounter(player, enemy)
        if not survived:
            print("Game over.")
            break
        cont = input("Continue to next encounter? (y/n): ").strip().lower()
        if cont != "y":
            print("You retire victorious. Thanks for playing!")
            break
        level += 1


def run_demo():
    # Non-interactive demo for testing
    p = Character("Demo", "Scholar")
    e = make_random_enemy(1)
    print(f"Demo: {p.name} ({p.health} HP) vs {e.name} ({e.health} HP)")
    while p.health > 0 and e.health > 0:
        dmg, _ = cast_spell(p, e)
        if dmg:
            print(f"Demo cast deals {dmg}")
        else:
            print("Demo out of mana")
            break
    print("Demo finished.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Run non-interactive demo")
    args = parser.parse_args()
    if args.demo:
        run_demo()
    else:
        interactive_game()


if __name__ == "__main__":
    main()
