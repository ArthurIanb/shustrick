from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(name="user_image")
def user_image(target, size=100):
    return mark_safe("<img src={} width={}px height={}px/>".format(target.image.url, size, size))
    