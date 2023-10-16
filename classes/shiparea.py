import click

class ShipArea:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def __repr__(self) -> str:
        return f"{self.name} ({len(self.components)} components)"

class Quarters(ShipArea):
    def __init__(self, name, components, room_type):
        super().__init__(name, components)
        self.room_type = room_type

class Bay(ShipArea):
    def __init__(self, name, components, purpose):
        super().__init__(name, components)
        self.purpose = purpose

class Laboratory(ShipArea):
    def __init__(self, name, components, research_field):
        super().__init__(name, components)
        self.research_field = research_field

class Hold(ShipArea):
    def __init__(self, name, components, capacity):
        super().__init__(name, components)
        self.capacity = capacity

class Mess(ShipArea):
    def __init__(self, name, components, meal_type):
        super().__init__(name, components)
        self.meal_type = meal_type
