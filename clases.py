#no puede ser en mayusculas
#no puede empezar con un numero
#no puede contener espacios
#no puede contener caracteres especiales ni vocales con tildes (NO ñ)}

#variable
#nom = "Maikol"  

# Entrada 
#nom = input("Ingresa tu nombre: ")

#salida
#print("Hola", nom, " bienvenido a la clase")

#Actividad: Que permita ingresar 5 datos de un usuario 
#y los despliegue de forma amable e intuitiva 
# NOTA: ocupe los 3 tipos de datos
#5 output y 1 print


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------


# DECLARAMOS LAS VARIABLES

#nombre = ""
#peso = 0
#religion = ""
#nacionalidad = ""
#numeroCelular = 0

# INGRESAMOS LOS INPUT PARA EL USUARIO

#nombre = input("Ingresa tu nombre: ")
#peso = input("ingresa tu peso: ")
#religion = input("Ingresa tu religion: ")
#nacionalidad = input("ingresa tu nacionalidad: ")
#numeroCelular = input("Ingresa tu numero de celular: ")

# IMPRIMIMOS EN PANTALLA LOS DATOS DEL USUARIO

#print(f"Hola {nombre} tu peso es {peso} tu religion es {religion} tu nacionalidad es {nacionalidad} y tu numero de celular es {numeroCelular}")

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

#como convertir una variable con los parentesis y en este caso el INT

#ed = 0
#ed_prox_anio = 0

#ed =int(input("su edad: ")) #int convierte un cadena(string, texto, alfanumérico) a número entero, float convierte a decimal

#ed_prox_anio = ed + 1

# salida
#print("su edad actual es", ed, "el proximo año vas a tener", ed_prox_anio)


# ACTIVIDAD 24/03

# desarrolle un programa que permita ingresar el año actual y el año de nacimiento
# y despliegue por pantalla la edad

# declaramos las variables
#ed_nacimiento = 0
#ed_actual = 2026
#edad = 0

# pedimos al usuario las variables CONVIRTIENDOLAS
#ed_actual = int(input("Ingresa el año actual: "))
#ed_nacimiento = int(input("Ingresa tu año de nacimiento: "))

# hacemos el calculo
#edad = ed_actual - ed_nacimiento

#imprimimos en pantalla el resultaodo con la variable final
#print(F"Su edad actual es: {edad}")

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

# Clase 25/03


#----------------------------------
# 1ra TAREA
#----------------------------------


# En una terminal salen dos buses con destino a la ciudad de valdivia
# transportan a 35 pasajeros cada uno, el valor del pasaje fue de 5.500. Cual es la recaudacion obtenida

# Declaramos las variables

"""cantidad_buses = 0
valor_pasaje = 0
recaudacion_total = 0
pasajeros_actuales = 0

cantidad_buses = int(input("ingresa la cantidad de buses: " ))
valor_pasaje = int(input("Ingresa el valor del pasaje: "))

if cantidad_buses > 0:
    for i in range(1, cantidad_buses + 1):
        pasajeros_actuales = int(input(f"Ingresa los pasajeros para el bus {i}: "))
    recaudacion_total = recaudacion_total + (valor_pasaje * pasajeros_actuales)

    print(f"la recaudacion total es:{recaudacion_total: }")

else: 
    print("error: la cantidad de buses debe ser mayor a 0")"""



# listado de como hacer fideos con procesos 50 lineas


#----------------------------------
# 2ra TAREA
#----------------------------------


# una distribuidora de insumos computacionales compro 20 cajas de mause
# Si cada caka contiene 16 mause y el valor de cada mause es de 3500
# cuanto debio cancelar la distribuidora por dicha compra


# listado de como hacer fideos con procesos 50 lineas



# don juan gonzalez compra 2 packs de cervezas (6 latas por pack)
# 1 marca dorada y  la otra baldica, el total de su compra fue 4500 pesos
# y el pack de baldica costo 2100 ¿cuanto es elcosto de cada lata de cervezas dorada y baldicac?


