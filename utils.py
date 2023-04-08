import json


def load_data():

    with open('list.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    #
    # questions = []
    # for new_quest in data:
    #     questions.append(Question(new_quest['q'], int(new_quest['d']), new_quest['a']))

    return print(data[1])

load_data()