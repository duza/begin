# -*- coding:utf-8 -*-
# using python 2.7.3
'''File 'in.txt' contents text on english language (including correct 
dates and the amount of money). Program converts dates in 
american format (ex: October 3, 2010) and del extra whitespace
in sums.'''
import re

def month_replace(match):
    '''Function returns name of the month, day and year '''
    dict_months = {1:"January", 2:"February", 3:"March", 4:"April", 
    5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 
    10:"October", 11:"November", 12:"December" }
    value_month = dict_months[int(match.group('month'))]
    value_day = str(int(match.group('day')))
    if len(match.group('year')) == 4:
        value_year = match.group('year')
    elif len(match.group('year')) == 2 and 0<int(match.group('year'))<15:
        value_year = '20'+match.group('year')
    else:
        value_year = '19'+match.group('year')
    return '{month} {day}, {year}'.format(month=value_month, 
        day=value_day, year=value_year)

def money_replace(match):
    '''Function returns the correct amount of money '''
    value_money = ''.join(match.group('money').split(' '))
    return '{money} {br}'.format(money=value_money, br=match.group('BR'))

money_string = re.compile(r"(?P<money>(\d+\s+)+)"
    r"(?P<BR>\bbelarusian roubles\b|\bblr\b)")
date_string = re.compile(r"(?P<day>\d{1,2})(?P<delimiter>[-./])"
    r"(?P<month>\d{1,2})(?P=delimiter)(?P<year>\d{4,4}|\d{2,2})")
with open('in.txt','r+b') as input_file:
    f = input_file.read()
    f = date_string.sub(month_replace,f)
    f = money_string.sub(money_replace,f)
    input_file.seek(0)
    input_file.write(f)