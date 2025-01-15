from abc import ABC, abstractmethod
from typing import List

class Hero(ABC):
    def __init__(self, name: str, health: int, strength: int) -> None:
        self._name: str = name
        self._health: int = health
        self._strength: int = strength
        self._effects: List['Effect'] = []  # type: ignore
        self._frozen: bool = False
        self._ability_cooldown: int = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def health(self) -> int:
        return self._health

    @property
    def strength(self) -> int:
        return self._strength

    def is_frozen(self) -> bool:
        """Проверяет, заморожен ли герой."""
        return self._frozen

    def freeze(self) -> None:
        """Замораживает героя."""
        self._frozen = True

    def unfreeze(self) -> None:
        """Размораживает героя."""
        self._frozen = False

    def take_damage(self, damage: int) -> None:
        """Наносит урон герою."""
        if self.is_alive():
            self._health -= damage
            if self._health < 0:
                self._health = 0

    def is_alive(self) -> bool:
        """Проверяет, жив ли герой."""
        return self._health > 0

    def add_effect(self, effect: 'Effect') -> None:  # type: ignore
        """Добавляет эффект к герою."""
        self._effects.append(effect)

    def apply_effects(self) -> None:
        """Применяет все активные эффекты к герою."""
        if self.is_alive():
            for effect in self._effects:
                self.take_damage(effect.damage_per_turn)
                effect.duration -= 1
            self._effects = [effect for effect in self._effects if effect.duration > 0]

    @abstractmethod
    def attack(self, opponent: 'Hero') -> None:
        """Абстрактный метод для атаки противника."""
        pass

    @abstractmethod
    def use_ability(self) -> None:
        """Абстрактный метод для использования специальной способности."""
        pass

    @abstractmethod
    def describe(self) -> str:
        """Абстрактный метод для описания героя."""
        pass