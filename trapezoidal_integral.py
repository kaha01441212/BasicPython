from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
s = 0
l = 0
import math
a = 0
b = math.pi/2
n = 100
h = (b-a) / n
for k in range(1, n+1):
    l = ((sin(a + (k - 1) * h)) + (sin(a + k * h))) 
    s += l*(h/2)
print(s)
