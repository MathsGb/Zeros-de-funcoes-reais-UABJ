import math

# função utilizada para o meu caso será f(x) = e^x - 4x^2
def funcao(x):
    resultado = math.e**x - 4*x**2
    return resultado

Erro = 0.0009
contador = 1
A = int(input("digite a extremidade a esquerda: "))
B = int(input("digite a extremidade a direita: "))
Meio = (A+B)/2 
resultado = funcao(Meio)

while (math.fabs(resultado) > Erro):
    if(resultado > 0):
        A = Meio
    else:
        B = Meio
    Meio = (A+B)/2 
    resultado = funcao(Meio)
    contador += 1

print(Meio)
print(contador)