import numpy as np
import math


n= 5
labirinto = np.array([[0] * n for i in range(n)])
#"""
labirinto = np.array(
  [
   [ 0,-2, 0, 0, 0, 0,-2, 0,-2, 0]
  ,[ 0,-2,-2,-2, 0, 0,-2, 0, 0, 0]
  ,[ 0,-2, 0, 0, 0, 0,-2, 0,-2, 0]
  ,[ 0,-2, 0,-2, 0, 0,-2, 0,-2, 0]
  ,[ 0, 0, 0,-2, 0, 0,-2, 0,-2, 0]
  ,[ 0,-2,-2,-2, 0, 0,-2, 0,-2, 0]
  ,[ 0,-2, 0, 0, 0, 0,-2, 0,-2, 0]
  ,[ 0,-2, 0, 0, 0, 0,-2, 0,-2, 0]
  ,[ 0,-2, 0,-2, 0, 0,-2, 0,-2, 0]
  ,[ 0, 0, 0,-2, 0, 0, 0, 0,-2, 0]
  ]
  )
#"""
n = len(labirinto)
inicial = (0,0)
final = (n-1,n-1)
labirinto[inicial]=1
solucao = 0
movimentos_possiveis = [(0,1),(1,0),(0,-1),(-1,0)]
caminho = 2

def e_valido(labirinto, inicial, destino):
  inicial_x, inicial_y = inicial
  destino_x, destino_y = destino
  n = len(labirinto)
  if destino_x < 0 or destino_y < 0 or destino_x >= n or destino_y >= n:
    #se for fora dos limites
    return False
  if labirinto[destino] < 0:
    #se for parede
    return False
  if labirinto[destino] > 0:
    #se já cruzou
    return False
  return True

def pegar_proxima_casa(labirinto,atual,movimentos_possiveis):
  x,y = atual
  return [(x+i,y+j) for i,j in movimentos_possiveis if e_valido(labirinto, atual, (x+i,y+j))]

def calcular_distancia(inicio, final):
  ini_x,ini_y = inicio
  fin_x,fin_y = final
  delta_x = fin_x - ini_x
  delta_y = fin_y - ini_y
  return math.sqrt(delta_x * delta_x + delta_y * delta_y)

def melhor_caminho(labirinto,atual, final,movimentos_possiveis):
  proximas = [(calcular_distancia((i,j),final),(i,j)) for i,j in pegar_proxima_casa(labirinto, atual,movimentos_possiveis)]
  return [(t[1]) for t in sorted(proximas)]

def solucionar(labirinto,inicial, final, movimentos_possiveis, caminho):
  global solucao
  if inicial == final:
    solucao += 1
    print("Solução ",solucao)
    print(labirinto)
    if solucao == 1:
      input()
    return True
  #for i,j in pegar_proxima_casa(labirinto,inicial, movimentos_possiveis):
  for i,j in melhor_caminho(labirinto, inicial, final,movimentos_possiveis):
    labirinto[i][j] = caminho
    solucionar(labirinto,(i,j),final, movimentos_possiveis,caminho+1)
    caminho -= 1
    labirinto[i][j] = 0
  return False

solucionar(labirinto, inicial, final, movimentos_possiveis,caminho)