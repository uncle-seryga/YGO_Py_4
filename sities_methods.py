from translate import Translator


def get_all_cities(self):
    data = eval(open('only_cities.json', 'r').read())
    return data


class Translate():
    def converter(self):
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

    def translate_to_english(self, word):
        translator = Translator(from_lang='uk', to_lang='en')  # en_en, us_en, au_en // uk_ua
        text = translator.translate(word)
        return text

    def translate_to_ukrainian(self, word):
        translator = Translator(from_lang='en', to_lang='uk')  # en_en, us_en, au_en // uk_ua
        text = translator.translate(word)
        return text

    def write_to_ua_file(self):
        file = open("cities_ua.json", 'w')
        data = get_all_cities()
        l = []
        for x in data:
            res = self.translate_to_ukrainian(x)
            l.append(res)
            print(f"{x}->{res}")
        file.write(str(l))


class GameMethods:

    def create_session(self, player_id):
        open(f"sessions/{player_id}.json", 'w').write(str({'turn': 1, 'cities': []}))

    def get_session_data(self, player_id):
        return eval(open(f"sessions/{player_id}.json", 'r').read())

    def add_city(self, word, player_id):
        f = eval(open(f"sessions/{player_id}.json", 'r').read())
        f['cities'].append(word)
        f['turn'] = f['turn'] + 1
        open(f"sessions/{player_id}.json", 'w').write(str(f))
