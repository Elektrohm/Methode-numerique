# Théo Denis, 17/02/2019, interpolation devoir 2

from numpy import *
from numpy.linalg import solve
import matplotlib.pyplot as plt

n = 4; m = 100
x = (2*pi/(m))*arange(0,m+1)
X = (2*pi/(2*n+1))*arange(0,2*n+1)


def interpolation(X,U,x):
    n = (len(X)-1)//2
    k = array(arange(-n,n+1)).reshape(1,len(X))
    X,x = X.reshape(len(X),1), x.reshape(len(x),1)
    kX,kx = X @ k, x @ k
    Expo_resolution, expo_interpolation = array(exp(1j*kX)), array(exp(1j*kx))
    a_k = solve(Expo_resolution,U)
    return real(expo_interpolation@a_k)


functions = [lambda x : x*(x-2*pi)*exp(-x), 
             lambda x : sin(x)+sin(5*x),
             lambda x : sign(x-2)]
 
for u in functions:
  plt.figure()
  plt.plot(x,u(x),'-b',label='Fonction u')
  U = u(X)
  uh = polyval(polyfit(X,U,len(X)-1),x)
  plt.plot(x,uh,'-g',label='Interpolation polynomiale')
  uh = interpolation(X,U,x)
  plt.plot(x,uh,'-r',label='Interpolation trigonométrique')
  plt.plot(X,U,'ob')
  plt.xlim((-0.2,2*pi+0.2)); plt.ylim((-3,3))
  plt.title('Interpolation trigonométrique : 2n+1 = %d ' % len(X))
  plt.legend(loc='upper right')
  
plt.show() 