import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courses.settings')

import django
django.setup()
from course.models import GACourse



def populate():
    gacourses = [{'title': 'Web Application Systems',
                     'date': '2022-04-01', 'description': 'This is the most useful, most valuable and most inspiring course ever! '},
                {'title': 'Software Engineering',
                     'date': '2022-06-01', 'description': 'This course is about good software engineering practices.'}]
    for c in gacourses:
        print(c)

    for course_data in gacourses:
        c = add_course(course_data['title'], course_data['date'], course_data['description'])

    for c in GACourse.objects.all():
        print(c)


def add_course(title, date, description):
    c = GACourse.objects.get_or_create(title=title)[0]
    c.date=date
    c.description = description
    c.save()
    return c

# Start execution


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
