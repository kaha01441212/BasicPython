from math import sin,pi,exp
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

def msekibun(f,a,b,n):
    h = (b-a)/n
    s=0
    l=0
    for i in range(1,n+1):
        l= f(a+(i-1)*h)+f(a+i*h)
        s+=l
    return s*(h/2)

def f(x):
    return sin(x)
print(msekibun(f,0,pi/2,50))

def g(x):
    return 4/(1+x**2)
print(msekibun(g,0,1,100))

def k(x):
    return (pi)**(1/2)*exp(-x**2)
print(msekibun(k,-100,100,1000))
