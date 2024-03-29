from django import template

register = template.Library()

page_menu = {
    'Home Page': 'articles:index',
    'Creation Page': 'articles:create',
}

@register.inclusion_tag("templatetags/menu.html", name='menu')
def menu(choosen_ref):
    return {'menu': page_menu, 'choosen_ref': choosen_ref}
