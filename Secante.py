import math

def f(x):
    return math.exp(x) - 4*x**2 

#condiçôes iniciais
x_0 = 0
x_1 = 1

erro = 0.00009
k = 0 # contador de interações

while(abs(f(x_1))>erro):

    if abs(x_0 - x_1) < erro:
        break
    x_2 = (x_0 * f(x_1) - x_1 * f(x_0)) / (f(x_1) - f(x_0))

    x_0 = x_1
    x_1 = x_2
    k += 1

print(f"solução encontrada foi {x_1} ")
print(f"o número de interações é foi {k} ")