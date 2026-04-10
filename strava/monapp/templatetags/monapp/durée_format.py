from django import template
from datetime import timedelta

register=template.Library()

@register.filter(name='durée_format')
def durée_format(td) :
    secondes_totales=int(td.total_seconds())
    heures=secondes_totales//3600
    minutes=(secondes_totales % 3600)// 60
    return f"{heures}h{minutes}" if minutes>0 else f"{heures}h"