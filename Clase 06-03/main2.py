op=0
while op<3:
    print("Menu")
    print("1. opcionA")
    print("2. opcionB")
    print("3. salir")
    op=int(input("Ingrese su opcion: "))

    if (op==1):
        print("Eligio la opcion 1")
    elif (op==2):
        print("Eligio la opcion 2")
    elif (op==3):
        print("Saliendo...")
    else:
        print("Ninguna")

