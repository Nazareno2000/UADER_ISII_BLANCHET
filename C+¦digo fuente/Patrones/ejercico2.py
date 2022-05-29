#*--------------------------------------------------
#* adapter.py
#* excerpt from https://refactoring.guru/design-patterns/adapter/python/example
#*--------------------------------------------------

from http import client
from sqlite3 import adapt
import string
from numpy import true_divide


class Target:
   

    def request(self) -> str:
        return "conexión real es por TCP/IP."


class Adaptee:


    def specific_request(self) -> str:
        return "puerto serie"


class Adapter(Target, Adaptee):

    def conexionconexito(self) -> str:
        return f"Adapter:  {self.specific_request()}"

    def abripuertoserie(self)-> str:
       return  print ("abierto el puerto TCP/ID")
        
    
    def put(self)-> str:
        return print("recibio mensanje")
       


    def close(self)->str:
       return print("Puerto cerrado")
       


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Cliente: solo puedo trabajar con los obejotos objetivos:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: La clase Adaptee tiene una interfaz rara. "
          "Mira, no lo entiendo:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Pero puedo trabajar con él a través del Adaptador:")
    adapter = Adapter()
    client_code(adapter.abripuertoserie())
    client_code(adapter.conexionconexito())
    client_code(adapter.put())
    client_code(adapter.close())