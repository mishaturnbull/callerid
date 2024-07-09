#!python3
# -*- coding: utf-8 -*-

"""
Sys.trace handling.
"""

import functools
import sys
import threading
from edgegraph.builder import explicit
from callerid import structure, util

def tracefunc(frame, event, arg):
    # only care about call events
    if event != 'call':
        return

    calleeinfo = util.info(frame)
    callerinfo = util.info(frame.f_back)

    if not structure.TracerConfig().should_record_call(callerinfo, calleeinfo):
        return

    callee = structure.Node(calleeinfo)
    caller = structure.Node(callerinfo)

    print(f"{caller.name} --> {callee.name}")

    explicit.link_directed(caller, callee)

def run_with_trace(func, *args, **kwargs):

    # make sure threading.settrace goes on the outside of sys.settrace --
    # otherwise we'll capture the threading internals of setting a trace, if
    # there are any
    threading.settrace(tracefunc)
    sys.settrace(tracefunc)

    ret = func(*args, **kwargs)

    sys.settrace(None)
    threading.settrace(None)

    return ret

def traced(func):
    """
    Decorator to run with trace.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return run_with_trace(func, *args, **kwargs)
    return wrapper

