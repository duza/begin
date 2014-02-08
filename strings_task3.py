# -*- coding: utf-8 -*-
# using python 2.7.3
''' File input.txt contents the correct Python code. Program removes 
all comments from the source file and saves it to output.txt'''

import re
from contextlib import nested
def replace_comment(match):
    # if match.group(1) :
    #     return match.group(1)
    # else:
    #     return ''
    value = match.group(1) or ''
    return value
comments_pattern = re.compile(r"(([\'\"]).*?\2)|(#.*)")
with nested(open('input.txt','rb'), open('output.txt','wb')) as (input_file, output_file):
    f = input_file.read()
    f = comments_pattern.sub(replace_comment,f)
    output_file.write(f)