# Author:  Federico Cañellas
# Email:   federico.leandro.c@gmail.com
# Date:    17-08-2019
# Version: 0.1
# Purpose: Utilities for work with os.argv

from console import error
from sys import argv

def mqty(min):
    """Test arguments minimun quantity and show and error message if necessary"""
    if len(argv) < min:
        error("Not enough arguments")
    
    return len(argv) >= min

def get(key, separator=':'):
    """Get an argument value --argument:value"""

    if key != '':
        for item in argv:
            if key in item and test_format(item, separator):
                return item.split(separator)[1]
    
    return None

def match(key):
    """Match a single boolean argument without a value"""

    if key != '':
        for item in argv:
            if key == item:
                return True

    return False

def test_format(pair, separator):
    """Test a key and value pair against separator format"""

    if not separator in pair:
        error("Argument format must be key%svalue format" % separator)

    return separator in pair