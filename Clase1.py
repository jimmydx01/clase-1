# Numericos
edad, _peso = 50, 70.5

#String
nombres = " Jimmy Martinez"
dirDomiciliaria = "la pradera"
tipo_sexo="M"

#Boolean
civil = True

#Colecciones
usuario=("Jmartinezb","1234", "Jmartinezb@unemi.edu.ec")
materias= ["programacion web", "PHP", "POO"]
docente = {"nombre":"Josue", "edad":20, "fac":"faci"}
#imprimir
print("""Mi nombre es {}, tengo {}
amos""".format(nombres,edad))
print(usuario, docente, materias)

#Estructura de control if
x=int(input("Ingresa un numero entero: "))
if x < 0:
    x=0
    print("Negativo cambiado a 0")
elif x == 0:
    print("cero")
elif x == 1:
    print("Uno")
else:
    print("Ninguna opcion")
print("ok") if type(x) == int else print("-")

#Uso while infinito
c = 1
while True:
    print(c)

# while validation
vocal = str(input("Ingrese vocal"))
while vocal not in ("a", "e", "i", "o", "u"):
    if vocal ==".":
        break
    vocal = input("Vocal: ")
print("su vocal o punto es: {}".format(vocal))

# for range(v) -- range(vi,vf)- range (vi, vf, inc)
frase = input("Ingrese frase: ")
for indice in range(len(frase)):
    print(indice,"=", frase[indice])

# for cadena - in(tupla)- in (lista)
for car in frase:
    if car in ('a','e', 'i' , 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        if car in["A","E", "I", "O", "U"]:
            continue
        else:
            cvoc = cvoc + 1
print("cantidad vocales: {}".format(cvoc))

#comprehension - [var for var in datos condicion]
[car for car in["a", 'e', 'o', 'u'] if car not in ["a", "i", "o"]]

# FUNCIONES SIN RETORNO
def vocales(frase):
    for car in frase:
        if car in ("a", "e", "i", "i", "o", "u"):
            print(car)

# LLAMADA DE FUNCION

oracion = input("Ingrese oracion: ")
vocales(oracion.lower())

# FUNCION CON RETORNO DE VALOR

def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)

# LLAMADA A FUNCION
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
print("Promedio: ()".format(listanotas, prom))

# Funciones Matematicas
import math
num1, num2, num, men = 12.572, 15.4, 4, "1234"
print(math.ceil(num1),"\t", math.floor(num1))
print(round(num1,1),"\t",type(num), "\t", type(men))

#Funciones de Cadena
mensaje = "Hola" + "mundo" + "Python"
men1 = mensaje.split()
men2 = "".join(men1)
print(mensaje[0], mensaje[0:4], men1, men2)
print(mensaje.find("mundo"), mensaje.lower())

#Funciones de Fecha
from datetime import datetime, timedelta, date
hoy, fdia = datetime.now(), date.today()
futuro = hoy + timedelta(days = 30)
dif, aa, mm, dd = futuro - hoy, hoy.year, hoy.month, hoy.day
fecha = date(aa, mm, dd+2)
print(hoy. fdia, futuro, dif, fecha)