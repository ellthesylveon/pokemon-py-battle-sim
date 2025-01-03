type_list = [
    'normal',
    'fire',
    'water',
    'electric',
    'grass',
    'ice',
    'fighting',
    'poison',
    'ground',
    'flying',
    'psychic',
    'bug',
    'rock',
    'ghost',
    'dragon',
    'dark',
    'steel',
    'fairy',
]

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

# type chart i googled that is useful
expanded_type_chart: dict[str, dict[str, int]] = {
    'normal': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 1.0,
        'flying': 1.0,
        'fighting': 2.0,
        'poison': 1.0,
        'ground': 1.0,
        'rock': 1.0,
        'psychic': 1.0,
        'ice': 1.0,
        'bug': 1.0,
        'ghost': 0.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 1.0
    },
    'fire': {
        'normal': 1.0,
        'fire': 0.5,
        'water': 2.0,
        'grass': 0.5,
        'flying': 1.0,
        'fighting': 1.0,
        'poison': 1.0,
        'ground': 2.0,
        'rock': 2.0,
        'psychic': 1.0,
        'ice': 0.5,
        'bug': 0.5,
        'ghost': 1.0,
        'steel': 0.5,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 0.5,
        'electric': 1.0
    },
    'water': {
        'normal': 1.0,
        'fire': 0.5,
        'water': 0.5,
        'grass': 2.0,
        'flying': 1.0,
        'fighting': 1.0,
        'poison': 1.0,
        'ground': 1.0,
        'rock': 1.0,
        'psychic': 1.0,
        'ice': 0.5,
        'bug': 1.0,
        'ghost': 1.0,
        'steel': 0.5,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 2.0
    },
    'grass': {
        'normal': 1.0,
        'fire': 2.0,
        'water': 0.5,
        'grass': 0.5,
        'flying': 2.0,
        'fighting': 1.0,
        'poison': 2.0,
        'ground': 0.5,
        'rock': 1.0,
        'psychic': 1.0,
        'ice': 2.0,
        'bug': 2.0,
        'ghost': 1.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 0.5
    },
    'flying': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 0.5,
        'flying': 1.0,
        'fighting': 0.5,
        'poison': 1.0,
        'ground': 0.0,
        'rock': 2.0,
        'psychic': 1.0,
        'ice': 2.0,
        'bug': 0.5,
        'ghost': 1.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 2.0
    },
    'fighting': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 1.0,
        'flying': 2.0,
        'fighting': 1.0,
        'poison': 1.0,
        'ground': 1.0,
        'rock': 0.5,
        'psychic': 2.0,
        'ice': 1.0,
        'bug': 0.5,
        'ghost': 1.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 0.5,
        'fairy': 2.0,
        'electric': 1.0
    },
    'poison': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 0.5,
        'flying': 1.0,
        'fighting': 0.5,
        'poison': 0.5,
        'ground': 2.0,
        'rock': 1.0,
        'psychic': 2.0,
        'ice': 1.0,
        'bug': 0.5,
        'ghost': 1.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 0.5,
        'electric': 1.0
    },
    'ground': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 2.0,
        'grass': 2.0,
        'flying': 1.0,
        'fighting': 1.0,
        'poison': 0.5,
        'ground': 1.0,
        'rock': 0.5,
        'psychic': 1.0,
        'ice': 2.0,
        'bug': 1.0,
        'ghost': 1.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 0.0
    },
    'rock': {
        'normal': 0.5,
        'fire': 0.5,
        'water': 2.0,
        'grass': 2.0,
        'flying': 0.5,
        'fighting': 2.0,
        'poison': 0.5,
        'ground': 2.0,
        'rock': 1.0,
        'psychic': 1.0,
        'ice': 1.0,
        'bug': 1.0,
        'ghost': 1.0,
        'steel': 2.0,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 1.0
    },
    'psychic': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 1.0,
        'flying': 1.0,
        'fighting': 0.5,
        'poison': 1.0,
        'ground': 1.0,
        'rock': 1.0,
        'psychic': 0.5,
        'ice': 1.0,
        'bug': 2.0,
        'ghost': 2.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 2.0,
        'fairy': 1.0,
        'electric': 1.0
    },
    'ice': {
        'normal': 1.0,
        'fire': 2.0,
        'water': 1.0,
        'grass': 1.0,
        'flying': 1.0,
        'fighting': 2.0,
        'poison': 1.0,
        'ground': 1.0,
        'rock': 2.0,
        'psychic': 1.0,
        'ice': 0.5,
        'bug': 1.0,
        'ghost': 1.0,
        'steel': 2.0,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 1.0
    },
    'bug': {
        'normal': 1.0,
        'fire': 2.0,
        'water': 1.0,
        'grass': 0.5,
        'flying': 2.0,
        'fighting': 0.5,
        'poison': 1.0,
        'ground': 0.5,
        'rock': 2.0,
        'psychic': 1.0,
        'ice': 1.0,
        'bug': 1.0,
        'ghost': 1.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 1.0
    },
    'ghost': {
        'normal': 0.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 1.0,
        'flying': 1.0,
        'fighting': 0.0,
        'poison': 0.5,
        'ground': 1.0,
        'rock': 1.0,
        'psychic': 1.0,
        'ice': 1.0,
        'bug': 0.5,
        'ghost': 2.0,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 2.0,
        'fairy': 1.0,
        'electric': 1.0,
    },
    'steel': {
        'normal': 0.5,
        'fire': 2.0,
        'water': 1.0,
        'grass': 0.5,
        'flying': 0.5,
        'fighting': 2.0,
        'poison': 0.0,
        'ground': 2.0,
        'rock': 0.5,
        'psychic': 0.5,
        'ice': 0.5,
        'bug': 0.5,
        'ghost': 1.0,
        'steel': 0.5,
        'dragon': 0.5,
        'dark': 1.0,
        'fairy': 0.5,
        'electric': 1.0
    },
    'dragon': {
        'normal': 1.0,
        'fire': 0.5,
        'water': 0.5,
        'grass': 0.5,
        'flying': 1.0,
        'fighting': 1.0,
        'poison': 1.0,
        'ground': 1.0,
        'rock': 1.0,
        'psychic': 1.0,
        'ice': 2.0,
        'bug': 1.0,
        'ghost': 1.0,
        'steel': 1.0,
        'dragon': 2.0,
        'dark': 1.0,
        'fairy': 2.0,
        'electric': 0.5
    },
    'dark': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 1.0,
        'flying': 1.0,
        'fighting': 2.0,
        'poison': 1.0,
        'ground': 1.0,
        'rock': 1.0,
        'psychic': 0.0,
        'ice': 1.0,
        'bug': 2.0,
        'ghost': 0.5,
        'steel': 1.0,
        'dragon': 1.0,
        'dark': 0.5,
        'fairy': 2.0,
        'electric': 1.0
    },
    'fairy': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 1.0,
        'flying': 1.0,
        'fighting': 0.5,
        'poison': 2.0,
        'ground': 1.0,
        'rock': 1.0,
        'psychic': 1.0,
        'ice': 1.0,
        'bug': 0.5,
        'ghost': 1.0,
        'steel': 2.0,
        'dragon': 0.0,
        'dark': 0.5,
        'fairy': 1.0,
        'electric': 1.0
    },
    'electric': {
        'normal': 1.0,
        'fire': 1.0,
        'water': 1.0,
        'grass': 1.0,
        'flying': 0.5,
        'fighting': 1.0,
        'poison': 1.0,
        'ground': 2.0,
        'rock': 1.0,
        'psychic': 1.0,
        'ice': 1.0,
        'bug': 1.0,
        'ghost': 1.0,
        'steel': 0.5,
        'dragon': 1.0,
        'dark': 1.0,
        'fairy': 1.0,
        'electric': 0.5
    }
}

ability_type_chart: dict[str, dict[str, float]] = {
    'bulletproof': {'bullet': 0},
    'dry skin': {'water': 0,
                 'fire': 1.25},
    'earth eater': {'ground': 0},
    #'filter': {'_': _}},
    'flash fire': {'fire': 0},
    'fluffy': {'fire': 2.0,
               'contact': 0.5},
    'heatproof': {'fire': 0.5},
    'levitate': {'ground': 0},
    'lightning rod': {'electric': 0},
    'motor drive': {'electric': 0},
    'punk rock': {'sound': 0.5},
    'sap sipper': {'grass': 0},
    'soundproof': {'sound': 0},
    'storm drain': {'water': 0},
    'thick fat': {'ice': 0.5,
                  'fire': 0.5},
    'water absorb': {'water': 0},
    'water bubble': {'fire': 0.5},
    'well-baked body': {'fire': 0},
    'wind rider': {'wind': 0},
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

