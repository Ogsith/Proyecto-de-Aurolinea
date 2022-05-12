import random
import datetime
IoM = input(" ¿Desea imprimir un ticket o modificar un ticket?")

if IoM == 'I' or IoM == 'i':
    print("Ingrese su nombre y apellidos ")
    NomAppellido = input()
    print("Ingrese su DNI: ")
    DNI = input()
    print("Ingrese su origen: ")
    Origen = input()
    print("Ingrese su destino: ")
    Destino = input()
    print("Ingrese la fecha de salida: ")
    Fsalida = input()
    horasalida=int(input("Ingrese la hora de salida: "))
    minutosalida=int(input("Ingrese los minutos de la salida: "))
    d1=datetime.timedelta(hours=0,minutes=30)
    d2=datetime.timedelta(hours=horasalida,minutes=minutosalida)
    tipoavion = input("Elija el avión que prefiera, Boeing-777 o Airbus-a350: ")
    if tipoavion == "Boeing-777" or tipoavion == "boeing-777":
        claseboeing = input("Elija una clase, Premium, Ejecutivo,Primera o Económica: ")
        #Son 55filas
        #En premium supongamos que solo hubieran 5 filas que pertenezcan a premium
        if claseboeing == "Premium":
            print("***************** UTEC airlines *****************")
            print("*BOARDING PASS - CARTE D´EMBARQUEMENT")
            print("*AVION BOEING-777 CLASE : Premium")
            print("*SEAT= ","FILA:",random.randint(1,5),"COLUMNA: ",random.randint(1,9))
        elif claseboeing == "Ejecutivo":
            #En ejecutivo supongamos que solo hubieran 18 filas
            print("***************** UTEC airlines *****************")
            print("*BOARDING PASS - CARTE D´EMBARQUEMENT")
            print("*BOEING-777 CLASE : Ejecutivo")
            print("*SEAT= ","FILA:",random.randint(1,18),"COLUMNA: ",random.randint(1,9))
        elif claseboeing == "Primera":
            #En primera supongamos que solo hubieran 16filas
            print("***************** UTEC airlines *****************")
            print("*BOARDING PASS - CARTE D´EMBARQUEMENT")
            print("*AVION BOEING-777 CLASE : PRIMERA")
            print("*SEAT= ","FILA:",random.randint(1,16),"COLUMNA: ",random.randint(1,9))
        elif claseboeing == "Económica":
            #En economica supongamos que solo hubieran 16 fias
            print("***************** UTEC airlines *****************")
            print("*BOARDING PASS - CARTE D´EMBARQUEMENT")
            print("*AVION BOEING-777 CLASE : ECONOMICA")
            print("*SEAT= ","FILA:",random.randint(1,16),"COLUMNA: ",random.randint(1,9))
    elif tipoavion == "Airbus-a350" or tipoavion == "airbus-a350":
        #Son 26 filas en total para airbus
        claseairbus = input("Elija una clase: Ejecutivo o Económico:")
        if claseairbus == "Ejecutivo":
            #Supongamos que en la clase ejecutivo solo hay 6filas de ejecutivo
            print("***************** UTEC airlines *****************")
            print("*BOARDING PASS - CARTE D´EMBARQUEMENT")
            print("*Airbus-a350 CLASE :Ejecutivo")
            print("*SEAT= ","FILA:",random.randint(1,6),"COLUMNA: ",random.randint(1,6))
        elif claseairbus == "Económico":
            #Supongamos que en la clase ejecutivo solo hay 20filas de economico
            print("***************** UTEC airlines *****************")
            print("*BOARDING PASS - CARTE D´EMBARQUEMENT")
            print("*Airbus-a350 CLASE :Ejecutivo")
            print("*SEAT= ","FILA:",random.randint(1,20),"COLUMNA: ",random.randint(1,6))

    print("*BOARDING TIME:",d2-d1)
    print("*FLIGHT: ",Destino)
    print("*DATE: ",Fsalida)
    print("*GATE P",random.randint(1,10)," ")
    print("*FROM: ",Origen,"To: ",Destino)
    print("*NAME OF PASSENGER: ",NomAppellido)

elif IoM == 'M' or IoM == 'm':
    n = input("Ingrese su nombre y appellido: ")
    a = input("Ingrese su número de asiento a modificar: ")
    DNI = input("Ingrese DNI: ")
    Clase = input("Ingrese la clase: ")
    print("***************** UTEC airlines *****************")
    print("*BOARDING PASS - CARTE D´EMBARQUEMENT")
    print("BOARDING PASS NUEVO")
    print("*SEAT:",a)
    print("DNI: ",DNI)
    print("AVION BOEING-777 CLASE : ",Clase)
    print("*NAME OF PASSENGER: ",n)

else:
    print("No está registrado")


Consola = input(" ¿Ahora desea modificar un ticket? ")
if Consola == 'M' or Consola == 'm':
    Nombre= input("Ingrese nombres: ")
    Apellido = input("Ingrese apellidos: ")
    DNI = input("Ingrese DNI: ")
    Clase = input("Ingrese la clase: ")
    print("***************** UTEC airlines *****************")
    print("*BOARDING PASS - CARTE D´EMBARQUEMENT")
    print("DNI: ",DNI)
    print("AVION BOEING-777 CLASE : ",Clase)
    print("*NAME OF PASSENGER: ",Nombre,Apellido)
