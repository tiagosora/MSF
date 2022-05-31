# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:29:53 2022

@author: draki
"""

#    VELOCIDADE TERMINAL 
#    x(y) = (Vt^2/g)*ln(cosh(gt/Vt)), Vt = velocidade terminal, t = tempo, g = gravidade
#    a(y) = g - (g/Vt^2)*Vy*|Vy|, Vy = velocidade no instante anterior

#    Aplicar logaritmos a funçoes para regressao linear
#    y=cx^n ---> log(y) = log(c) + n * log(x)
#    y=c*e^(nt) ---> log(y) = log(c) + n*t
#    n = declive

#    Equaçoes de movimento
#    x = x0 + v0 * t + 1/2 * a * t^2
#    v = v0 + a*t
#    v^2 = v0^2 + 2a * (x-x0) equaçao de torriceli


#    Euleur
#    v(psi + psi) = v(psi) + ac*dt, neste caso ac = g
#    x(psi +psi) = x(psi) +v(psy)*dt