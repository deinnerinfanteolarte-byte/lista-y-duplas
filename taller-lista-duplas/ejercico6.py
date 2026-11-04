n = int(input("Cuantos números? "))
num_buscar = int(input("Digite el número a buscar: "))

list_nums = []

for i in range(1, n + 1):
    num = int(input(f"\nDigite #{i}: "))
    list_nums.append(num)

pos = -1
for j in range(len(list_nums)):
    if num_buscar == list_nums[j]:
        pos = j
        print("Pos", j)

if pos >= 0:
    print(f"{num_buscar} está en la posición {pos}")
else:
    print(f"El {num_buscar} no está en la lista")