CallerID
========

CallerID is a Python call tracing utility designed to capture *actual usage* of
a program as it runs.  It should, therefore, be impervious to the usual "call
tracer of a duck-typed language" drawbacks.

This is A.) somewhat a proof-of-concept; I'm not 100% sure the idea will work
until I try it, and B.) designed to work closely with [edgegraph][1].

Credit
------

Credit for the idea behind this utility (using Python's sys.settrace) goes to
GitHub user FloweryK, specifically the `call-tracer` project.  [Check it
out here!][2]

[1]: https://github.com/mishaturnbull/edgegraph
[2]: https://github.com/FloweryK/call-tracer

