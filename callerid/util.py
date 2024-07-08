#!python3
# -*- coding: utf-8 -*-

"""
Frame interpretation utilities.

Almost all the real meat & potatoes of this code is taken largely unaltered
from FloweryK's call-tracer library.  Thank you!!
"""

def info(frame):
    # https://github.com/FloweryK/call-tracer/blob/main/calltracer/module.py#L16
    class_name = ''
    if getattr(frame.f_locals, 'self', None) is not None:
        class_name = frame.f_locals['self'].__class__.__name__ + '.'
    elif getattr(frame.f_locals, 'cls', None) is not None:
        cls = frame.f_locals['cls']
        if hasattr(cls, '__name__'):
            class_name = cls.__name__ + '.'

    function_name = frame.f_code.co_name

    return {
            'path': frame.f_code.co_filename,
            'line': frame.f_lineno,
            'name': class_name + function_name,
            'args': frame.f_locals,
        }

def depth(frame):
    # https://github.com/FloweryK/call-tracer/blob/main/calltracer/module.py#L7
    depth = 0
    current = frame
    while current.f_back:
        current = current.f_back
        depth += 1
    return depth

