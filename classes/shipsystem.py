import click

class ShipSystem:
    def __init__(self, system_type, system_name, energy_consumption):
        self.system_name = system_name
        self.system_type = system_type
        self.energy_consumption = energy_consumption

    def __repr__(self):
        return f"{self.system_type}: {self.system_name}"

    @click.command()
    def activate(self):
        # Implement activation logic here
        pass

    @click.command()
    def deactivate(self):
        # Implement deactivation logic here
        pass