# declaramos las variables
"""marca1 = ""
marca2 = ""
total_compra = 0
precio_marca1 = 0
precio_marca2 = 0
latas_por_pack = 6
precio_por_lata = 0
total_latas = 0

# pedimos la marca de cerveza
marca1 = input("Indique la marca que desea comprar:")
marca2 = input("Indique la otra marca que desea comprar:")


# convertimos la variable en int para poder trabajar con ella 
total_compra = float(input("ingresa el total de la boleta: "))
precio_marca2 = float(input(f"cuanto costo el pack de {marca2}: "))


# calculamos el precio de la cerveza MARCA 1 
precio_marca1 = total_compra - precio_marca2

total_latas = latas_por_pack * 2

precio_por_lata = (total_compra / total_latas)

print("El precio por lata (promedio de ambas marcas) es:", precio_por_lata)"""

# ---------------------------------------
# clase 27/03
# ---------------------------------------


"""usuario_correcto = "anto"
contrasena_correcta =  "anto123"

usuario = str(input("Ingresa tu usuario:"))
contrasena= str(input("Ingresa tu contraseña:"))

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso concedido")

elif usuario == usuario_correcto and contrasena != contrasena_correcta:
    print("La contraseña no es correcta")

elif usuario != usuario_correcto and contrasena == contrasena_correcta:
    print("El usuario es incorrecto")
    
else:
    print("El usuario y la contraseña no coinciden")"""


# BASE DE DATOS CON RANGE Y DICCIONARIO 

"""base_de_datos = {}

for i in range(1, 51):
    usuario = f"alumno {i}"
    contrasena = f"alumno {i}"
    base_de_datos[usuario] = contrasena

user_input = input("Ingresa tu usuario: ")
pass_input = input("Ingresa tu contraseña: ")

if user_input in base_de_datos:
    if base_de_datos[user_input] == pass_input:
        print(f"Acceso concedido. Que tal {user_input}")
    
    else:
        print("contraseña incorrecta.")
else:
    print("El alumno no existe en la base de datos")"""

#------------------------------------------------------------------
"""age = 0

age = int(input("Cual es tu edad: "))

if age > 130:
    print("Estas muerto viejo")
else:
    
    if age >= 18:
        print("Eres mayor de edad")
    else:
        
        if age > 0:
            print("Eres menor de edad")
        else:
            print("No has nacido")"""

# desarrolle u  programa que permita ingresar 3 numeros y desplegar siempre el mayor
# NOTA siempre con los 3 numeros distintos

"""num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))

if num1 > num2:
 
    if num1 > num3:
        print(f"El mayor es el numero 1: {num1}")
    else:
        
        print(f"El mayor es el numero 3: {num3}")
else:
    
    if num2 > num3:
        print(f"El mayor es el numero 2: {num2}")
    else:
       
        print(f"El mayor es el numero 3: {num3}")"""

# desarrole un programa que permita ingreasar 3 numeros y siempre los despliegue ascendentemente

"""A = 0
B = 0
C = 0

A = int(input("Ingrese el numero 1: "))
B = int(input("Ingrese el numero 2: "))
C = int(input("Ingrese el numero 3: "))

if A < B:
    if B < C:
        print(f"El orden es: \n {A} \n {B} \n {C}")
    else:
        if A < C:
            print(f"El orden es: \n{ A} \n {C} \n {B}")
        else:
            print(f"El orden es: \n {C} \n {A} \n {B}")
else:
    if A < C:
        print(f"El orden es: \n {B} \n {A} \n {C}")
    else:
        if B < C:
            print(f"El orden es: \n {B} \n {C} \n {A}")
        else:
            print(f"El orden es: \n {C} \n {B} \n {A}")"""

# -------------------------------------------------------------------------
# desarrole un programa que permita ingresar 2 numeros
# si el primero es mayor que el segundo, desliegue la resta de ellos
# si no la multiplicacion de ellos, si son iguales se suman

num1 = 0 
num2 = 0
operacion = 0


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))


if num1 > num2:
    operacion = num1 - num2
    print(f"La resta da {operacion}")
else:
    if num1 < num2:
        operacion = num1 * num2
        print(f"La multiplicacion da {operacion}")
    else:
            operacion = num1 + num2
            print(f"La suma da {operacion}")
