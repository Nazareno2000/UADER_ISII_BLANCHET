import string

class VGA:
  
    def conexion(self)-> str:
       return  print ("conectado")
        
   

class HD :
    
    def serial_open(self) -> str:
        return "conectado atraves puerto VGA"
        
   


class AdapterVGA2HD(VGA, HD):

    def conexion(self) -> str:
        return f"Adapter:  {self.serial_open()}"
 
   

def sender(VGA: "VGA") :
    print(VGA.conexion())




Vga = VGA()
sender(Vga)

adapter= AdapterVGA2HD()

sender(adapter)