

POUND = {
    'name': 'Pound',
    'power': 40,
    'accuracy': 100,
    'type_': 'normal',
    'category': 'physical',
    'power_points': 56,
    'priority': 0,
    'flags': [],
    'boost_amount': [0, 0, 0, 0, 0],
    'boost_category': '',
}

PROTECT = {
    'name': 'Protect',
    'power': 0,
    'accuracy': 100,
    'type_': 'normal',
    'category': 'status',
    'power_points': 16,
    'priority': 4,
    'flags': ['protects'],
    'boost_amount': [0, 0, 0, 0, 0],
    'boost_category': '',
}

PSYCHIC = {
    'name': 'Psychic',
    'power': 90,
    'accuracy': 100,
    'type_': 'psychic',
    'category': 'special',
    'power_points': 16,
    'priority': 0,
    'flags': [],
    'boost_amount': [0, 0, 0, 0, 0],
    'boost_category': '',
}

EARTHQUAKE = {
    'name': 'Earthquake',
    'power': 100,
    'accuracy': 100,
    'type_': 'ground',
    'category': 'special',
    'power_points': 16,
    'priority': 0,
    'flags': [],
    'boost_amount': [0, 0, 0, 0, 0],
    'boost_category': '',
}

FEINT = {
    'name': 'Feint',
    'power': 30,
    'accuracy': 100,
    'type_': 'normal',
    'category': 'physical',
    'power_points': 16,
    'priority': 2,
    'flags': ['breaks_protect'],
    'boost_amount': [0, 0, 0, 0, 0],
    'boost_category': '',
}

THUNDER_WAVE = {
    'name': 'Thunder Wave',
    'power': 0,
    'accuracy': 90,
    'type_': 'electric',
    'category': 'status',
    'power_points': 32,
    'priority': 0,
    'flags': ['paralysis'],
    'boost_amount': [0, 0, 0, 0, 0],
    'boost_category': '',
}

SWORDS_DANCE = {
    'name': 'Swords Dance',
    'power': 0,
    'accuracy': 101,
    'type_': 'normal',
    'category': 'status',
    'power_points': 32,
    'priority': 0,
    'flags': ['stat_boost'],
    'boost_amount': [1.0, 0, 0, 0, 0],
    'boost_category': 'attack sharply rose!',
}

NASTY_PLOT = {
    'name': 'Nasty Plot',
    'power': 0,
    'accuracy': 101,
    'type_': 'dark',
    'category': 'status',
    'power_points': 32,
    'priority': 0,
    'flags': ['stat_boost'],
    'boost_amount': [0, 0, 1.0, 0, 0],
    'boost_category': 'special attack sharply rose!',
}
