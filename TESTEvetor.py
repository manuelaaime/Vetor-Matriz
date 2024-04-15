VET = []

for i in range(10):
    numero = int(input(f"Digite o número {i+1}/10: "))
    VET.append(numero)

# Verifica se existem números repetidos e em quais posições.
repetidos = {}
for i, numero in enumerate(VET):
    if VET.count(numero) > 1:
        if numero not in repetidos:
            repetidos[numero] = []
        repetidos[numero].append(i)

if repetidos:
    print("Números repetidos e suas respectivas posições:")
    for numero, posicoes in repetidos.items():
        print(f"O número {numero} está repetido nas posições: {posicoes}")
else:
    print("Não existem números repetidos no vetor VET.")
