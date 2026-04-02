import math
print("{:<3} {:<12} {:<20} {:<20} {:<20}".format("n","x","f(x)","g(x)","diferencia"))
print("-"*75)
for n in range(1, 11):
    x=8**(-n)
    f=math.sqrt(x**2+1)-1
    g=x**2/(math.sqrt(x**2+1)+1)
    print("{:<3} {:<12.5e} {:<20.15e} {:<20.15e} {:<20.15e}".format(n,x,f,g,abs(f - g)))