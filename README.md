<<<<<<< HEAD
# Force-of-the-underworld
A game that was inspired by Ultima V

Hey, thanks for reading this, no-one does. I mean it.

Heres the game doc.



# The Force of the Underworld

## Classic CRPG Design Document

### Inspired by the structure and feel of classic 1980s open-world RPGs such as Ultima V

---

# 1. High Concept

## Genre

Open-world party-based fantasy CRPG.

## Core Vision

The player explores a massive living fantasy world where the surface kingdoms are slowly being corrupted by an ancient force beneath the earth known as The Underworld Current.

The game focuses on:

* Exploration
* Discovery
* Dungeon crawling
* Party management
* Morality systems
* NPC schedules
* Open-ended quests
* Survival during travel
* Hidden lore
* Dangerous overworld travel

The tone is darker and more mysterious than most classic fantasy games.

---

# 2. Main Premise

Long ago the world was sustained by a colossal living structure known as the World Tree.

Deep beneath the roots of the tree rested its heart:

## The Core Gem

The Core Gem radiated life energy through the roots of the planet.
It maintained:

* seasons
* fertility
* magic
* weather
* spiritual balance
* the barrier between the surface and the Underworld

Centuries ago, during a forgotten cataclysm known as The Sundering Below, the Core Gem shattered.

Its fragments scattered across:

* ruined kingdoms
* ancient vaults
* buried temples
* abyssal depths
* corrupted forests
* forgotten cities beneath the earth

After the shattering:

* crops slowly failed
* monsters became more aggressive
* corruption spread through the land
* the dead began returning
* the Underworld started leaking into reality

This spreading corruption became known as:

## The Force of the Underworld

The Force slowly twists:

* minds
* animals
* weather
* magic
* stone
* even time itself

The player begins as a prisoner transported to a mining fortress after being falsely accused of stealing forbidden relic fragments.

During a catastrophic cave collapse, the player discovers one of the shattered Core Gem fragments hidden deep underground.

When the player touches it:

* visions of the dying World Tree appear
* ancient voices call for help
* corrupted creatures awaken
* the prison collapses

The player escapes into the surface world carrying the fragment.

The main quest becomes a journey to recover the remaining shattered pieces of the Core Gem before the world's life force completely collapses.

As the story progresses, the player discovers:

* some factions want to restore the World Tree
* others want to control the Core Gem
* some believe the world deserves to die
* the Underworld Force may have originally been sealed by the World Tree itself
* restoring the Core Gem could heal the world or unleash something ancient trapped beneath it

---

# 3. World Structure

## World Style

The world is fully explorable from the beginning.

### Regions

* Northern Highlands
* Ashen Marshes
* The Golden Coast
* Blackstone Kingdom
* The Sunken Forest
* The Hollow Desert
* Frozen Teeth Mountains
* The Underworld Depths

Each region contains:

* towns
* hidden shrines
* caves
* castles
* ruins
* wilderness encounters
* secret passages
* underground layers

---

# 4. Scale and Traversal

## Overworld

The world uses a tile-based overworld map.

### Travel Modes

* Walking
* Horseback
* Cart
* Ship
* Underground rail lifts
* Ancient portal gates

### World Features

* Day/night cycle
* Moon phases
* Weather system
* Hunger system
* Camping
* Ambushes during travel
* Random encounters

### Example Random Events

* Bandits attack at night
* Merchant caravan requests help
* Sinkhole opens nearby
* Wandering spirit appears
* Rain floods roads
* Underworld tremors spawn monsters

---

# 5. Town System

## Living NPC System

Every NPC has:

* a home
* a job
* a schedule
* relationships
* faction alignment
* opinions of the player

### Daily Schedule Example

Morning:

* work
* markets open

Evening:

* taverns active
* guards patrol

Night:

* citizens sleep
* thieves emerge
* monsters become stronger

---

# 6. Morality and Reputation

Inspired by virtue systems.

The game tracks:

## Reputation Categories

* Mercy
* Honor
* Knowledge
* Sacrifice
* Courage
* Truth
* Discipline
* Balance

Actions affect world reactions.

### Examples

Helping refugees increases Mercy.
Stealing lowers Honor.
Lying affects Truth.
Using forbidden magic damages Balance.

NPCs react dynamically.
Certain companions may leave the party.
Some towns may ban the player.

---

# 7. Party System

