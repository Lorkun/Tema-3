class nave():
    def __init__(self, nombre, largo, tripulacion, passengers):
        self.nombre=nombre
        self.largo=largo
        self.tripulacion=tripulacion
        self.passengers= passengers
    def __str__(self):
         return "nombre: {}, {} mide de largo, transporta una tripulacion de  {} individuos, los cuales pasajeros son  {} individuos ".format( self.nombre, self.largo, self.tripulacion, self.passengers )
     
EstrellaMuerte= nave("Estrella_de_la_muerte",160000,1281670,100000)
HalconMilenario= nave("Halcon_milenario",34.37,5,3)
Caza_estelar_Ala_x= nave("Caza_estelar_ala_x", 12.5,1,1)
Caza_estelar_TIE= nave("Caza_estelar_TIE",6.3,1,1)
Super_destructor_Estelar = nave("Super_destructor_Estelar",120000,370000,260000)
Crucero_clase_Ventator= nave("Crucero_clase_Ventator",1000,6100,5500)
AT_AT = nave("AT-AT",200,100,10)

naves=[EstrellaMuerte,HalconMilenario,Caza_estelar_Ala_x,Super_destructor_Estelar,Crucero_clase_Ventator, AT_AT,Caza_estelar_TIE]

print(EstrellaMuerte)
print(HalconMilenario)


num_passengers_naves = sorted(naves, key=lambda x: x.passengers, reverse=True)
num_tripulacion_naves = sorted(naves, key=lambda x: x.tripulacion,reverse=True)
largo_de_naves = sorted(naves, key=lambda x: x.largo)

def naves_mas_passengers (n):
    print("Las 5 naves con mas pasajeros son las siguientes: ")
    for i in range (5):
        if i<len(n):
            print(n[i].nombre)

def naves_mas_tripulacion (n):
    print("La nave con mas tripulacion es la ",n[0].nombre)

def naves_mayor_menor_dimension (n):
    print("La nave mas grande es ", n[-1].nombre,"y la nave mas pequena es ",n[0].nombre)

def naves_AT(n):
    print("Las naves que empiezan por AT son las siguientes:")
    for i in n:
        if i.nombre[:2] == "AT":
            print(i.nombre, "es un vehiculo terrestre no una nave.")
        

def naves_mas_seis_pass(n):
    print("La naves que pueden transportar a 6 o mas individuos son: ")
    for i in n:
        if i.passengers >= 6:
            print(i.nombre)


naves_mas_passengers(num_passengers_naves)
naves_mas_tripulacion(num_tripulacion_naves)
naves_mayor_menor_dimension(largo_de_naves)
naves_AT(naves)
naves_mas_seis_pass(naves)
naves_mayor_menor_dimension(naves)

print("La nave más grande",EstrellaMuerte)
print("La nave más pequeña",Caza_estelar_TIE)
