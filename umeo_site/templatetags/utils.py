from django import template
 
 
register = template.Library()
 
@register.filter(name="next_point")
def multipliy(value, args):
    return value * value * args