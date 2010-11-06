from django import template

register = template.Library()

@register.filter
def dictget(dictionary, key):
    try:
        return dictionary.get(key,'')
    except:
        return ''

@register.filter
def listitem(li, index):
    try:
        return li[index]
    except:
        return ''

@register.filter
def intpercent(value):
    try:
        value = int(value)
    except:
        pass
    try:
        if value > -101 and value < 101:
            return '%d%%' % value
    except:
        pass
    return ''


@register.filter
def parse_int(value):
    try:
        value = int(value)
    except:
        pass
    try:
        if value or value == 0:
            return value
    except:
        pass
    return ''
