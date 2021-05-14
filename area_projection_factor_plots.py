import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def projected_angle_fac_park_tuller(theta, mode="both"):
    # mode: standing, walking, both

    # Park, S., & Tuller, S. E. (2011). Human body area factors for radiation exchange analysis: standing and walking postures. International journal of biometeorology, 55(5), 695-709.

    # Mean of Standing posture:
    # y = 3.01E-07x3 - 6.46E-05x2 + 8.34E-04x + 0.298
    # R² = 0.9998
    # Mean of Walking posture:
    # y = 3.67E-07x3 - 6.74E-05x2 + 8.49E-04x + 0.297
    # R² = 0.9996
    # Mean of Standing and Walking postures:
    # y = 3.34E-07x3 - 6.60E-05x2 + 8.42E-04x + 0.297
    # R² = 0.9997

    x = theta
    y = 0

    if mode == "both":
        y = 3.34E-07 * x ** 3 - 6.60E-05 * x ** 2 + 8.42E-04 * x + 0.297
    elif mode == "standing":
        y = 3.01E-07 * x ** 3 - 6.46E-05 * x ** 2 + 8.34E-04 * x + 0.298
    elif mode == "walking":
        y = 3.67E-07 * x ** 3 - 6.74E-05 * x ** 2 + 8.49E-04 * x + 0.297

    return y


def projected_angle_fac_matzarakis(theta):
    # Staiger, H., & Matzarakis, A. (2020). Accuracy of Mean Radiant Temperature Derived from Active and Passive Radiometry. Atmosphere, 11(8), 805.
    # https://www.mdpi.com/2073-4433/11/8/805/htm#B11-atmosphere-11-00805
    return 0.308 * math.cos(theta * (0.998 - (theta ** 2 / 50000)))


def projected_cylinder_area(theta, r, h):
    # From scratch:
    # Consider a cylinder of radius r and height h rotated with respect to the flow direction of a fluid by  about an axis parallel to the base. The frontal area of the cylinder is the area perpendicular to the flow direction. If this shape is projected onto the 2D plane, the resulting 2D area is pi r^2 sin theta + 2 r h cos theta
    # Test: For a cylinder with r = 1 and h = 2 this should be
    # A = 2*1 = 2 m^2 for theta = 90°
    # A = r^2 * PI = 3.14 m^2 for theta = 0°
    # PI*r*2*sin(B) + 2*r*h*cos*(B)
    diameter = 2 * r
    return math.pi * r ** 2 * math.sin(theta) + diameter * h * math.cos(theta)


h = 2
r = 0.3

cyl_surf_area = 2 * r ** 2 * math.pi + 2 * r * math.pi * h

blueish = (0 / 255, 127 / 255, 255 / 255)
magenta = (247 / 255, 60 / 255, 124 / 255)
teal = (23 / 255, 142 / 255, 146 / 255)

colors = [blueish, magenta, teal]

dims = (6, 3)
fig, ax = plt.subplots(figsize=dims)

size = 4

for theta in range(0, 90, 1):
    rad = np.deg2rad(theta)
    sa = projected_cylinder_area(rad, r, h)
    am = projected_angle_fac_matzarakis(rad)

    # Normalize this one by cylinder surface area

    plt.scatter(theta, sa / cyl_surf_area, color=colors[0], s=size, )
    # Matzarakis equation
    plt.scatter(theta, am, color=colors[1], s=size, )

    # Park, S., & Tuller
    mode = ["both", "standing", "walking"]
    colors2 = ["darkcyan", "darkslategray", "cyan"]

    for i in zip(mode, colors2):
        apt = projected_angle_fac_park_tuller(theta, i[0])
        plt.scatter(theta, apt, color=i[1], s=size, )

ax.legend(["Simple Cylinder Approach",
           "Matzarakis (2020)",
           "Park & Tuller (2011) - Both",
           "Park & Tuller (2011) - Standing",
           "Park & Tuller (2011) - Walking"])
ax.set(xlim=(0, 90), ylim=(0, 0.35))
ax.set_ylabel("Area Projection Factor")
ax.set_xlabel("Azimuth [°]")
plt.tight_layout()
plt.savefig("Area_Projection_Factor_Plot.pdf")
plt.savefig("Area_Projection_Factor_Plot.png", dpi=600)

plt.show()
