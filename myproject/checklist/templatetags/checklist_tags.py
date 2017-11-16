from django import template

register = template.Library()

# Adds specified class to attribute for html/css
@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})