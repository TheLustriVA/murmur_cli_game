import click

class ShipComponent:
    def __init__(self, component_type, location):
        self.component_type = component_type
        self.location = location

    def __repr__(self) -> str:
        return f"{self.component_type} ({self.location})"

    @click.command()
    def damage(self):
        # Implement damage logic here
        pass

    @click.command()
    def repair(self):
        # Implement repair logic here
        pass

    @click.command()
    @click.argument("target_component")
    def reroute_power(self, target_component):
        # Implement power rerouting logic here
        pass
