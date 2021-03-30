from django import template
from film_site.models import Category

register = template.Library()


@register.inclusion_tag('film_site/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}
