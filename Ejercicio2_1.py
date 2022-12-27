import copy
def mdet(matriz):
    suma = 0
    if len(matriz) == 3 and len(matriz[0])==3:
        suma = ((matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])+(matriz[0][1]*matriz[1][2]*matriz[2][0]))-((matriz[0][2]*matriz[1][1]*matriz[2][0])+(matriz[0][1]*matriz[1][0]*matriz[2][2])+(matriz[2][1]*matriz[1][2]*matriz[0][0]))
        return suma

    else:
        for i in range(len(matriz)):
            aux = copy.deepcopy(matriz)
            aux.remove(matriz[0])
            for j in range(len(aux)):
                aux[j]= aux[j][0:i] + aux[j][i+1:]
            suma += (-1)** (i %2) * matriz[0][i * mdet(aux)]
            return suma

print(mdet([[3,2,3],[5,3,4],[9,1,7]])) 
