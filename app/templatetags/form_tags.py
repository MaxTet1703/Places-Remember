from django import template

register = template.Library()


@register.inclusion_tag("templatetags/form.html", takes_context=True)
def render_places_form(context, do, data=None):
    result = {
        'url': context["request"].path,
        'do': do,
    }
    if data:
        result["data"] = data
    return result