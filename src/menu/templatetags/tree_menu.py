from django import template
from django.template import RequestContext

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(
    context: RequestContext,
    slug_menu: str = '',
    item_id: None | int = None
):
    if item_id is not None and 'menu' in context:
        data = context['menu']
    else:
        data = MenuItem.objects.select_related().filter(
            category__slug=slug_menu
        ).order_by('pk')
    return {
        'menu': data,
        'current_menu': (item for item in data if item.parent_id == item_id),
        'slug': context['slug']
    }
