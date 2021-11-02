from django_seed import Seed

from .models import Course
from instructors.models import Instructor

from django.contrib.auth import get_user_model


class CourseSeeder:

    def gen_instructor(self, seeder, student_ids):
        student_id = seeder.faker.random_elements(
            student_ids, length=1, unique=True)

        student_id = student_id[0]
        student = Instructor.objects.get(id=student_id)

        return student

    def seed(self, count):
        seeder = Seed.seeder()

        instructors = Instructor.objects.values_list('id', flat=True)
        instructors = list(instructors)

        seeder.add_entity(Course, count, {
            'instructor_id': lambda x: self.gen_instructor(seeder, instructors),
            'name': lambda x: seeder.faker.sentence(nb_words=4),
            "description": lambda x: seeder.faker.paragraph(nb_sentences=5),
        })

        inserted_pks = seeder.execute()
        return inserted_pks
