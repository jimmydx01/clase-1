from clase4 import cargo

class empleado:
    secuencia=0
    def _init_(self,nom,ced,sue,cargo):
        empleado.secuencia=empleado.secuencia+1
        self.codigo=self.generarCodigo()
        self.nombre=nom 
        self.cedula=ced 
        self.sueldo=sue 
        self.cargo=cargo
    def mostrar(self):
        print("codigo:{} nombre:{} cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))

    def generarCodigo(self):
        empleado.secuencia=empleado.secuencia+1
        return empleado.secuencia

cargo1 = cargo("DOCENTE")
emp1= empleado("daniel","0914",500,cargo1)
emp1.mostrar()    
cargo2 = cargo("ANALISTA")
emp2= empleado("ana","0914",500,cargo2)
emp2.mostrar()          