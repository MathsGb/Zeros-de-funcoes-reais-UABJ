import math

# função utilizada para o meu caso será f(x) = e^x - 4x^2
def funcao(x):
    resultado = math.e**x - 4*x**2
    return resultado

#condições iniciais
A = 0
B = 1
Erro = 0.0009
k = 1

Meio = (A+B)/2
resultado = funcao(Meio)

while (math.fabs(resultado) > Erro):
    if(resultado > 0):
        A = Meio
    else:
        B = Meio
    Meio = (A+B)/2 
    resultado = funcao(Meio)
    k += 1

print(f"O resultado da raiz é {Meio}")
print(f"e o número de interações é {k}")