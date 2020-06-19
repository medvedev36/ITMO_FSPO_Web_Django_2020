from django import template
from Core.choices import FUEL_TYPE_CHOICES

register = template.Library()

@register.filter()
def display_type(int_type):
    return FUEL_TYPE_CHOICES[int_type - 1][1]

@register.filter()
def mul(a, b):
    return float(a) * float(b)