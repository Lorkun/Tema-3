import sympy

pol1 = input("Introduce el primer polinomio: ")
pol2 = input("Introduce el segundo polinomio: ")

sympy.init_printing()
x,y = sympy.symbols("x,y")
pol1 = sympy.Poly(pol1)
pol2 = sympy.Poly(pol2)


def resta(pol1, pol2):
    return pol1-pol2
def dividir(pol1, pol2):
    return pol1/pol2

print(resta(pol1,pol2))
print(dividir(pol1,pol2))




