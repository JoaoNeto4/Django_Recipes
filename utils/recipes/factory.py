from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')
#print(signature(fake.random_number))


def make_recipe():
    return {
        'title': fake.random_number(),
        'description': fake.random_number(),
        'preparation_time': fake.sentence(2),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(2),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word(),
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())