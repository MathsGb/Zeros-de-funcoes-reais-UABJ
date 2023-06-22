import math

def f(x):
    return math.exp(x) - 4*x**2

#condições iniciais
A = 0 
B = 1

erro = 0.00009
k = 0  #contador de 

#criamos a contante "M" para a nossa reta

M = (B * f(A) - A * f(B)) / (f(A) - f(B))

while(f(M) > erro):
    if (f(A) * f(M)) < 0:
        B = M
    else:
        A = M
    k += 1
    M = (B * f(A) - A * f(B)) / (f(A) - f(B))

print(f"A raiz encontrada foi {M} ")
print(f"o número de interações é foi {k} ")