from django import template
from datetime import datetime
register = template.Library()



def lastDayAdded(context,value):
    productDay=str(value.inDate)
    todayIs =str(datetime.today().strftime('%Y-%m-%d'))

    if todayIs == productDay:


        context['sonGun']=True
    else:

        context['sonGun']=False
    return ''
register.simple_tag(takes_context=True)(lastDayAdded)