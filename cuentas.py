import random 

def muliplicacion(estado):
  
    if estado is None :
        a = random.randint(1,10)
        b = random.randint(1,10)

    print(f"{a} x {b}")
    respuesta = int(input("Respuesta......"))

    if (a*b) == respuesta:
       return True
       




def _main() -> None:
  live = 3
  estado = None
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
       print("GANADOR")
       break
    

if __name__ == '__main__':
  _main()