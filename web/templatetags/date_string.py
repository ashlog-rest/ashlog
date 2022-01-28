import datetime
from django import template

register = template.Library()

fmt = '%Y-%m-%d %H:%M:%S.%f'


@register.simple_tag()
def date_string(date):
    """ Return a formatted datetime string """
    date_ = datetime.datetime.strptime(date, fmt)
    return date_.strftime('%b %d %H:%M:%S, %Y')
