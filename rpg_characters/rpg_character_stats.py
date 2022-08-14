from random import randint

attacker = {

    'HP:': 125,
    'MP': 25,
    'STR': 13,
    'VIT': 12,
    'DEX': 9,
    'AGI': 9,
    'INT': 7,
    'MND': 6,
    'LUCK': randint(4, 9),
    'SPECIAL': 'critical hits allow attacker to attack again',
    'SKILLS': ['Bludgeon', 'Attack-up All', 'Multi-Attack']

    }

defender = {

    'HP:': 142,
    'MP': 62,
    'STR': 11,
    'VIT': 17,
    'DEX': 10,
    'AGI': 7,
    'INT': 8,
    'MND': 11,
    'LUCK': randint(5, 10),
    'SPECIAL': '15% chance damage is reduced by 30%',
    'SKILLS': ['Provoke', 'Defense-up all', 'Invincibility']

    }

healer = {

    'HP:': 95,
    'MP': 125,
    'STR': 7,
    'VIT': 6,
    'DEX': 8,
    'AGI': 10,
    'INT': 11,
    'MND': 15,
    'LUCK': randint(6, 13),
    'SPECIAL': '5% chance that all tiers of cure spells consume 0 MP',
    'SKILLS': ['Cure I through V', 'Remedies to all ailments', 'resurrection']

    }

magician = {

    'HP:': 102,
    'MP': 137,
    'STR': 5,
    'VIT': 5,
    'DEX': 6,
    'AGI': 12,
    'INT': 15,
    'MND': 11,
    'LUCK': randint(3, 7),
    'SPECIAL': '1/10 of all damage is converted into MP',
    'SKILLS': ['Dual-cast', 'Recharge-MP', 'Witchcraft-necromancy familiar']
    }

monk = {

    'HP:': 150,
    'MP': 0,
    'STR': 13,
    'VIT': 15,
    'DEX': 11,
    'AGI': 9,
    'INT': 7,
    'MND': 7,
    'LUCK': randint(3, 7),
    'SPECIAL': 'physical attack twice per turn',
    'SKILLS': ['Style-change Chong-Ji', 'Bare Knuckle exchange', 'Dogfight']

    }