## Party Size

Maximum of 8 characters.

## Companion Types

* Knights
* Rangers
* Priests
* Shadow Mages
* Alchemists
* Hunters
* Underground Exiles
* Ancient Constructs

Each companion has:

* loyalty
* personal quests
* fears
* rivalries
* hidden backstory

---

# 8. Character Classes

## Base Classes

### Warrior

Heavy armor melee fighter.

### Ranger

Bow specialist with survival bonuses.

### Scholar

Reads ancient languages and uses support magic.

### Priest

Healing and light magic.

### Shadow Mage

Uses dangerous Underworld energy.

### Alchemist

Crafts potions, bombs, toxins.

### Tinker

Creates mechanical devices.

### Warden

Anti-monster specialist.

---

# 9. Stats System

## Main Attributes

* Strength
* Dexterity
* Intelligence
* Spirit
* Endurance
* Willpower

## Derived Stats

* Health
* Mana
* Stamina
* Accuracy
* Dodge
* Carry Weight
* Light Radius
* Corruption Resistance

---

# 10. Corruption System

The Underworld Force slowly corrupts:

* locations
* items
* companions
* enemies
* the player

## Corruption Effects

Low corruption:

* whispers
* visual distortions

Medium corruption:

* nightmares
* stat changes
* hallucinations

High corruption:

* mutations
* hostile reactions
* alternate endings unlocked

Players can:

* resist corruption
* embrace corruption
* weaponize corruption

---

# 11. Combat System

## Style

Turn-based tactical combat.

### Combat Features

* grid movement
* terrain bonuses
* light/darkness mechanics
* line of sight
* morale system
* status effects
* environmental hazards

### Environmental Hazards

* cave collapse
* poison gas
* cursed ground
* lava
* flooding

## Prototype

A minimal playable prototype was added at `src/game.py`.

- Run interactively:

```
python -m src.game
```

- Run a short non-interactive demo:

```
python -m src.game --demo
```

The prototype uses the existing `Character` class in `src/character.py` and provides a simple turn-based encounter loop.
* darkness

---

# 12. Magic System

## Magic Schools

* Flame
* Tide
* Stone
* Storm
* Light
* Blood
* Shadow
* Void

## Spell Discovery

Spells are discovered through:

* books
* ruins
* experimentation
* rituals
* hidden teachers

### Dangerous Magic

Underworld magic is extremely powerful but corrupting.

Examples:

* summon abyss creatures
* consume enemy souls
* open underground gates
* reshape terrain
* create living weapons

---

# 13. Dungeon Design

## Dungeon Philosophy

Dungeons are dangerous labyrinths requiring:

* mapping
* preparation
* resource management
* puzzle solving

## Dungeon Types

* Crypts
* Mines
* Ancient temples
* Underground cities
* Living caves
* Corrupted forests underground
* Giant machine ruins
* Abyssal catacombs

### Dungeon Mechanics

* darkness matters
* food matters
* traps matter
* enemies roam dynamically
* sound attracts creatures

---

# 14. Underworld Layers

The deeper the player travels underground, the stranger reality becomes.

## Layer Structure

### Layer 1

Mostly natural caves.

### Layer 2

Ancient buried civilizations.

### Layer 3

Corrupted biological tunnels.

### Layer 4

Gravity distortions.

### Layer 5

Time distortion zones.

### Layer 6

The Black Core.

---

# 15. Factions

## Main Factions

### The Crown of Blackstone

Authoritarian kingdom hiding ancient secrets.

### The Deep Delvers

Explorers studying underground ruins.

### The Ashen Priests

Religious order worshipping purification through fire.

### The Hollow Court

Corrupted nobles serving the Underworld.

### The Free Lanterns

Smugglers and rebels.

### The Silent Chorus

Hive-mind cult hearing voices from below.

---

# 16. Main Quest Structure

## Act 1 — The First Fragment

* escape the mines
* survive corrupted tunnels
* learn about the World Tree
* protect the first Core Gem fragment

## Act 2 — The Scattered Shards

* search ancient ruins for fragments
* recruit companions
* uncover the history of The Sundering Below
* prevent factions from stealing shards

## Act 3 — The Dying Lands

* entire regions begin collapsing
* forests decay
* monsters spread rapidly
* the World Tree roots begin blackening
* the player must restore minor life shrines to stabilize the world

