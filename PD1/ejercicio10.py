import math
valores=[1,2,3]
print("Evaluación para x = 8^(-n)\n")
for n in valores:
    x=8**(-n)
    f=math.sqrt(x**2+1)-1
    g=x**2/(math.sqrt(x**2+1)+1)
    print("Para n =",n)
    print("x = 8^(-{}) = {:.10f}".format(n,x))
    print("f(x) = {:.15f}".format(f))
    print("g(x) = {:.15f}".format(g))
    print("diferencia =",abs(f-g))
    print("-----------------------------")
//Para n=1,2,3 los valores de f y g son prácticamente iguales.
//Sin embargo, para valores más pequeños de x se presentan diferencias
//debido al error de cancelación.