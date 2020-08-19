# Author:  Francisca Cañellas
# Email:   francisca.leonor.alejandra.c@gmail.com
# Date:    17-08-2019
# Version: 0.1
# Purpose: Utilities for test Python version at runtime

from console import error
from re import sub
from sys import version_info, version

def __get_version_integer(v=version_info):
    """Get 3 digits integer from sys.version_info"""

    # FIX LENGTH WITH ZEROS
    if len(v) < 3:
        v = v + [0] * (3 - len(v))

    return v[0] * 100 + v[1] * 10 + v[2]

def get_version(minor=True, micro=True):
    """Get Python version string"""

    version = str(version_info[0])

    if minor:
        version += '.' + str(version_info[1])
    
    if minor and micro:
        version += '.' + str(version_info[2])

    return version

def test(min_v=None):
    """Test a minimun version for Python
    
    min_v:str|int

    Version format must include major, micro and minor if posible
    Example:
    - mayor: 2
    - mayor + minor: 2.7 | 27
    - mayor + minor + micro: 2.7.3 | 273
    """

    if not min_v:
        raise Exception("I need a minimun Python version for test!")
    
    # PARSE VERSION
    if isinstance(min_v, str):
        min_v = int(sub("[\.]+", '', min_v))

    v_test = __get_version_integer() >= min_v

    if not v_test:
        error("I need Python +%s" % get_version())

    return v_test
