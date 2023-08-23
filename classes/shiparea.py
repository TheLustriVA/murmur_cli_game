import click

class ShipArea:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def __repr__(self) -> str:
        return f"{self.name} ({len(self.components)} components)"