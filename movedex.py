
class Move:
    def __init__(self, name: str, power: int, accuracy: int, types: str,
                 category: str, power_points):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.types = types
        self.category = category
        self.power_points = power_points

POUND: Move = Move('Pound', 40, 100, 'normal', 'physical', 56)
MEGA_PUNCH: Move = Move('Mega Punch', 80, 85, 'normal', 'physical', 35)
HYPER_VOICE: Move = Move('Hyper Voice', 90, 100, 'normal', 'special', 16)
BOOMBURST: Move = Move('Boomburst', 140, 100, 'normal', 'special', 16)
DARK_PULSE: Move = Move('Dark Pulse', 80, 100, 'dark', 'special', 24)