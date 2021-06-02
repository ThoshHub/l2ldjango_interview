from django import template
import datetime

register = template.Library()

def l2l_dt(date_val):

    if(isinstance(date_val, str)): # if string, convert it into date object and return proper format
        date_time_obj = datetime.datetime.strptime(date_val, "%Y-%m-%dT%H:%M:%S")
        return date_time_obj.strftime('%Y-%m-%d %H:%M:%S')
    else: # otherwise, return proper format
        return date_val.strftime('%Y-%m-%d %H:%M:%S')

register.filter('l2l_dt', l2l_dt)