## Act 4 — Descent Into the Underworld

* travel into deep underground layers
* discover where the largest fragment fell
* uncover the origin of the Force of the Underworld
* learn the truth about the ancient gods

## Act 5 — Restoration or Ruin

The player reforges the Core Gem.

Possible endings include:

* fully restore the World Tree
* sacrifice yourself to revive the world's life force
* control the World Tree for political power
* merge the surface and Underworld
* corrupt the restored gem and become ruler of a dying world
* destroy the cycle entirely and create a new age

# 17. Side Quests

## Examples

### The Silent Well

Villagers vanish after hearing singing from a well.

### The Iron Plague

Miners slowly turn metallic.

### Lanterns in the Fog

Ghost lights lure travelers into underground tunnels.

### The Sleeping Fortress

A castle only appears during eclipses.

### Beneath the Orchard

Roots beneath a farm hide an ancient temple.

---

# 18. Economy

## Currency

* Copper Marks
* Silver Crowns
* Blackstone Gold

## Trade Goods

* ore
* food
* relics
* monster parts
* books
* magical crystals

### Dynamic Economy

Trade routes affect prices.
Corrupted regions suffer shortages.
Bandit attacks increase costs.

---

# 19. Crafting

## Systems

* blacksmithing
* alchemy
* enchanting
* rune carving
* engineering
* cooking

## Rare Materials

* abyss crystals
* void iron
* ghost silk
* titan bone
* ember fungus

---

# 20. Survival Systems

## Needs

* hunger
* fatigue
* disease
* sanity
* temperature

## Examples

Cold regions require heat sources.
Underground spores cause hallucinations.
Darkness lowers morale.

---

# 21. Enemy Design

## Surface Enemies

* wolves
* brigands
* corrupted guards
* rogue mages

## Underworld Enemies

* bone crawlers
* whisper leeches
* blind giants
* mimic growths
* abyssal knights
* shadow masses
* memory eaters

## Elite Creatures

World bosses wander dynamically.
Some can destroy towns.

---

# 22. Bosses

## Example Bosses

### The Hollow King

Ancient ruler fused into a cave throne.

### The Maw Engine

Buried machine-god consuming souls.

### Saint Veyra

Corrupted priestess controlling plague spores.

### The First Listener

A gigantic entity buried beneath the deepest layer.

---

# 23. Visual Style

## Style Goals

* pixel art
* dark fantasy
* moody lighting
* heavy shadows
* torch illumination
* retro UI

### Inspiration Style

* Ultima V
* Ultima VI
* early CRPGs
* classic roguelikes
* gothic fantasy

---

# 24. Audio Design

## Music Style

* ambient synth
* medieval instruments
* underground drones
* eerie choir

## Sound Design

* dripping caves
* distant whispers
* echoing footsteps
* monster breathing in darkness

---

# 25. User Interface

## Interface Style

Classic CRPG interface.

### UI Components

* inventory window
* party portraits
* minimap
* message log
* command buttons
* dialogue window

### Commands

* Talk
* Search
* Use
* Cast
* Attack
* Camp
* Push
* Unlock

---

# 26. Dialogue System

## Keyword Dialogue

Inspired by classic RPG dialogue.

Players ask about:

* names
* jobs
* rumors
* locations
* factions
* secrets

Hidden keywords unlock deeper lore.

---

# 27. Hidden Systems

## Secret Mechanics

* hidden underground kingdoms
* ancient language translation
* dream worlds
* corruption mutations
* faction infiltration
* hidden endings
* procedural underground shifts

---

# 28. Save System

## Save Philosophy

The game encourages preparation.

Options:

* manual saves
* limited safe resting
* dangerous dungeon persistence

---

# 29. Technical Structure

## Engine Possibilities

* Godot
* Unity
* Custom C++ engine

## Rendering Modes

* top-down tile mode
* dungeon mode
* tactical combat maps

---

# 30. Expansion Ideas

## Future Expansions

### Seas of Ash

Naval exploration expansion.

### The Frozen Below

Ice continent with buried cities.

### The Broken Moon

Reality distortion expansion.

---

# 31. Multiplayer Concepts

Optional future mode.

## Co-op Features

* shared party control
* trading
* dungeon expeditions
* faction warfare

---

# 32. Example Intro Sequence

The game opens in darkness.

The player hears:

