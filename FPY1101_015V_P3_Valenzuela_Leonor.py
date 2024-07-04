import os
os.system("cls")

#codigo=codigo+letra
#    codigo.endswith()
#LARGONIF12

personas=[]

def registo_personas():
    print("Registrando")
    while True:
        nombre= input("Ingrese nombre : ").lower()
        #while len(nombre) < 8:
        while nombre =="" or nombre ==" " :
            nombre=int("Nombre no valido, ingrese nuevamente : ")
        try:
            edad=int(input("Ingrese su edad : "))
        except:
            edad=0
        if edad <1:
            print("Edad fuera de rango")
            break
        else:            
            nif=input("Ingrese NIF : ")
            while len(nif)!=12:
                nif=input("Nif no valido, ingrese nuevamente : ")
        



        persona ={
            'Nombre' : nombre,
            'Edad' :   edad,
            'NIF' : nif
        }

        personas.append(persona)

        otro=input("Desea agregar otro si o no : ").lower()
        if otro =="si":
            continue
        else:
            break

def buscar_persona():
    print("Buscando")
    nif_buscado=input("Ingrese NIF a consultar  : ")
    for persona in personas:
        if nif_buscado!= persona['NIF']:
            print("Nif no se encuentra en nuestros registros")
        else:
            if nif_buscado.endswith("SP"):
                print("España")
                print(persona)
                
def imprimir_certificado():
    print("Seleccione certificado")
    print("""
          1. Certificado de Nacimiento $.1500.-
          2. Estado Conyugal $.4000.-
          3. Pertenencia a Union Española $5.000.-
          
          """)
    try:
        opc=int(input("Ingrese numero de certificado : "))
    except:
        opc=-1
    if opc <1 or opc >3:
        print("Opcion no valida")
    else:
        if opc ==1:
            nif_imprimir =input("Ingrese NIF : ")
            print("Certificado de nacimiento $1.500.-")
            for persona in personas:
                if nif_imprimir != persona['NIF']:
                    print("No ha sido porisble generar el certificado, NIF sin registros")
                else:
                    print("Nombre", "Edad", "NIF")
                    print(f"{persona['Nombre']}, {persona['Edad']}, {persona['NIF']}")
        elif opc==2:
            nif_imprimir =input("Ingrese NIF : ")
            print("Estado Conyugal $4.000")
            for persona in personas:
                if nif_imprimir != persona['NIF']:
                    print("No ha sido porisble generar el certificado, NIF sin registros")
                else:
                    print("Nombre", "Edad", "NIF")
                    print(f"{persona['Nombre']}, {persona['Edad']}, {persona['NIF']}")
        elif opc==3:
            nif_imprimir =input("Ingrese NIF : ")
            print("Pertenencia a Union Española $5.000.-")
            for persona in personas:
                if nif_imprimir != persona['NIF']:
                    print("No ha sido porisble generar el certificado, NIF sin registros")
                else:
                    print("Nombre", "Edad", "NIF")
                    print(f"{persona['Nombre']}, {persona['Edad']}, {persona['NIF']}")
                         
        
        
def salir():
    print("Hasta pronto")


while True:
    print("""
        Menú:
        1. Grabar
        2. Buscar
        3. Imprimir Certificados
        4. Salir
         """)

    try:
        op=int(input("Ingrese Opcion : "))
    except:
        op=0

    if op <1 or op >4:
        
        print("Opcion no valida")
    else:
        if op ==1:
            registo_personas()
        elif op==2:
            buscar_persona()
    
        elif op==3:
            os.system("cls")
            imprimir_certificado()
            
        elif op ==4:
            salir()
            
        else:
            break


