import requests


def get_super_hero_intelligence(id_number):
    super_hero_intelligence = requests.get('https://akabab.github.io/superhero-api/api/powerstats/' + str(id_number) + '.json').json()[
        'intelligence']
    return super_hero_intelligence


def get_super_hero_name(id_number):
    super_hero_name = requests.get('https://akabab.github.io/superhero-api/api/id/' + str(id_number) + '.json').json()[
        'name']
    return super_hero_name


id_numbers_list = [332, 655, 149]


def compare_super_heroes_by_intelligence(id_numbers):
    max_intelligence = 0
    smartest_super_hero_id = 0
    for id_number in id_numbers:
        if get_super_hero_intelligence(id_number) > max_intelligence:
            max_intelligence = get_super_hero_intelligence(id_number)
            smartest_super_hero_id = id_number
    print(
        f'Самый умный герой {get_super_hero_name(smartest_super_hero_id)} с уровнем интелекта {get_super_hero_intelligence(smartest_super_hero_id)}')


compare_super_heroes_by_intelligence(id_numbers_list)
