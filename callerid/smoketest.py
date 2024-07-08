#!python3
# -*- coding: utf-8 -*-

"""
Smoketest the call tracer for dev purposes.
"""

from edgegraph.output import pyvis, plantuml
from callerid import tracer, structure

@tracer.traced
def foo(x):
    return bar(x)

def bar(x):
    return baz(x)

def baz(x):
    return x

if __name__ == '__main__':
    foo(7)

    uni = structure.DEFAULT_UNIVERSE
    psrc = plantuml.render_to_plantuml_src(uni, plantuml.PLANTUML_RENDER_OPTIONS)
    plantuml.render_to_image(psrc, 'graph.png')
    pvn = pyvis.make_pyvis_net(uni, rvfunc=repr)
    pvn.show('graph.html', notebook=False)

    from pprint import pprint
    import code; code.interact(local={**locals(), **globals()})

