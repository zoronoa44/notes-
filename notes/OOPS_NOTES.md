# Python OOP — Complete Notes (Pokémon Edition)

> Built while learning OOP through debugging real bugs — recursion errors, scope confusion, setter/getter mix-ups. These notes cover every concept with definitions, analogies, code, and common mistakes.

---

## Table of Contents

1. [Why OOP Exists](#1-why-oop-exists)
2. [Class & Object](#2-class--object)
3. [`self` and `__init__`](#3-self-and-__init__)
4. [Instance vs Class Attributes](#4-instance-vs-class-attributes)
5. [Methods](#5-methods)
6. [Encapsulation](#6-encapsulation)
7. [Property, Getter, Setter — Deep Dive](#7-property-getter-setter--deep-dive)
8. [Inheritance](#8-inheritance)
9. [Polymorphism](#9-polymorphism)
10. [Abstraction](#10-abstraction)
11. [Dunder (Magic) Methods](#11-dunder-magic-methods)
12. [classmethod & staticmethod — Deep Dive](#12-classmethod--staticmethod--deep-dive)
13. [Composition](#13-composition)
14. [Common Mistakes Cheat Sheet](#14-common-mistakes-cheat-sheet)
15. [Interview Questions](#15-interview-questions)
16. [Mini Project — Battle Simulator](#16-mini-project--battle-simulator)

---

## 1. Why OOP Exists

**The problem, without OOP:**

```python
name1 = "Pikachu"
hp1 = 35
type1 = "Electric"

name2 = "Charmander"
hp2 = 39
type2 = "Fire"
```

Related data (`name1`, `hp1`, `type1` all describe ONE Pokémon) is scattered across separate variables with no connection. Scaling to 100 Pokémon means 100 sets of numbered variables. Functions have to be handed a pile of loose arguments every time.

**Definition:** Object-Oriented Programming (OOP) is a programming paradigm that bundles related **data** (attributes) and **behavior** (methods) into a single unit called an **object**.

**Analogy:** Instead of three separate spreadsheets for a person's name, age, and address that never talk to each other, OOP puts them in one row of one table — one self-contained unit.

---

## 2. Class & Object

**Definitions:**

| Term | Definition |
|---|---|
| **Class** | A blueprint/template that defines what attributes and methods its objects will have. |
| **Object** | A concrete instance created from a class blueprint. Also called an **instance**. |
| **Instantiation** | The act of creating an object from a class. |

**Analogy:** "Pikachu" as a species/concept in the Pokédex is the **class**. The actual electric mouse sitting on your shoulder is the **object**.

```python
class Pokemon:
    def __init__(self, name, hp, ptype):
        self.name = name
        self.hp = hp
        self.ptype = ptype

pikachu = Pokemon("Pikachu", 35, "Electric")
print(pikachu.name)   # Pikachu
```

**Line-by-line:**
- `class Pokemon:` — declares a new blueprint. Capitalized by convention (PEP 8).
- `def __init__(self, name, hp, ptype):` — special setup method, runs automatically on creation.
- `self.name = name` — stores the value onto *this specific object*.

**Common mistakes:**
- Forgetting `self` in `__init__` → `TypeError: __init__() takes 3 positional arguments but 4 were given`
- Not assigning the created object to a variable — it vanishes immediately.

---

## 3. `self` and `__init__`

**Definition of `self`:** the automatic first parameter of every instance method, representing "the specific object this method is currently running on." Not a keyword — just a very strong convention (never rename it).

**Definition of `__init__`:** the constructor method. Runs automatically the moment an object is created, used to set up initial attribute values.

```
pikachu = Pokemon("Pikachu", 35, "Electric")
       │
       ▼
Python actually calls:
Pokemon.__init__(pikachu, "Pikachu", 35, "Electric")
```

`self` is simply Python auto-filling "which object am I working on" as the first argument — you never pass it manually.

**Official docs (docs.python.org):** *"the instance is passed as the first argument of the function."*

**Common mistake:**
```python
def __init__(self, name, hp, ptype):
    name = name   # ❌ creates a local variable, dies when __init__ ends
```
This never actually stores anything on the object → `pikachu.name` → `AttributeError`.

---

## 4. Instance vs Class Attributes

| Type | Definition | Example |
|---|---|---|
| **Instance attribute** | Belongs to one specific object, unique per instance | `self.hp` — every Pokémon has different HP |
| **Class attribute** | Shared by ALL instances of the class | `pokedex_count` — one shared counter |

```python
class Pokemon:
    pokedex_count = 0        # class attribute

    def __init__(self, name, hp, ptype):
        self.name = name     # instance attribute
        self.hp = hp
        self.ptype = ptype
        Pokemon.pokedex_count += 1

p1 = Pokemon("Pikachu", 35, "Electric")
p2 = Pokemon("Charmander", 39, "Fire")
print(Pokemon.pokedex_count)   # 2
```

**⚠️ Danger — mutable class attributes:**
```python
class Pokemon:
    moves = []   # ❌ shared by EVERY Pokémon!

p1 = Pokemon()
p1.moves.append("Thunderbolt")
p2 = Pokemon()
print(p2.moves)   # ['Thunderbolt'] — p2 never learned this, but it shows up!
```
**Fix:** put `self.moves = []` inside `__init__` so each object gets its own fresh list.

---

## 5. Methods

**Definition:** a function defined inside a class that operates on an object's data. The first parameter is always `self`.

```python
class Pokemon:
    def __init__(self, name, hp, ptype):
        self.name = name
        self.hp = hp
        self.ptype = ptype

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {amount} damage! HP: {self.hp}")

pikachu = Pokemon("Pikachu", 35, "Electric")
pikachu.take_damage(10)   # Pikachu took 10 damage! HP: 25
```

`pikachu.take_damage(10)` is shorthand for `Pokemon.take_damage(pikachu, 10)` — `self` becomes `pikachu`.

**Common mistake:** calling `Pokemon.take_damage(10)` directly (skipping the instance) crashes, because `10` gets bound to `self` and `amount` is missing.

---

## 6. Encapsulation

**Definition:** the OOP principle of hiding/protecting internal data from outside interference, and controlling how it's accessed and modified. One of the 4 pillars of OOP (alongside Inheritance, Polymorphism, Abstraction).

**Why it exists:** without it, any code anywhere could do `pikachu.hp = -9999` or `pikachu.hp = "banana"` and silently corrupt the object.

**Python's access convention** (no true "private" enforcement like Java — just naming conventions):

| Prefix | Meaning | Enforced by Python? |
|---|---|---|
| `name` | Public — free to use | — |
| `_name` | Protected — "internal use, please don't touch" | No, convention only |
| `__name` | Private — name-mangled to `_ClassName__name` | Partially (discourages accidental access) |

Encapsulation in Python is implemented properly using **`@property`** — covered in full detail in the next section.

---

## 7. Property, Getter, Setter — Deep Dive

This is the section people get stuck on most. Full breakdown below.

### 7.1 Definitions

| Term | Definition |
|---|---|
| **Getter** | A method that *retrieves* (reads) the value of an attribute. Triggered by reading `obj.attribute` (no `=`). |
| **Setter** | A method that *sets* (writes) a new value to an attribute, usually with validation. Triggered by `obj.attribute = value`. |
| **`@property`** | A built-in Python decorator that turns a method into a getter, letting it be accessed like a plain attribute (no parentheses). |
| **`@x.setter`** | A decorator (built onto the property object created by `@property`) that attaches a setter function to that same property name. |

### 7.2 The mental model — Box and Guards

Think of the real data as a **box** (`self._hp`), with two **guards** controlling access:

```
     GUARD 1 (getter)         GUARD 2 (setter)
   "give me the value"      "here's a new value"
        │                          │
        ▼                          ▼
   ┌─────────────────────────────────────┐
   │            BOX  (self._hp)          │
   └─────────────────────────────────────┘
```

- **Getter** — runs when you *read* `obj.hp` (no `=` sign). Goes into the box, hands you the value.
- **Setter** — runs when you *write* `obj.hp = value` (there's an `=` sign). Checks/validates first, THEN saves into the box.

**The one-second rule:** is there an `=` sign right after `.attribute`?
- No `=` → **getter** runs (you're asking)
- Yes `=` → **setter** runs (you're giving)

### 7.3 Full working example

```python
class Pokemon:
    def __init__(self, name, hp):
        self.name = name
        self._hp = hp          # the box — underscore = "internal storage"

    @property
    def hp(self):               # GETTER
        return self._hp

    @hp.setter
    def hp(self, new_value):    # SETTER
        if new_value < 0:
            new_value = 0
        self._hp = new_value    # ⚠️ MUST save to the box, every path
```

```python
pikachu = Pokemon("Pikachu", 35)
print(pikachu.hp)        # 35   → getter runs
pikachu.hp = -50         # setter runs, clamps to 0, saves it
print(pikachu.hp)        # 0    → getter runs
```

### 7.4 Why `@property`, not `@getter`

There is no `@getter` in real Python. `@property` is the built-in mechanism — it's literally a built-in type (`property`). The decorated method automatically becomes the getter. If you've seen `@getter` in a video, the presenter was speaking loosely, or using a custom, non-standard decorator.

### 7.5 Why `@hp.setter` has a dot in it

```python
@property
def hp(self):
    return self._hp
```

The moment this runs, `hp` is no longer a plain function — it becomes a **property object**. That object has a built-in feature called `.setter`. So:

```python
@hp.setter
def hp(self, new_value):
    ...
```

means: *"take the property object `hp`, use its `.setter` tool to attach this function as its setter."* The dot-name is required because a class might have multiple properties (`hp`, `level`, `exp`) — Python needs to know exactly which one you're adding a setter to.

### 7.6 The #1 bug — infinite recursion

```python
@property
def hp(self):
    return self.hp   # ❌ INFINITE RECURSION
```

Accessing `self.hp` *inside* `hp`'s own getter re-triggers the getter, forever → `RecursionError`.

**Fix:** the getter/setter must always talk to the **underscore-prefixed box** (`self._hp`), never the bare property name (`self.hp`) — or it calls itself forever.

Same trap applies inside the setter:
```python
@hp.setter
def hp(self, new_value):
    if new_value < 0:
        self.hp = 0    # ❌ also infinite recursion — calls the setter again!
```
Must be `self._hp = 0` instead.

### 7.7 The #2 bug — setter with no "normal path"

```python
@hp.setter
def hp(self, new_value):
    if new_value < 0:
        new_value = 0
        self._hp = 0
    # ❌ missing: what happens when new_value is FINE?
```

If `new_value` is valid (not negative), nothing is saved — `self._hp` never updates on the common case. The save line (`self._hp = new_value`) must run on **every path**, not just the error path.

### 7.8 Setters are NOT for actions/methods

A setter takes exactly **one** value and treats it as "the new value to assign." If an operation needs *extra context* (e.g., "how much damage", "who attacked"), it's an **action**, not an assignment — it belongs in a regular method, not a setter.

```python
# ❌ WRONG — trying to force an action into a setter
@hp.setter
def take_damage(self, dmg_amount):
    ...

# ✅ RIGHT — action = regular method, which internally uses self.hp
def take_damage(self, dmg_amount):
    self.hp -= dmg_amount   # reads getter, computes, triggers setter automatically
```

### 7.9 Reading `self.hp -= dmg_amount` — the hidden double-guard

This single line secretly does BOTH steps:

```
self.hp -= dmg_amount
    │
    ├── STEP 1: reads self.hp  → GETTER runs → returns current value
    ├── STEP 2: subtracts dmg_amount
    └── STEP 3: writes result back to self.hp → SETTER runs → validates & saves
```

Any line shaped like `obj.attr = obj.attr <operation>` (including `+=`, `-=`) always means **getter first, then setter** — read, compute, write back.

### 7.10 Quick reference table

| Code | Getter runs? | Setter runs? |
|---|---|---|
| `x = pikachu.hp` | ✅ | ❌ |
| `pikachu.hp = 50` | ❌ | ✅ |
| `pikachu.hp -= 10` | ✅ | ✅ (in that order) |
| `pikachu.hp += 5` | ✅ | ✅ (in that order) |
| `y = pikachu.hp + charmander.hp` | ✅ ✅ (once per Pokémon) | ❌ (`y` is a plain variable, not a property) |
| `pikachu.take_damage(10)` | depends on the method's internal code | depends on the method's internal code |

### 7.11 Can I call a property like a function?

**No.** Once `@property` is applied to a name, that name is no longer callable with parentheses.

```python
pikachu.hp        # ✅ correct way to read
pikachu.hp()       # ❌ TypeError — 'int' object is not callable (or similar)
pikachu.hp = 10    # ✅ correct way to write
```

This restriction applies **only** to the specific name turned into a property. Every other regular method in the class (`take_damage`, `is_fainted`, etc.) works exactly as normal, called with `object.method(args)`.

---

## 8. Inheritance

**Definition:** a mechanism where a new class (**child/subclass**) derives attributes and methods from an existing class (**parent/superclass**), and can add or override its own.

**Relationship type:** "is-a" — `FirePokemon` **is a** `Pokemon`.

```
        Pokemon
       ┌──┴──┐
  FirePokemon  WaterPokemon
```

```python
class Pokemon:
    def __init__(self, name, hp, ptype):
        self.name = name
        self.hp = hp
        self.ptype = ptype

    def attack(self):
        print(f"{self.name} uses Tackle!")


class FirePokemon(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp, ptype="Fire")   # reuse parent's setup

    def attack(self):                               # OVERRIDE
        print(f"{self.name} uses Flamethrower! 🔥")

charmander = FirePokemon("Charmander", 39)
charmander.attack()   # Charmander uses Flamethrower! 🔥
```

**`super().__init__(...)`** calls the parent's constructor so you don't repeat `self.name = name` etc. (DRY principle — Don't Repeat Yourself).

**Common mistake:** forgetting `super().__init__()` → `self.name` never gets set on the child → crashes later.

**Official docs:** [docs.python.org — Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)

---

## 9. Polymorphism

**Definition:** "many forms" — the ability for different classes to respond to the same method call, each in its own way.

```python
team = [FirePokemon("Charmander", 39), Pokemon("Rattata", 30, "Normal")]

for p in team:
    p.attack()

# Charmander uses Flamethrower! 🔥
# Rattata uses Tackle!
```

The loop doesn't check *what kind* of Pokémon it has — it just calls `.attack()` and trusts each object to handle it correctly.

**Note:** polymorphism does NOT strictly require inheritance. Python uses **duck typing** — "if it has an `.attack()` method, it works," related class hierarchy or not.

---

## 10. Abstraction

**Definition:** hiding implementation complexity and exposing only a required "contract" — a base class that forces subclasses to implement specific methods, without providing a usable default itself.

```python
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @abstractmethod
    def attack(self):
        pass   # no implementation — subclasses MUST provide one

p = Pokemon("Test", 10)
# TypeError: Can't instantiate abstract class Pokemon with abstract method attack
```

That error is intentional protection — you can't create a "bare" Pokémon with no defined behavior.

**Official docs:** [`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html)

---

## 11. Dunder (Magic) Methods

**Definition:** methods surrounded by double underscores (`__name__`) that let custom objects integrate with Python's built-in syntax (`print()`, `==`, `<`, `len()`, etc.). "Dunder" = **D**ouble **UNDER**score.

```python
class Pokemon:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def __str__(self):
        return f"{self.name} (Lv.{self.level}, HP:{self.hp})"

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

pikachu = Pokemon("Pikachu", 35, 12)
charmander = Pokemon("Charmander", 39, 15)

print(pikachu)                        # Pikachu (Lv.12, HP:35)   — uses __str__
print(pikachu < charmander)           # True                     — uses __lt__
team = sorted([pikachu, charmander])  # sorted() uses __lt__ automatically!
```

Without `__str__`, `print(pikachu)` would show `<__main__.Pokemon object at 0x7f8a2c1b0a90>`. Without `__lt__`, `sorted()` would crash on a list of custom objects.

**Common mistake:** implementing `__eq__` without `__hash__` → `TypeError: unhashable type` when putting objects in a `set` or using as `dict` keys.

**Official docs:** [Data model / dunder methods](https://docs.python.org/3/reference/datamodel.html)

---

## 12. classmethod & staticmethod — Deep Dive

### 12.1 Definitions

| Term | Definition |
|---|---|
| **Instance method** | Default method type. First parameter `self` — the specific object. Needs an instance to call. |
| **`@classmethod`** | A method bound to the **class itself**, not an instance. First parameter is `cls` (the class). Commonly used as an alternative constructor ("factory method"). |
| **`@staticmethod`** | A method that belongs to the class namespace but needs **neither** `self` nor `cls`. Pure logic related to the class's purpose. |

### 12.2 Code

```python
class Pokemon:
    total_created = 0

    def __init__(self, name, hp, ptype):
        self.name = name
        self.hp = hp
        self.ptype = ptype
        Pokemon.total_created += 1

    @classmethod
    def from_dict(cls, data):
        """Factory: build a Pokemon from a dictionary."""
        return cls(data["name"], data["hp"], data["type"])

    @staticmethod
    def is_super_effective(attack_type, defend_type):
        """Doesn't need self OR cls — pure logic."""
        chart = {"Water": "Fire", "Fire": "Grass", "Grass": "Water"}
        return chart.get(attack_type) == defend_type
```

```python
raw = {"name": "Squirtle", "hp": 44, "type": "Water"}
squirtle = Pokemon.from_dict(raw)
print(squirtle.name)                                    # Squirtle
print(Pokemon.is_super_effective("Water", "Fire"))       # True
```

### 12.3 Side-by-side comparison

| Decorator | Auto-passed argument | Called via | Typical use case |
|---|---|---|---|
| *(none — instance method)* | `self` (the object) | `instance.method()` | Needs THIS object's data (e.g., `take_damage`) |
| `@classmethod` | `cls` (the class) | `ClassName.method()` or `instance.method()` | Alternative constructors, touching class-level (shared) data |
| `@staticmethod` | nothing automatic | `ClassName.method()` or `instance.method()` | Logic related to the class conceptually, but touches no instance/class data |

### 12.4 Why `cls` instead of a hardcoded class name?

```python
@classmethod
def from_dict(cls, data):
    return cls(data["name"], data["hp"], data["type"])
```

Using `cls(...)` instead of `Pokemon(...)` means if a subclass (e.g. `FirePokemon`) inherits this method and calls `FirePokemon.from_dict(data)`, `cls` automatically becomes `FirePokemon` — the factory method correctly builds the *right* subclass, not always the base class.

### 12.5 Common mistake

Using `@staticmethod` when the logic actually needs `self` → `NameError: name 'self' is not defined`, because it's simply never passed in.

---

## 13. Composition

**Definition:** a design principle where an object is built by **containing** other objects, rather than inheriting from them. Relationship type: **"has-a"**, as opposed to inheritance's "is-a".

```python
class Trainer:
    def __init__(self, name):
        self.name = name
        self.team = []             # Trainer HAS a list of Pokemon — composition

    def add_pokemon(self, pokemon):
        self.team.append(pokemon)
        print(f"{pokemon.name} joined {self.name}'s team!")

ash = Trainer("Ash")
ash.add_pokemon(Pokemon("Pikachu", 35, "Electric"))
# Pikachu joined Ash's team!
```

**Why the distinction matters:** `Trainer` should **not** inherit from `Pokemon` — a trainer isn't a *type* of Pokémon, he *owns* them. Composition models real-world relationships more accurately than forcing everything into an inheritance tree.

**Design principle:** *"favor composition over inheritance"* when the relationship isn't a true is-a.

---

## 14. Common Mistakes Cheat Sheet

| Mistake | Symptom | Fix |
|---|---|---|
| `return self.hp` inside `hp`'s own getter | `RecursionError` | Return `self._hp` (the box), not `self.hp` (the door) |
| `self.hp = 0` inside `hp`'s own setter | `RecursionError` | Assign `self._hp = 0` directly |
| Setter with no save on the "normal" path | Value silently never updates | Add `self._hp = new_value` outside/after the validation `if` |
| Forcing an action (e.g. `take_damage`) into a setter | Confusing API, wrong argument meaning | Actions = regular methods; setters = pure "set this one value" |
| Forgetting `super().__init__()` in a child class | `AttributeError` later when using inherited attributes | Always call `super().__init__(...)` in the child's `__init__` |
| Mutable class attribute (`moves = []`) shared across instances | Data "leaks" between unrelated objects | Move it into `__init__` as `self.moves = []` |
| `@staticmethod` that actually needs `self` | `NameError: name 'self' is not defined` | Use a regular method or `@classmethod` instead |
| Calling `Pokemon.method(10)` without an instance | Wrong argument gets bound to `self` | Call via an instance: `pikachu.method(10)` |
| Trying to call a property like `pikachu.hp()` | `TypeError: not callable` | Properties are accessed without parentheses: `pikachu.hp` |

---

## 15. Interview Questions

1. What's the difference between `@classmethod` and `@staticmethod`?
2. What's the difference between method overriding and overloading in Python? (Python doesn't support traditional overloading.)
3. Why doesn't Python have true "private" attributes like Java?
4. When would you choose composition over inheritance?
5. What's the difference between `__str__` and `__repr__`?
6. Why does implementing `__eq__` sometimes require implementing `__hash__` too?
7. What happens if you forget to call `super().__init__()` in a subclass?
8. Why can't you instantiate a class with an unimplemented `@abstractmethod`?

---

## 16. Mini Project — Battle Simulator

Skeleton to build out (fill every `TODO` yourself — that's where the actual learning happens):

```python
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, name, hp, level):
        self.name = name
        self._hp = hp
        self.level = level

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)   # TODO: why does this prevent negative HP?

    @abstractmethod
    def attack(self, target):
        pass

    def is_fainted(self):
        # TODO: return True if hp is 0
        pass

    def __str__(self):
        return f"{self.name} (Lv.{self.level}, HP:{self.hp})"


class FirePokemon(Pokemon):
    def attack(self, target):
        # TODO: deal damage to target.hp, print a message
        pass


class Trainer:
    def __init__(self, name):
        self.name = name
        self.team = []

    def add_pokemon(self, pokemon):
        # TODO
        pass


def battle(p1: Pokemon, p2: Pokemon):
    # TODO: loop turns, alternate attacks, stop when one is_fainted()
    pass
```

**Requirements:**
1. Fill every `TODO`.
2. Add at least 2 more Pokémon subclasses (Water, Grass).
3. Make `battle()` run a full fight and print a winner.
4. Push to GitHub as `pokemon-oop-battle-sim`.
5. Decide your own tie-break rule for simultaneous faints — that's a design decision.

---

## Real-World Applications

- **Django models** — inheritance + `__init__` for database schemas
- **Game engines** — composition for entities (Player *has* Inventory, Inventory *has* Items)
- **GUI frameworks** — encapsulation for internal widget state
- **pandas DataFrames** — dunder methods powering `+`, `==`, and print formatting

## Official Documentation References

- [Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [`abc` module — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Data Model / Dunder Methods](https://docs.python.org/3/reference/datamodel.html)
- [`property()` built-in](https://docs.python.org/3/library/functions.html#property)

---

*Notes compiled from a hands-on debugging session — every bug above was a real one caught and fixed along the way.*