* mining tools
* distant screams
* rock shifting
* whispers from beneath the walls

A prisoner nearby says:

"You hear it too, don't you? The breathing under the stone."

Suddenly:

* tremors begin
* walls crack
* black growth spreads through the tunnels
* creatures emerge

The prison collapses.

The player escapes into the surface world as the first signs of catastrophe begin spreading across the kingdom.

---

# 33. Endgame Themes

The game explores:

* fear of the unknown
* corruption of power
* sacrifice
* civilization versus truth
* whether humanity deserves survival
* the cost of sealing ancient horrors

The Underworld Force may ultimately be:

* a prison
* a god
* the planet itself
* humanity's buried consciousness
* or something far older.

---

# 34. Final Design Goals

The game should feel:

* mysterious
* dangerous
* immersive
* systemic
* reactive
* lonely at times
* rewarding to explore

The player should constantly feel that:

* the world existed before them
* hidden things are beneath the surface
* every ruin has history
* every descent underground matters

The deeper the player travels, the more reality itself begins to unravel.
=======
Force-of-the-underworld

A game that was inspired by Ultima V



Hey, thanks for reading this, no one does. I mean it.



Here's the game doc.



The Force of the Underworld

Classic CRPG Design Document

Inspired by the structure and feel of classic 1980s open-world RPGs such as Ultima V

1\. High Concept

Genre

Open-world party-based fantasy CRPG.



Core Vision

The player explores a massive living fantasy world where the surface kingdoms are slowly being corrupted by an ancient force beneath the earth known as The Underworld Current.



The game focuses on:



Exploration

Discovery

Dungeon crawling

Party management

Morality systems

NPC schedules

Open-ended quests

Survival during travel

Hidden lore

Dangerous overworld travel

The tone is darker and more mysterious than most classic fantasy games.



2\. Main Premise

Long ago the world was sustained by a colossal living structure known as the World Tree.



Deep beneath the roots of the tree rested its heart:



The Core Gem

The Core Gem radiated life energy through the roots of the planet. It maintained:



seasons

fertility

magic

weather

spiritual balance

the barrier between the surface and the Underworld

Centuries ago, during a forgotten cataclysm known as The Sundering Below, the Core Gem shattered.



Its fragments scattered across:



ruined kingdoms

ancient vaults

buried temples

abyssal depths

corrupted forests

forgotten cities beneath the earth

After the shattering:



crops slowly failed

monsters became more aggressive

corruption spread through the land

the dead began returning

the Underworld started leaking into reality

This spreading corruption became known as:



The Force of the Underworld

The Force slowly twists:



minds

animals

weather

magic

stone

even time itself

The player begins as a prisoner transported to a mining fortress after being falsely accused of stealing forbidden relic fragments.



During a catastrophic cave collapse, the player discovers one of the shattered Core Gem fragments hidden deep underground.



When the player touches it:



visions of the dying World Tree appear

ancient voices call for help

corrupted creatures awaken

the prison collapses

The player escapes into the surface world carrying the fragment.



The main quest becomes a journey to recover the remaining shattered pieces of the Core Gem before the world's life force completely collapses.



As the story progresses, the player discovers:



some factions want to restore the World Tree

others want to control the Core Gem

some believe the world deserves to die

the Underworld Force may have originally been sealed by the World Tree itself

restoring the Core Gem could heal the world or unleash something ancient trapped beneath it

3\. World Structure

World Style

The world is fully explorable from the beginning.



Regions

Northern Highlands

Ashen Marshes

The Golden Coast

Blackstone Kingdom

The Sunken Forest

The Hollow Desert

Frozen Teeth Mountains

The Underworld Depths

Each region contains:



towns

hidden shrines

caves

castles

ruins

wilderness encounters

secret passages

underground layers

4\. Scale and Traversal

Overworld

The world uses a tile-based overworld map.



Travel Modes

Walking

Horseback

Cart

Ship

Underground rail lifts

Ancient portal gates

World Features

Day/night cycle

Moon phases

Weather system

Hunger system

Camping

Ambushes during travel

Random encounters

Example Random Events

Bandits attack at night

Merchant caravan requests help

Sinkhole opens nearby

Wandering spirit appears

Rain floods roads

Underworld tremors spawn monsters

5\. Town System

Living NPC System

Every NPC has:



a home

a job

a schedule

relationships

faction alignment

opinions of the player

