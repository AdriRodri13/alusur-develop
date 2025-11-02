from django import template
from app.utils import get_translated_field

register = template.Library()

@register.filter
def translate_field(obj, field_name):
    """
    Template filter para obtener campos traducidos.
    Uso: {{ objeto|translate_field:"titulo" }}
    """
    return get_translated_field(obj, field_name)
