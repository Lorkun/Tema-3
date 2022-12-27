def Hanoi(discos, TInicial=1, TAuxiliar = 2, TFinal=3):
    if discos == 1:
        print(TInicial,"t",TFinal)

    else:
        Hanoi(discos-1,TInicial,TFinal,TAuxiliar)
        print(TInicial,"t",TFinal)
        Hanoi(discos-1,TAuxiliar,TInicial,TFinal)
    return 

