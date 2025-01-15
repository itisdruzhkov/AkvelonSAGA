from heroes.hero import Hero

class Effect:
    def __init__(self, name: str, duration: int, damage_per_turn: int) -> None:
        self.name: str = name
        self.duration: int = duration
        self.damage_per_turn: int = damage_per_turn

    def apply(self, target: 'Hero') -> None:
        target.add_effect(self)