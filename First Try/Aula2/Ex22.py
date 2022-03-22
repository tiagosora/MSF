# symbolic calculus
import numpy as np
import scipy as sym

t=sym.Symbol('t',real=True,positive=True)
g=sym.Symbol('g',real=True,positive=True)
vt=sym.Symbol('vt',real=True,positive=True)
y=sym.Symbol('y',real=True,positive=True)
vy=sym.Symbol('vy',real=True,positive=True)
ay=sym.Symbol('ay',real=True,positive=True)
D=sym.Symbol('D',real=True,positive=True)




D=sym.diff(sym.sin(2*t),t,1)    #works
print(' d/dt (sin(2t)) = ',D)

# b)
y=vt**2/g*sym.log(sym.cosh(g/vt*t))
#D=sym.diff(vt**2/g*sym.log(sym.cosh(g/vt*t)),t,1)    #works
D=sym.diff(y,t,1)
vy=sym.simplify(D)
print('d/dt(log(cosh(gt/vt))=',vy)


#c)
D=sym.diff(vt**2/g*sym.log(sym.cosh(g/vt*t)),t,2)    #works
ay=sym.simplify(D)
print('d2/dt2(log(cosh(gt/vt))=',ay) 

D=sym.diff(vy,t,1)       
ay=sym.simplify(D)
print('d/dt(velocidade) = ',ay) 

