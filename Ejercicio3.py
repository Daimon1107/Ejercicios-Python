Hospital_Veterinario=[]

def agregarPrincipal(lista):
    Hospital_Veterinario.append(lista)

final = []

cantidad = int(input("Cuantas mascotas va a ingresar: "))
cont = 0
perro = 1
    
while cont<cantidad:
    print(f"Ingrese el dato del perro {perro}\n")
    dato1 = input("Ingrese el primer dato: ")
    dato2 = input("Ingrese el segundo dato: ")
    dato3 = input("Ingrese el tercer dato: ")
    dato4 = input("Ingrese el cuarto dato: ")
    
    lista= [dato1,dato2,dato3,dato4]
    cont+=1
    perro+=1
    agregarPrincipal(lista)
    print("")
    
def verificarDecimal(cadena):
    indice = cadena.find(".")
    if indice is -1:
        return False
    return True

def verificarEntero(cadena):
    try:
        int(cadena)
        return True
    except:
        return False
    
def verificarBool(cadena):
    if cadena=="True" or cadena=="False":
        return True
    return False

def verificarCadena(cadena):
    if verificarDecimal(cadena)==False:
        if verificarBool(cadena)==False:
            if verificarEntero(cadena)==False:
                return True
    return False

    
# Cambia los valores string iniciales a los tipos correspondientes              
def unificarVec():
    resultado = []
    for i in Hospital_Veterinario:
        for j in i:
            if verificarCadena(j)==True:
                resultado.append(j)
            if verificarDecimal(j)==True:
                resultado.append(float(j))
            if verificarEntero(j)==True:
                resultado.append(int(j))
            if j=="True":
                resultado.append(True)
            if j=="False":
                resultado.append(False)
        #En esta linea se agregan el nuevo vector
        
        final.append(resultado)   
        resultado = []
     
unificarVec()   
nueva = [" "," "," "," "]
Resultado = []
for i in final:
   for j in i:      
       if type(j)==int:
           nueva[0] = j
       if type(j)==str:
          nueva[1] = j
       if type(j)==float:
          nueva[2] = j
       if type(j)==bool:
           nueva[3] = j      
     
   Resultado.append(nueva)
   nueva = [" ", " "," "," "] 

Resultado.sort(reverse=True)
        
print(f"Vector Resultado: {Resultado}")
