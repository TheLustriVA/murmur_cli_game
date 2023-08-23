import click

class Starship:
    def __init__(self, name, hull_integrity, shield_strength, energy):
        self.name = name
        self.hull_integrity = hull_integrity
        self.shield_strength = shield_strength
        self.energy = energy

    def __repr__(self):
        return f"{self.name} ({self.hull_integrity} hull, {self.shield_strength} shields, {self.energy} energy)"

    @click.command()
    @click.option("--damage", type=int, help="Amount of damage taken")
    def take_damage(self, damage):
        self.hull_integrity -= damage

    @click.command()
    @click.option("--amount", type=int, help="Amount of energy to recharge")
    def recharge_energy(self, amount):
        self.energy += amount

    @click.command()
    @click.option("--amount", type=int, help="Amount of hull integrity to repair")
    def repair(self, amount):
        self.hull_integrity += amount
