from django import template

register = template.Library()

@register.filter
def before_underscore(value):
    return value.split('_')[0] if isinstance(value, str) else value
