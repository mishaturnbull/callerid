#!python3
# -*- coding: utf-8 -*-

"""
Graph structure backend.

Almost all the real meat & potatoes of this code is taken largely unaltered
from FloweryK's call-tracer library.  Thank you!!
"""

from edgegraph.structure import Vertex, Universe, singleton
from callerid import util

DEFAULT_UNIVERSE = Universe()

def cb_hashfn(args, kwargs):
    frame = args[0]
    info = util.info(frame)
    name = info['path'] + ':' + info['name']
    return name

class Node (Vertex, metaclass=singleton.semi_singleton_metaclass(cb_hashfn)):

    def __init__(self, frame):
        info = util.info(frame)
        super().__init__(universes=[DEFAULT_UNIVERSE], attributes=info)

        self.frame = frame
        self.fullname = cb_hashfn([frame], None)

    def __repr__(self):
        return f"<CallerID node {self.fullname} @ {hex(id(self))}>"

