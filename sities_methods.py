from translate import Translator


def converter():
    """
    Need to be run before 1-st play
    :return:
    """
    cities = []
    f = open('only_cities.json', 'w')
    cities_json = eval(open('cities.json', 'r').read())
    for x in cities_json:
        cities.append(x['name'])
    f.write(str(cities))


def translate_to_english(word):
    translator = Translator(from_lang='uk', to_lang='en')  # en_en, us_en, au_en // uk_ua
    text = translator.translate(word)
    return text


def get_all_cities():
    data = eval(open('only_cities.json', 'r').read())
    return data


def create_session(player_id):
    open(f"sessions/{player_id}.json", 'w').write(str([]))


def get_session_data(player_id):
    return eval(open(f"sessions/{player_id}.json", 'r').read())
