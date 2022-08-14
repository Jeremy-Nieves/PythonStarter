from random import randint
from rpg_character_stats import attacker, defender, healer, monk, magician

party_members = []


def create_party(size=1):

    i = 0
    while i < size:
        set_job = randint(1, 5)

        if set_job == 1:
            rpg_class = 'attacker'
            print('Attacker has the following base stats:')
            for k, v in attacker.items():
                print(k, v)

        elif set_job == 2:
            rpg_class = 'defender'
            print('\nDefender has the following base stats:')
            for k, v in defender.items():
                print(k, v)

        elif set_job == 3:
            rpg_class = 'magician'
            print('\nMagician has the following base stats: ')
            for k, v in magician.items():
                print(k, v)

        elif set_job == 4:
            rpg_class = 'monk'
            print('\nMonk has the following base stats: ')
            for k, v in monk.items():
                print(k, v)

        else:
            rpg_class = 'healer'
            print('\nHealer has the following base stats: ')
            for k, v in healer.items():
                print(k, v)

        new_member = [rpg_class]
        party_members.append(new_member)
        i += 1


create_party(3)
print('\nYour party consists of the following roles: ')
print(party_members)


def name_party():
    name_player_1 = input('What will you name your first party member: ')
    party_members[0] = name_player_1

    name_player_2 = input('What will you name your second party member: ')
    party_members[1] = name_player_2

    name_player_3 = input('What will you name your third party member: ')
    party_members[2] = name_player_3

    print(party_members)

name_party()
