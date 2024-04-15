import random

A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

matriz_A = sum(sum(linha) for linha in A)
print("Soma de todos os valores da matriz A:", matriz_A)

B = [[valor * 3 for valor in linha] for linha in A]

print("Matriz B:")
for linha in B:
    print(linha)
