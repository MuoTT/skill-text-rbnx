# Codegen mirror — must match
# primitive-hdu-cartesian-plotter-rbnx/capabilities/lib/plotter/msg/Waypoint.msg.
#
# Absolute machine position in millimetres. z encodes pen state:
# z_down = -50 (pen on paper), z_up = -46 (pen lifted). The PLC has no
# per-point motion profile; set the global profile with SET_PARAM first.
float64 x
float64 y
float64 z