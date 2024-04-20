from django import template

from ..forms import PlacesForm

register = template.Library()


@register.inclusion_tag("templatetags/form.html", takes_context=True)
def render_places_form(context, do):
    return {
        'form': PlacesForm,
        'url': context["request"].path,
        'do': do
    }