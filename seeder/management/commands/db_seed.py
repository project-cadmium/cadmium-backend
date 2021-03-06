from django.core.management.base import BaseCommand

from users.seeder import seed as seed_users

from instructors.seeder import seed as seed_instructors
from courses.seeder import CourseSeeder


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        print('Seeding database:\n')

        print('Users')
        inserted = seed_users(200)
        print(inserted, end='\n\n')

        print('Instructors')
        inserted = seed_instructors(50)
        print(inserted, end='\n\n')

        print('Courses')
        sd = CourseSeeder()
        inserted = sd.seed(300)
        print(inserted, end='\n\n')
