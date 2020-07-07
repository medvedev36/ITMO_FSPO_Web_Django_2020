from django import template


register = template.Library()


def get_bootstrap_alert(tags):
    return 'danger' if tags == 'error' else tags


register.simple_tag(get_bootstrap_alert, name='get_bootstrap_alert')