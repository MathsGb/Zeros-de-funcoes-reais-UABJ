import math

def f(x):
    return math.e**x - 4*x**2

# Função de interação
def phi(x):
    X1 = x - (f(x)/(math.e**x - 8*x))
    return X1

# aproximação inicial

#condição inicia ou somente X0 está dentro do intervalo dado
A = 0.5

Erro = 0.00009
k = 0

while(abs(f(A)) > Erro):
    A = phi(A)
    k += 1

print(f"solução encontrada foi {A} ")
print(f"o número de interações é foi {k} ")