from django.shortcuts import render
from django.utils.timezone import datetime
from course.models import GACourse


def index(request):
    courses_list = GACourse.objects.order_by('date')[:5]

    context_dict = {}
    context_dict['courses'] = courses_list
    response = render(request, 'course/index.html', context=context_dict)
    return response
