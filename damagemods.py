

spread: float = 0.75
weather_boost: float = 1.5
glaive_rush_boost: int = 2
critical_hit: float = 1.5
same_type: float = 1.5
adaptability: int = 2
effectiveness: dict[str, float | int] = {
    'immune': 0,
    'double resistance': 0.25,
    'resistance': 0.5,
    'normal': 1,
    'weak': 1.5,
    'double weak': 2
}