Daily Schedule Example

Morning:



work

markets open

Evening:



taverns active

guards patrol

Night:



citizens sleep

thieves emerge

monsters become stronger

6\. Morality and Reputation

Inspired by virtue systems.



The game tracks:



Reputation Categories

Mercy

Honor

Knowledge

Sacrifice

Courage

Truth

Discipline

Balance

Actions affect world reactions.



Examples

Helping refugees increases Mercy. Stealing lowers Honor. Lying affects Truth. Using forbidden magic damages Balance.



NPCs react dynamically. Certain companions may leave the party. Some towns may ban the player.



7\. Party System

Party Size

Maximum of 8 characters.



Companion Types

Knights

Rangers

Priests

Shadow Mages

Alchemists

Hunters

Underground Exiles

Ancient Constructs

Each companion has:



loyalty

personal quests

fears

rivalries

hidden backstory

8\. Character Classes

Base Classes

Warrior

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



9\. Stats System

Main Attributes

Strength

Dexterity

Intelligence

Spirit

Endurance

Willpower

Derived Stats

Health

Mana

Stamina

Accuracy

Dodge

Carry Weight

Light Radius

Corruption Resistance

10\. Corruption System

The Underworld Force slowly corrupts:



locations

items

companions

enemies

the player

Corruption Effects

Low corruption:



whispers

visual distortions

Medium corruption:



nightmares

stat changes

hallucinations

High corruption:



mutations

hostile reactions

alternate endings unlocked

Players can:



resist corruption

embrace corruption

weaponize corruption

11\. Combat System

Style

Turn-based tactical combat.



Combat Features

grid movement

terrain bonuses

light/darkness mechanics

line of sight

morale system

status effects

environmental hazards

Environmental Hazards

cave collapse

poison gas

cursed ground

lava

flooding

darkness

12\. Magic System

Magic Schools

Flame

Tide

Stone

Storm

Light

Blood

Shadow

Void

Spell Discovery

Spells are discovered through:



books

ruins

experimentation

rituals

hidden teachers

Dangerous Magic

Underworld magic is extremely powerful but corrupting.



Examples:



summon abyss creatures

consume enemy souls

open underground gates

reshape terrain

create living weapons

13\. Dungeon Design

Dungeon Philosophy

Dungeons are dangerous labyrinths requiring:



mapping

preparation

resource management

puzzle solving

Dungeon Types

Crypts

Mines

Ancient temples

Underground cities

Living caves

Corrupted forests underground

Giant machine ruins

Abyssal catacombs

Dungeon Mechanics

darkness matters

food matters

traps matter

enemies roam dynamically

sound attracts creatures

14\. Underworld Layers

The deeper the player travels underground, the stranger reality becomes.



Layer Structure

Layer 1

Mostly natural caves.



Layer 2

Ancient buried civilizations.



Layer 3

Corrupted biological tunnels.



Layer 4

Gravity distortions.



Layer 5

Time distortion zones.



Layer 6

The Black Core.



15\. Factions

Main Factions

The Crown of Blackstone

Authoritarian kingdom hiding ancient secrets.



The Deep Delvers

Explorers studying underground ruins.



The Ashen Priests

Religious order worshipping purification through fire.



The Hollow Court

Corrupted nobles serving the Underworld.



The Free Lanterns

Smugglers and rebels.



The Silent Chorus

Hive-mind cult hearing voices from below.



16\. Main Quest Structure

Act 1 — The First Fragment

escape the mines

survive corrupted tunnels

learn about the World Tree

protect the first Core Gem fragment

Act 2 — The Scattered Shards

search ancient ruins for fragments

recruit companions

uncover the history of The Sundering Below

prevent factions from stealing shards

Act 3 — The Dying Lands

entire regions begin collapsing

forests decay

monsters spread rapidly

the World Tree roots begin blackening

the player must restore minor life shrines to stabilize the world

Act 4 — Descent Into the Underworld

travel into deep underground layers

discover where the largest fragment fell

uncover the origin of the Force of the Underworld

learn the truth about the ancient gods

Act 5 — Restoration or Ruin

The player reforges the Core Gem.



Possible endings include:



fully restore the World Tree

sacrifice yourself to revive the world's life force

control the World Tree for political power

merge the surface and Underworld

corrupt the restored gem and become ruler of a dying world

destroy the cycle entirely and create a new age

