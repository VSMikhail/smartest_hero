import requests

from pprint import pprint
def get_super_hero_id(name):
    super_hero_dict = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
    id = 0
    for super_hero in super_hero_dict:
        if super_hero['name'] == name:
            id = super_hero['id']

    if id == 0:
        print('Не верное имя героя:', name)
    return id



def get_super_hero_intelligence(id_number):
    if 0 < id_number < 732:
        super_hero_intelligence = requests.get('https://akabab.github.io/superhero-api/api/powerstats/' + str(id_number) + '.json').json()[
            'intelligence']
        return super_hero_intelligence
    else:
        print('Не верный id:', id_number)
        return 0


def get_super_hero_name(id_number):
    if 0 < id_number < 732:
        super_hero_name = requests.get('https://akabab.github.io/superhero-api/api/id/' + str(id_number) + '.json').json()[
            'name']
        return super_hero_name
    else:
        print('Не верный id:', id_number)
        return 'Нет имени'


names_list = ['Hulk', 'Thanos', 'Captain America']


def compare_super_heroes_by_intelligence(names_list):
    id_numbers =[]
    for name in names_list:
        id_numbers.append(get_super_hero_id(name))
    if 0 in id_numbers:
        print('В списке есть неверное имя!')
    else:
        max_intelligence = 0
        smartest_super_hero_id = 0
        for id_number in id_numbers:
            if get_super_hero_intelligence(id_number) > max_intelligence:
                max_intelligence = get_super_hero_intelligence(id_number)
                smartest_super_hero_id = id_number
        print(
            f'Самый умный герой {get_super_hero_name(smartest_super_hero_id)} с уровнем интелекта {get_super_hero_intelligence(smartest_super_hero_id)}')


compare_super_heroes_by_intelligence(names_list)