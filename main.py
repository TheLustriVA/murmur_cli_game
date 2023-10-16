from classes import Starship, CrewMember, AlienEnemy, ShipComponent, ShipArea, ShipSystem, GameController
from rich import print
from rich.console import Console

console = Console(color_system="auto")


def main():
    # Initialize instances of each class
    starship = Starship("USS Enterprise", 100, 80, 200)
    crew_member = CrewMember("James Kirk", "Captain", ["Leadership", "Tactical"])
    alien_enemy = AlienEnemy("Large", "High", ["Telekinesis", "Energy Blast"])
    ship_component = ShipComponent("Engine", "Aft")
    ship_area = ShipArea("Engineering", ["Reactor Core", "Capacitors", "Warp Drive"])
    ship_system = ShipSystem("Propulsion", "Zodiac Class Penrose Void-Impeller", 200)
    game_controller = GameController()

    # Perform actions or interactions here to test functionality
    console.print(f"[bold magenta on white]{starship}[/bold magenta on white]")
    console.print(f"[bold magenta]{crew_member}[/bold magenta]")
    console.print(f"[bold]{ship_area}[/bold]")
    console.print(f"[bold]{ship_system}[/bold]")
    console.print(f"[bold]{ship_component}[/bold]")
    console.print(f"[bold]{alien_enemy}[/bold]")
    console.print(f"[bold]{game_controller}[/bold]")

if __name__ == "__main__":
    main()
