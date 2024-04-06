from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
s = 0
import math
h = math.pi / (2 * 100)
for k in range(1, 101):
    l = ((sin((k - 1) * h)) + (sin(k * h))) * 2 / h
    s += l
print(s)

