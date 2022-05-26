



print("---- MENU----")
print("1.- Ingresar informacion")
print("2.- Buscar informacion")
print("3.- Salir")

opcion = int(input("Ingrese su opcion : "))
lista = ["","","","",""]
total = []

while True:

    if opcion==1:

        print("Crear registro: ")
        nombre = input("Ingrese su nombre: ")
        lista[0] = nombre

        apellido = input("Ingrese su apellido: ")
        lista[1] = apellido
        marca = input("Ingrese la maraca del computador: ")
        lista[2] = marca
        ciudad = input("Ingrese la ciudad en donde reside:  ")
        lista[3] = ciudad
    
        tamaño = str(input("Ingrese el tamaño del computador:  "))
        lista[4] = tamaño
        total.append(lista)
        lista= ["","","","",""]

        opcion = int(input("Ingrese su opcion : "))
    elif opcion==2:
        buscar = input("Digite el dato de la persona que va a buscar: ")
        for i in total:
            for j in i:
                if j==buscar:
                    print("Se encontro estos datos: ")
                    print(f"Cliente {i}")
                    
        opcion = int(input("Ingrese su opcion : "))

        break
    else: 
        break