numeros = []

while True:
    n = int(input())
    if n == 99999:
        break
    numeros.append(n)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(f"Pares: {pares} (total {len(pares)})")
print(f"Impares: {impares} (total {len(impares)})")