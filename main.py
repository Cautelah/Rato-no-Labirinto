import numpy as np

solucao = 0
n= 3
movimentos_possiveis = [(0,1),(1,0)]
labirinto = np.array([[0] * n for i in range(n)])
labirinto = np.array([
   [ 0, -1,-1,-1]
  ,[ 0, 0,-1, 0]
  ,[ 0, 0,-1,-1]
  ,[-1, 0, 0, 0]
  ]
  )
n = len(labirinto)
inicial = (0,0)
final = (n-1,n-1)
labirinto[inicial]=1

def e_valido(labirinto, inicial, destino):
  inicial_x, inicial_y = inicial
  destino_x, destino_y = destino
  n = len(labirinto)
  if destino_x < 0 or destino_y < 0 or destino_x >= n or destino_y >= n:
    #se for fora dos limites
    return False
  if labirinto[destino_x][destino_y] < 0:
    #se for parede
    return False
  if labirinto[destino_x][destino_y] == 1:
    #se já cruzou
    return False
  return True

def pegar_proxima_casa(labirinto,atual,movimentos_possiveis):
  x,y = atual
  return [(x+i,y+j) for i,j in movimentos_possiveis if e_valido(labirinto, atual, (x+i,y+j))]


def solucionar(labirinto,inicial, final, movimentos_possiveis):
  global solucao
  if inicial == final:
    solucao += 1
    print("Solução ",solucao)
    print(labirinto)
    return True
  for i,j in pegar_proxima_casa(labirinto,inicial, movimentos_possiveis):
    labirinto[i][j] = 1
    solucionar(labirinto,(i,j),final, movimentos_possiveis)
    labirinto[i][j] = 0
  return False

solucionar(labirinto, inicial, final, movimentos_possiveis)