# -*- coding: utf-8 -*-
# using python 2.7.3
''' File in.txt is correct file its contains real 
coordinates of segments on the plane (one segment per line) 
in the format: (x1;y1) (x2;y2). Program creates a list of 
the form (len; num), where len - the length of segment, 
rounded to an integer value, and num - number of segments of 
such length. In output happens sorting the list by descending
(high to low) num.'''
import re
from collections import Counter

#pattern for search coordinates of float numbers
coordinats_pattern = re.compile(r'[(]\s*([-]?\d+(?:\,\d+)?(?:[eE][+-]\d+)?)\s*'
    r';\s*([-]?\d+(?:\,\d+)?(?:[eE][+-]\d+)?)\s*[)]\s*'
r'[(]\s*([-]?\d+(?:\,\d+)?(?:[eE][+-]\d+)?)\s*;'
    r'\s*([-]?\d+(?:\,\d+)?(?:[eE][+-]\d+)?)\s*[)]')
obj_count_len = Counter()
with open('in.txt','rb') as f:
    for line in f:
        tuple_coors = tuple(map(float,(el.replace(',','.') for el in coordinats_pattern.findall(line)[0])))
        len_segment = ((tuple_coors[0]-tuple_coors[2])**2 + (tuple_coors[1]-tuple_coors[3])**2)**.5
        obj_count_len[round(len_segment)] += 1
for tup in obj_count_len.most_common():
    print '{0:.0f};{1}'.format(*tup)