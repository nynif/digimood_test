# Space Defense
# 26/07/2023, by Antoine Boutet

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __str__(self):
		return f'({self.x}, {self.y})' 

# Major 
class Vessel:
    def __init__(self, major_type):
        self.major_type = major_type

    def move_to(self, point: Point):
        pass  # Implement movement to given coordinates

# SupportCraft is a MAJOR TYPE
class SupportCraft(Vessel):
    def __init__(self, type):
        super().__init__("support_craft")
        self.medical_unit = True
        self.type = type

    def execute_order(self):
        # If there is sharing action when executing a order, it will be here
        pass 

# Definition of all subtype for SupportCraft
class Refueling(SupportCraft):
    def __init__(self):
        super().__init__("refueling")

    def execute_order(self):
        # Define here specif action
        pass

class MechanicalAssistance(SupportCraft):
    def __init__(self):
        super().__init__("mechanical_assistance")

    def execute_order(self):
        # Define here specif action
        pass

class Cargo(SupportCraft):
    def __init__(self):
        super().__init__("cargo")

    def execute_order(self):
        # Define here specif action
        pass

# OffensiveCraft is a MAJOR TYPE
class OffensiveCraft(Vessel):
    def __init__(self, type, cannons):
        super().__init__("offensive_craft")
        self.cannons = cannons
        self.is_command_ship = False
        self.type = type

    def attack(self):
        pass  # Attack will fire all cannons

    def raise_shields(self):
        pass  # Implement raising shields

# Definition of all subtype for OffensiveCraft

class Cruiser(OffensiveCraft):
    def __init__(self):
        super().__init__("Cruiser", 12)

class Destroyer(OffensiveCraft):
    def __init__(self):
        super().__init__("Destroyer", 6)

class Battleship(OffensiveCraft):
    def __init__(self):
        super().__init__("Battleship", 24)

class CommandShip(Battleship):
    # We can have only ONE CommandShip
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            raise Exception("We can have only one CommandShip")
        cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.is_command_ship = True

### commande to create Vessel: 
# refueling = Refueling()
# mechanical_assist = MechanicalAssistance()
# cargo = Cargo()
# cruiser = Cruiser()
# destroyer = Destroyer()
# battleship = Battleship()
# commandship = CommandShip()