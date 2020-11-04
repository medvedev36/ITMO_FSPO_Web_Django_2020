from django import template
from datetime import datetime

from tickets.choices import PAYMENT_TYPE_CHOICE, USER_TYPE_CHOICE

register = template.Library()


def datetime_sub(a, b):
    res = (a - b).seconds
    h, m = res // 3600, res // 60 % 60
    return '{}ч. {}м.'.format(h, m)

def sub(a, b):
    return a - b

def payment_converter(payment_type):
    return PAYMENT_TYPE_CHOICE[payment_type - 1][1]

def user_type_converter(payment_type):
    return USER_TYPE_CHOICE[payment_type - 1][1]

def modulo(num, val):
    return num % val

def division(num, val):
    return num // val

register.filter('datetime_sub', datetime_sub)
register.filter('sub', sub)
register.filter('payment_converter', payment_converter)
register.filter('user_type_converter', user_type_converter)
register.filter('division', division)