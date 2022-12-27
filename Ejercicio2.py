lista = [3,2,3,5,3,4,9,1,7]
for n in range (1, 4):
    for v in range(1, 4):
        matriz = int(input(f"Type a value [{n},{v}]"))
        lista.append(matriz)

calc1 = (lista[0]*lista[4]*lista[8])
calc2 = (lista[1]*lista[5]*lista[6])
calc3 = (lista[2]*lista[3]*lista[7])
calc4 = (lista[2]*lista[4]*lista[6])
calc5 = (lista[0]*lista[5]*lista[7])
calc6 = (lista[1]*lista[3]*lista[8])

result = ((calc1 + calc2 + calc3)-(calc4 + calc5 + calc6))
print(result)

