import click

class AlienEnemy:
    def __init__(self, size, strength, abilities):
        self.size = size
        self.strength = strength
        self.abilities = abilities

    def __repr__(self):
        return f"{self.size} ({self.strength})"