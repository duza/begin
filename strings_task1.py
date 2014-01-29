#-*- coding:utf-8 -*-
#using python 2.7.3
''' This program calculates sum of values in all lines on which 
indicates the first element of the string. Strings are in the file 
".csv". '''
from os.path import getsize
# if file is not empty
if getsize('in.csv')>0: 
    #   Open file 'in.csv' for reading and create list of strings
    f = open('in.csv')
    input_data = f.read().split('\n')
    # create a new list for elements
    elements, errors = [], 0
    # the resulting string to output
    result = ''
    for line in input_data:
        # splitting string on values
        line = line.split(';')    
        try:
            # find index of the value for addition to summ
            index = int(line[0])
            #  added value in list 'elements'
            elements.append(float(line[index].replace(',', '.')))
            if elements[-1] > 0:
                result += ' + {}'.format(str(elements[-1]).replace('.',','))
            elif elements[-1] < 0:
                result += ' - {}'.format(\
                    str(abs(elements[-1])).replace('.',','))
            else:
                result += ' + 0,0'
        except Exception:
            errors += 1
            elements.append(0)
    # del excess chars in start of the line result
    if result.startswith(' - ') :
        result = '-'+result[3:]
    elif result.startswith(' + '):
        result = result[3:]
    print 'result({0}) = {1}'.format(result ,\
     str(round(sum(elements),2)).replace('.',',') )
    print "error-lines = {}".format(errors)
    f.close()
else:
    print "Sorry.File is empty."