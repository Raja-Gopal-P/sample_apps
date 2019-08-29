from django import template


register = template.Library()


@register.filter
def empty_filter(obj, value):
    if not obj:
        return value
    return obj
