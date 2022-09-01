
from tkinter import S


class Servidor:
    def __init__(self,name):
        self.name=name
    
    def execute(self):
        return 'TCP/IP'

class Aplicacion:
    def __init__(self,name):
        self.name=name
 
   
 
    def Conexion(self):
        return 'Serie'
 
class Adapter:
    def __init__(self,obj,adapted_methods):
        self.obj=obj
        self.__dict__.update(adapted_methods)
 
    def __str__(self):
        return  str(self.obj)

def main():
    objects=[Servidor('TCI/IP')]
    Servidor=Servidor('TCI/IP')
    objects.append(Adapter(Servidor,dict(execute=Servidor.play)))
    Aplicacion=Aplicacion('Series')
    objects.append(Adapter(Aplicacion,dict(execute=Aplicacion.speak)))
    for i in objects:
        print('{} {}'.format(str(i),i.execute()))