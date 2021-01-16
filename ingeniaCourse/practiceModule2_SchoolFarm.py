# School Farm
# aplicación Práctica Módulo 2
print("#------Registro Huerta Estudiantil------#")
print("""Ingrese un valor de acuerdo al cultivo que requiera registrar: 
'0- Cilantro Salvaje  1- Tomate 2- Cilantro Común 3- Yuca 4- Cebolla Larga'""")
tipoCultivo = int(input("-"))
if tipoCultivo == 0:
    resolucion = ""
    cultivo1 = "Cilantro Salvaje"
    canCultivo1 = float(input("Ingrese la cantidad de cultivo proyectado para recolección: "))
    tieCultivo1 = float(input("Ingrese el tiempo que lleva el cultivo en semanas: "))
    probCultivo1 = int(input("Ingrese 1 si el cultivo tiene problemas o 0 si no presenta problemas "))
    if probCultivo1 == 1:
        resolucion = input("Ingrese el tipo de problema que manifiesta el cultivo: ")
    elif probCultivo1 == 0:
        resolucion = "El cultivo es sano"
    else:
        print("Ha ingresado un valor erroneo, intentelo de nuevo")
        exit()
    print("")
    print("Resumen cultivo de: " + cultivo1)
    print("Cantidad Dispuesta para cocecha: " + str(canCultivo1) + " kilogramos Aprox.")
    print("Tiempo actual de la cocecha: " + str(tieCultivo1) + " semanas")
    print("El cultivo presenta problemas relacionados con: " + resolucion)
elif tipoCultivo == 1:
    resolucion = ""
    cultivo1 = "Tomate"
    canCultivo1 = float(input("Ingrese la cantidad de cultivo proyectado para recolección: "))
    tieCultivo1 = float(input("Ingrese el tiempo que lleva el cultivo en semanas: "))
    probCultivo1 = int(input("Ingrese 1 si el cultivo tiene problemas o 0 si no presenta problemas "))
    if probCultivo1 == 1:
        resolucion = input("Ingrese el tipo de problema que manifiesta el cultivo: ")
    elif probCultivo1 == 0:
        resolucion = "El cultivo es sano"
    else:
        print("Ha ingresado un valor erroneo, intentelo de nuevo")
        exit()
    print("")
    print("Resumen cultivo de: " + cultivo1)
    print("Cantidad Dispuesta para cocecha: " + str(canCultivo1) + " kilogramos Aprox.")
    print("Tiempo actual de la cocecha: " + str(tieCultivo1) + " semanas")
    print("El cultivo presenta problemas relacionados con: " + resolucion)
elif tipoCultivo == 2:
    resolucion = ""
    cultivo1 = "Cilantro Común"
    canCultivo1 = float(input("Ingrese la cantidad de cultivo proyectado para recolección: "))
    tieCultivo1 = float(input("Ingrese el tiempo que lleva el cultivo en semanas: "))
    probCultivo1 = int(input("Ingrese 1 si el cultivo tiene problemas o 0 si no presenta problemas "))
    if probCultivo1 == 1:
        resolucion = input("Ingrese el tipo de problema que manifiesta el cultivo: ")
    elif probCultivo1 == 0:
        resolucion = "El cultivo es sano"
    else:
        print("Ha ingresado un valor erroneo, intentelo de nuevo")
        exit()
    print("")
    print("Resumen cultivo de: " + cultivo1)
    print("Cantidad Dispuesta para cocecha: " + str(canCultivo1) + " kilogramos Aprox.")
    print("Tiempo actual de la cocecha: " + str(tieCultivo1) + " semanas")
    print("El cultivo presenta problemas relacionados con: " + resolucion)
elif tipoCultivo == 3:
    resolucion = ""
    cultivo1 = "Yuca"
    canCultivo1 = float(input("Ingrese la cantidad de cultivo proyectado para recolección: "))
    tieCultivo1 = float(input("Ingrese el tiempo que lleva el cultivo en semanas: "))
    probCultivo1 = int(input("Ingrese 1 si el cultivo tiene problemas o 0 si no presenta problemas "))
    if probCultivo1 == 1:
        resolucion = input("Ingrese el tipo de problema que manifiesta el cultivo: ")
    elif probCultivo1 == 0:
        resolucion = "El cultivo es sano"
    else:
        print("Ha ingresado un valor erroneo, intentelo de nuevo")
        exit()
    print("")
    print("Resumen cultivo de: " + cultivo1)
    print("Cantidad Dispuesta para cocecha: " + str(canCultivo1) + " kilogramos Aprox.")
    print("Tiempo actual de la cocecha: " + str(tieCultivo1) + " semanas")
    print("El cultivo presenta problemas relacionados con: " + resolucion)
elif tipoCultivo == 4:
    resolucion = ""
    cultivo1 = "Cebolla Larga"
    canCultivo1 = float(input("Ingrese la cantidad de cultivo proyectado para recolección: "))
    tieCultivo1 = float(input("Ingrese el tiempo que lleva el cultivo en semanas: "))
    probCultivo1 = int(input("Ingrese 1 si el cultivo tiene problemas o 0 si no presenta problemas "))
    if probCultivo1 == 1:
        resolucion = input("Ingrese el tipo de problema que manifiesta el cultivo: ")
    elif probCultivo1 == 0:
        resolucion = "El cultivo es sano"
    else:
        print("Ha ingresado un valor erroneo, intentelo de nuevo")
        exit()
    print("")
    print("Resumen cultivo de: " + cultivo1)
    print("Cantidad Dispuesta para cocecha: " + str(canCultivo1) + " Ataos Aprox.")
    print("Tiempo actual de la cocecha: " + str(tieCultivo1) + " semanas")
    print("El cultivo presenta problemas relacionados con: " + resolucion)
else:
    print("Ha ingresado un valor erroneo, intentelo de nuevo. ")
    exit()