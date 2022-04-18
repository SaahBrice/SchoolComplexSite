from django import template
from account.models import CustomUser, Teachers, Classes, Subjects, Students, Academic_years



register = template.Library()


@register.filter(name = 'number')
def number(value):
    test= int(value)
    quantity = 0
    classehere = Classes.objects.get(id=test)
    studentsheres= Students.objects.all()
    for studentshere in studentsheres:
        if classehere.name == studentshere.classs.name:
            quantity = quantity+1

    return quantity

@register.filter(name = 'count')
def count(value):
    quantity = value.count()
    return quantity

@register.filter()
def to_int(value):
    value = float(value) + 0
    return value
