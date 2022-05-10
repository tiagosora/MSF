import sympy as sym

## Criação dos símbolos a utilizar no cálculo simbólico
t = sym.Symbol('t',real=True,positive=True)
g = sym.Symbol('g',real=True,positive=True)
vt = sym.Symbol('vt',real=True,positive=True)
y = sym.Symbol('y',real=True,positive=True)
vy = sym.Symbol('vy',real=True,positive=True)
ay = sym.Symbol('ay',real=True,positive=True)
D = sym.Symbol('D',real=True,positive=True)

## Alínea b)
y = (vt**2/g)*sym.log(sym.cosh(g/vt*t))
D = sym.diff(y,t,1)
vy = sym.simplify(D)
print("A expressão da velocidade instantânea é: ", vy)

# Alínea c)

D = sym.diff(y,t,2)
ay = sym.simplify(D)
print("A expressão da aceleração instântanea é: ", ay)



