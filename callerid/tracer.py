#!python3
# -*- coding: utf-8 -*-

"""
Sys.trace handling.
"""

import functools
import sys
from edgegraph.builder import explicit
from callerid import structure

def tracefunc(frame, event, arg):
    # only care about call and returns
    if event not in ('call', 'return'):
        return

    callee = structure.Node(frame)
    caller = structure.Node(frame.f_back)

    print(f"{caller.name} --> {callee.name}")

    explicit.link_directed(caller, callee)

def run_with_trace(func, *args, **kwargs):
    sys.settrace(tracefunc)
    ret = func(*args, **kwargs)
    sys.settrace(None)
    return ret

def traced(func):
    """
    Decorator to run with trace.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return run_with_trace(func, *args, **kwargs)
    return wrapper

