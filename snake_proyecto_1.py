import random

matriz= []

numTablero = int(input("ingrese el tamaño del tablero:  "))
cantidadManzanas = 1
cantidadOstaculos = 2

for f in range(numTablero):
    matriz.append(['*'] * numTablero ) #espacios en blanco

x = 0
while  x < cantidadOstaculos / 2:
  fila = random.randint(0, numTablero - 2)
  columna = random.randint(0, numTablero - 2)

  matriz[fila][columna] = 'X' 
  matriz[fila][columna + 1] = 'X'
  matriz[fila + 1][columna] = 'X'
  matriz [fila + 1][columna + 1] = 'X'

  x = x + 1 

b = 0
while  b < cantidadManzanas:
  fila = random.randint(0, numTablero - 2)
  columna = random.randint(0, numTablero - 2)
  while matriz[fila][columna] == 'X':
        fila = random.randint(0, numTablero - 2)
        columna = random.randint(0, numTablero - 2)

  matriz[fila][columna] = 'O' 
  b = b + 1

#repeticion aleatoria

   # imprimir juego
if numTablero >= 4:
 print(" ----" + numTablero * "----" )
 for fila in matriz:
  print("|" + " ".join(f"{x:3} " for x in fila) + '|')

print(" ----" + numTablero * "----" )

if numTablero < 4:
  print("El minino de juego debe de ser 4 filas y 4 columnas")

