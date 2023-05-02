# Este año los elfos han comprado una máquina que envuelve regalos. Pero...
# ¡no viene programada! Necesitamos crear un algoritmo que le ayude en la
# tarea. A la máquina se le pasa un array con los regalos. Cada regalo es un
# string. Necesitamos que la máquina envuelva cada regalo en papel de regalo
# y lo coloque en un array de regalos envueltos. El papel de regalo es el
# símbolo * y para envolver un regalo se coloca el símbolo * de forma que
# rodee totalmente al string por todos los lados. Por ejemplo:

regalo1=input("Regalo 1:")
regalo2=input("Regalo 2:")
regalo3=input("Regalo 3:")
regalo4=input("Regalo 4:")
regalo5=input("Regalo 5:")

print("Empaquetado realizado")

listaRegalos=(regalo1,regalo2,regalo3,regalo4)
for regalo in listaRegalos:
    print(f"*****{regalo}*****")