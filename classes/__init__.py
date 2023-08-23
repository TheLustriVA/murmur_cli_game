__version__ = "0.0.1"

from .starship import Starship
from .shipsystem import ShipSystem  
from .shiparea import ShipArea 
from .shipcomponent import ShipComponent
from .alienenemy import AlienEnemy
from .crewmember import CrewMember
from .gamecontroller import GameController

__all__ = [
    "Starship",
    "CrewMember",
    "AlienEnemy",
    "ShipComponent",
    "ShipArea",
    "ShipSystem",
    "GameController"
]
