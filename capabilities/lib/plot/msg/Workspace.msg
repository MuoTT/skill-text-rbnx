# Rectangular drawing workspace in machine millimetres.
#
# Paper frame: x 0..180, y 0..150, +X right, +Y up. Machine zero (0,0,0)
# sits 50 mm above the paper's lower-left corner, so the paper surface is
# z = -50, pen-down z = -50 and pen-up z = -46.
#
# All-zero x/y bounds mean "use the skill config". z_up <= z_down falls
# back to the configured pen heights. Heights must satisfy
# -50 <= z_down < z_up <= 0.
float64 x_min
float64 x_max
float64 y_min
float64 y_max
float64 z_up
float64 z_down