import sities_methods


def if_city(player_city):
    if sities_methods.translate_to_english(player_city) in sities_methods.get_all_cities():
        print(f'Rule 1 Check. {player_city} is a city')
        return True
    else:
        print(f'Rule 1 Fail. {player_city} is not a city')
        return False


def if_not_played(player_id, player_city):
    if player_city in sities_methods.get_session_data(player_id):
        print(f'Rule 2 Fail. {player_city} was played before')
        return False
    else:
        print(f'Rule 2 Check. {player_city} is unique')
        return True


def if_last_letter(player_city: str, previous_city: str):
    letter = -1
    if previous_city[-1] == 'ь':
        letter = -2
    if player_city[0].title() == previous_city[letter].title():
        print(f'Rule 3 Check {player_city[0].title()}={previous_city[letter].title()}')
        return True
    else:
        print(f'Rule 3 Fail {player_city[0].title()}!={previous_city[letter].title()}')
        return False


def if_valid(word, player_id):
    result = [if_city(word), if_not_played(player_id, word),
              if_last_letter(word, sities_methods.get_session_data(player_id)['cities'][-1])]
    if result.count(True) == 3:
        sities_methods.add_city(word, player_id)



if_valid("вільнюс", 431008303)
