
menu = "Viva jesus\n"
menu += "1. Ingresar nombre y año de nacimiento\n"
menu += "2. calcular edad y mostrar en pantalla\n"
menu += "3. Mostrar saludo de buenas noches el usuario\n"
menu += "4. Contar cuantos años tendra en el 2030\n"
menu += "5. Salir\n"
print(menu)

opcion = 0 
nombre = ""
while (opcion != 5):  
    edad = 0
    opcion = int(input("Ingresar la opcion: "))
    if opcion == 1:
        nombre = input("Ingresar nombre: ")
        edad = int(input('Ingresar año de nacimiento: '))
        edadActual = 2022 - edad 
    elif opcion == 2:
        print(nombre)
        print(edadActual)  
          
