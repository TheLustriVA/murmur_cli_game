import click

class CrewMember:
    def __init__(self, name, role, skills):
        self.name = name
        self.role = role
        self.skills = skills

    def __repr__(self):
        return f"{self.name} ({self.role})"