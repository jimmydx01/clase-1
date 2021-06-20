 class Ciclos:
    def __init__(self, num1=0):
        self.numero1 = num1

    def usowhile(self):
        # ciclo repetitivo que se ejecuta por verdadero y sale por falso
        car = input("Ingrese una vocal")
        car = car.lower()
        while car not in ("a", "e", "i", "o", "u"):
            car = input("Ingrese una vocal: ").lower
        print("felicitaciones el caracter: {}  es una vocal".format(car))


ciclo1 = Ciclos()
ciclo1.usowhile()


class Condicion:
    contador = 0  # variable de clases(opcional)
    # __init__ Metodo constructor que se ehecuta cuando se instancia la clase cuyo objeto es crear
    # e inicializar ls atributos de la clase. Self es un objeto que representa

    def __init__(self, num1=0, num2=0):
        self.numero1 = num1
        self.numero2 = num2

    def uso_if(self):
        if self.numero1 == self.numero2:
            print("num1:{}, num2:{}  SOn iguales".format(self.numero1, self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1:{},numero3:{} son iguales".format(self.numero1, self.numero2))
        else: print("No son iguales")

# usar clase
cond1 = Condicion()
print(cond1.numero1)
print(cond1.numero2)

cond1 = Condicion(10,20)
print(cond1.numero1)
print(cond1.numero2)

num=2
if type(num)==int:
    print("respuesta", num*2)
else:
    print("El dato no es numerico")

def mensaje(men):
    print(men)

mensaje("Mi primer programa")
mensaje("Mi segundo programa")


#class Sintaxis:
    #def useVariables(self):
        #edad, _peso = 50, 70.50


#ejer1 = Sintaxis()
#ejer1.useVariables()

class Sintaxis:
    instancia = 0 # variables de clases
    # __init__ Metoo constructor que se ejecura cuando se instancia la lase cuyo objetivo es
    # e inicializar los atributos de la clase, Self es un objeto que representa la clase creada
    def __init__(self, dato="Inicializacion"):
        self.frase = dato # variables de instancia
        #Sintaxis.instancia = Sintaxis.Instancia+1

    # def usoVariables(self):
    #     edad, _peso = 50, 70.5
    #     nombres = "Jimmy Martinez"
    #     tipo_sexo = "M"
    #     civil = True
    #     print(nombres, edad)

# ejer1 = Sintaxis() #se crea un objeto que es una instancia de la clase
# ejer1.usoVariables()
# print(ejer1.frase)

    def usoVariables(self):
        edad, _peso = 50, 70.5
        nombres = "Jimmy Martinez"
        tipo_sexo = "M"
        civil = True
        # tuplas = () son colecciondes de datos de cualquier tipo inmutables
        usuario=()
        usuario=("Jmartinezb",1234, "Jmartinezb@unemi.edu.ec", True)
        #usuario[3]="milagro"
        # listas = [] colecciones mutables
        materias = []
        materias = ["Programacion web", "PHP", "POO"]
        materias[1]= "Python"
        materias.append("Go")
        # diccionario = {} coleccioones de objetos clave: valor tipo json
        docente = []
        docente = {"nombre":"Daniel","edad":50, "fac":"faci"}
        docente ["carrera"] = "CS"
        # #presentacion con format
        # print("""Mi nombres es {}, tengo {}
        # anos""".format(nombres, edad))
        #print(usuario, materias, docente)
        print(usuario,usuario[0], usuario[0:2], usuario[-1])
        #print(materias, materias[2:}, materias[:1], materias[::], materias[-2:])
        #print(docente, docente["nombre"])


ejer1 = Sintaxis() #se crea un objeto que es una instancia de la clase
ejer1.usoVariables()
print(ejer1.frase)
