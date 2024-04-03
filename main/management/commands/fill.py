from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'John', 'first_name': 'Smit'},
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Ivanov', 'first_name': 'Ivan'},
            {'last_name': 'Aleksandrov', 'first_name': 'Aleksand'}
        ]
        students_for_crate = []
        for student_item in student_list:
            students_for_crate.append(Student(**student_item))

        Student.objects.bulk_create(students_for_crate)
        # for student_item in student_list:
        #     Student.objects.create(**student_item)
