strong_type_chart: dict[str, list[str]] = {
    'normal': ['none'],
    'fire': ['grass', 'ice', 'bug', 'steel'],
    'water': ['fire', 'ground', 'rock'],
    'electric': ['water', 'flying'],
    'grass': ['water', 'ground', 'rock'],
    'ice': ['grass', 'ground', 'flying', 'dragon'],
    'fighting': ['normal', 'ice', 'rock', 'dark', 'steel'],
    'poison': ['grass', 'fairy'],
    'ground': ['fire', 'electric', 'poison', 'rock', 'steel'],
    'flying': ['grass', 'fighting', 'bug'],
    'psychic': ['fighting', 'poison'],
    'bug': ['grass', 'psychic', 'dark'],
    'rock': ['fire', 'ice', 'flying', 'bug'],
    'ghost': ['psychic', 'ghost'],
    'dragon': ['dragon'],
    'dark': ['psychic', 'ghost'],
    'steel': ['ice', 'rock', 'fairy'],
    'fairy': ['fighting', 'dragon', 'dark']
}

resistance_type_chart: dict[str, list[str]] = {
    'normal': ['none'],
    'fire': ['bug', 'fairy', 'grass', 'ice', 'fire', 'steel'],
    'water': ['water', 'ice', 'fire', 'steel'],
    'electric': ['electric', 'flying', 'steel'],
    'grass': ['grass', 'electric', 'ground', 'water'],
    'ice': ['ice'],
    'fighting': ['dark', 'rock', 'bug'],
    'poison': ['bug', 'fairy', 'fighting', 'grass', 'poison'],
    'ground': ['poison', 'ground'],
    'flying': ['grass', 'fighting', 'bug'],
    'psychic': ['fighting', 'psychic'],
    'bug': ['fighting', 'grass', 'ground'],
    'rock': ['fire', 'normal', 'flying', 'poison'],
    'ghost': ['bug', 'poison'],
    'dragon': ['electric', 'fire', 'water', 'grass'],
    'dark': ['dark', 'ghost'],
    'steel': ['ice', 'rock', 'fairy', 'bug', 'dragon', 'flying', 'grass', 'normal', 'psychic', 'steel'],
    'fairy': ['fighting', 'bug', 'dark']
}

immunity_type_chart: dict[str, list[str]] = {
    'normal': ['ghost'],
    'ghost': ['normal', 'fighting', 'trapping'],
    'steel': ['poison', 'sandstorm', 'toxic'],
    'fairy': ['dragon'],
    'dark': ['psychic', 'prankster'],
    'rock': ['sandstorm'],
    'ground': ['electric', 'sandstorm'],
    'flying': ['ground'],
    'poison': ['toxic'],
    'grass': ['powder'],
    'electric': ['paralysis'],
    'fire': ['burn']
}
