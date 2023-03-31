"""
Напишите класс Character обладающий 3 характеристиками: атака, здоровье, уклоенине
FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

Класс имеет следующие методы:
Распределение атрибутов как описано выше: character_1 = Character("fighter")
Атака
Получение урона в случае если увернуться не удалось.
Уклонение: каждое очко уклонения умножается на 5. Результат уклонения зависит от рандомно генерируемого числа
от 0 до 100. Если это число меньше или равно навыка уклонения, то герой уклоняется от атаки.
Смерть: если здоровье меньше 1.

Напишите функцию которая заставит сразиться разных героев друг с другом 100 раз. Выведите счет.
"""
import random

FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

class Character:

    _health = 0
    _attack = 0
    _dodge = 0

    def __init__(self, char_type):
        self._char_type = char_type
        self._assign_attributes()

    def __str__(self):
        return self._char_type

    def _assign_attributer(self):
        types_dict = TYPES[self._char_type]
        self._health = types_dict['health']
        self._attack = types_dict['attack']
        self._dodge = types_dict['dodge']

    def attack(self):
        return self._attack

    def take_damage(self):
        if self._dodge_succes():
            return "Missed!"
        self._health -= damage
        return f"{self._char_type} took {damage} damage."

    def _dodge_succes(self):
        dodge_chance = self._dodge * 5
        dodge_roll = random.randint(1, 100)
        if dodge_chance >= dodge_roll:
            return True
        return False

    def is_dead(self):
        return self._health < 1

def character_fight(type1, type2):






