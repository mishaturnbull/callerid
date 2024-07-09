#!python3
# -*- coding: utf-8 -*-

"""
Graph structure backend.

Almost all the real meat & potatoes of this code is taken largely unaltered
from FloweryK's call-tracer library.  Thank you!!
"""

import re
from edgegraph.structure import Vertex, Universe, singleton
from callerid import util

DEFAULT_UNIVERSE = Universe()

def cb_hashfn(args, kwargs):
    info = args[0]
    name = info['path'] + ':' + info['name']
    return name

class Node (Vertex, metaclass=singleton.semi_singleton_metaclass(cb_hashfn)):

    def __init__(self, frameinfo):
        super().__init__(universes=[DEFAULT_UNIVERSE], attributes=frameinfo)

        self.fullname = cb_hashfn([frameinfo], None)

    def __repr__(self):
        return f"<CallerID node {self.fullname} @ {hex(id(self))}>"


class TracerConfig (metaclass=singleton.TrueSingleton):

    def __init__(self, filters=None):
        self.filters = filters or []

        for i, raw in enumerate(self.filters):
            self.filters[i] = re.compile(raw)

    def check_filter(self, path):
        for filt in self.filters:
            if filt.search(path):
                return True
        return False

    def should_record_call(self, caller, callee):
        if self.check_filter(cb_hashfn([caller], None)):
            return False
        if self.check_filter(cb_hashfn([callee], None)):
            return False
        return True

