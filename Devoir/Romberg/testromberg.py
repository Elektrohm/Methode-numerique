from matplotlib import pyplot as plt
from numpy import *
import time
from romberg import romberg

def u(x):
    return (x*x+x+1)*cos(x)
a = 0
b = pi/2
n = 1

t0 = time.clock()
I,n,errorEst = romberg(u,a,b,n,100,1e-8)
print(time.clock()-t0)
errorExact = abs(2.03819742706724 - I)
print("\n ======= Integral of (x*x+x+1)*cos(x) between 0 and pi/2 = %21.14e " % I)
print(" True error = %14.7e" % errorExact)
print(" Est. error = %14.7e" % errorEst)
print(" Number of intervals = %d" % n)
plt.figure("Mastering the trapezoids integration rule :-)")
x = array([a,b])
plt.plot(x,u(x),'.k',markersize=5)
x = linspace(a,b,200)
plt.fill(append(x,[0]),append(u(x),[0]),'xkcd:sky blue')
x = linspace(-0.5,2.0,300)
plt.plot(x,u(x),'-k')
plt.title('Integrating (x*x+x+1)*cos(x) between 0 and pi/2')
plt.gca().axhline(y=0,color='k',linewidth=1.0)
plt.text(0.1,0.1,"I = %8.6f" % I,fontsize=12)
plt.show()