17\. Side Quests

Examples

The Silent Well

Villagers vanish after hearing singing from a well.



The Iron Plague

Miners slowly turn metallic.



Lanterns in the Fog

Ghost lights lure travelers into underground tunnels.



The Sleeping Fortress

A castle only appears during eclipses.



Beneath the Orchard

Roots beneath a farm hide an ancient temple.



18\. Economy

Currency

Copper Marks

Silver Crowns

Blackstone Gold

Trade Goods

ore

food

relics

monster parts

books

magical crystals

Dynamic Economy

Trade routes affect prices. Corrupted regions suffer shortages. Bandit attacks increase costs.



19\. Crafting

Systems

blacksmithing

alchemy

enchanting

rune carving

engineering

cooking

Rare Materials

abyss crystals

void iron

ghost silk

titan bone

ember fungus

20\. Survival Systems

Needs

hunger

fatigue

disease

sanity

temperature

Examples

Cold regions require heat sources. Underground spores cause hallucinations. Darkness lowers morale.



21\. Enemy Design

Surface Enemies

wolves

brigands

corrupted guards

rogue mages

Underworld Enemies

bone crawlers

whisper leeches

blind giants

mimic growths

abyssal knights

shadow masses

memory eaters

Elite Creatures

World bosses wander dynamically. Some can destroy towns.



22\. Bosses

Example Bosses

The Hollow King

Ancient ruler fused into a cave throne.



The Maw Engine

Buried machine-god consuming souls.



Saint Veyra

Corrupted priestess controlling plague spores.



The First Listener

A gigantic entity buried beneath the deepest layer.



23\. Visual Style

Style Goals

pixel art

dark fantasy

moody lighting

heavy shadows

torch illumination

retro UI

Inspiration Style

Ultima V

Ultima VI

early CRPGs

classic roguelikes

gothic fantasy

24\. Audio Design

Music Style

ambient synth

medieval instruments

underground drones

eerie choir

Sound Design

dripping caves

distant whispers

echoing footsteps

monster breathing in darkness

25\. User Interface

Interface Style

Classic CRPG interface.



UI Components

inventory window

party portraits

minimap

message log

command buttons

dialogue window

Commands

Talk

Search

Use

Cast

Attack

Camp

Push

Unlock

26\. Dialogue System

Keyword Dialogue

Inspired by classic RPG dialogue.



Players ask about:



names

jobs

rumors

locations

factions

secrets

Hidden keywords unlock deeper lore.



27\. Hidden Systems

Secret Mechanics

hidden underground kingdoms

ancient language translation

dream worlds

corruption mutations

faction infiltration

hidden endings

procedural underground shifts

28\. Save System

Save Philosophy

The game encourages preparation.



Options:



manual saves

limited safe resting

dangerous dungeon persistence

29\. Technical Structure

Engine Possibilities

Godot

Unity

Custom C++ engine

Rendering Modes

top-down tile mode

dungeon mode

tactical combat maps

30\. Expansion Ideas

Future Expansions

Seas of Ash

Naval exploration expansion.



The Frozen Below

Ice continent with buried cities.



The Broken Moon

Reality distortion expansion.



31\. Multiplayer Concepts

Optional future mode.



Co-op Features

shared party control

trading

dungeon expeditions

faction warfare

32\. Example Intro Sequence

The game opens in darkness.



The player hears:



mining tools

distant screams

rock shifting

whispers from beneath the walls

A prisoner nearby says:



"You hear it too, don't you? The breathing under the stone."



Suddenly:



tremors begin

walls crack

black growth spreads through the tunnels

creatures emerge

The prison collapses.



The player escapes into the surface world as the first signs of catastrophe begin spreading across the kingdom.



33\. Endgame Themes

The game explores:



fear of the unknown

corruption of power

sacrifice

civilization versus truth

whether humanity deserves survival

the cost of sealing ancient horrors

The Underworld Force may ultimately be:



a prison

a god

the planet itself

humanity's buried consciousness

or something far older.

34\. Final Design Goals

The game should feel:



mysterious

dangerous

immersive

systemic

reactive

lonely at times

rewarding to explore

The player should constantly feel that:



the world existed before them

hidden things are beneath the surface

every ruin has history

every descent underground matters

The deeper the player travels, the more reality itself begins to unravel.

>>>>>>> 8ff793d (hello world)
