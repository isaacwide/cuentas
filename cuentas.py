import random 

def muliplicacion(estado):
    
    if estado == 0 :
        a = random.randint(1,10)
        b = random.randint(1,10)
    if estado == 1 :
        a = random.randint(10,20)
        b = random.randint(10,20)
    if estado == 2 :
        a = random.randint(21,40)
        b = random.randint(21,40)
    if estado == 3 :
       print("VAMOS A ALOCARNOS ")
       a = random.randint(21,40)
       b = random.randint(21,40)
       
    print(f"{a} x {b}")
    respuesta = int(input("Respuesta......"))

    if (a*b) == respuesta:
       return True
    return False

def _main() -> None:
  live = 3
  estado = 0 
  pinter = False 
  alive = True
  contador = 0 
  
  while alive:

    pinter = muliplicacion(estado)

    if pinter :
       contador =  contador +1
    else : 
       live = live - 1  


    if live == 0 :
       alive = False
       print("DEAD")

    if contador == 3 :
       contador = 0 
       estado = estado +1  
       print("GANADOR")
    

if __name__ == '__main__':
  _main()