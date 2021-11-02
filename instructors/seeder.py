from django_seed import Seed

from .models import Instructor
from django.contrib.auth import get_user_model


def gen_user_id(seeder, user_ids):
    user_id = seeder.faker.random_elements(user_ids, length=1, unique=True)

    user_id = user_id[0]
    user = get_user_model().objects.get(id=user_id)

    return user


def seed(count):
    seeder = Seed.seeder()

    users = get_user_model().objects.values_list('id', flat=True)
    users = list(users)

    seeder.add_entity(Instructor, count, {
        'user_id': lambda x: gen_user_id(seeder, users),
        "biography": lambda x: seeder.faker.paragraph(nb_sentences=5),
    })

    inserted_pks = seeder.execute()
    return inserted_pks
