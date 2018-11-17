import networkx as nx
import random
import copy

	
#colore os vertices
def AcListC(grafo, x, y, cor):
	Remove(grafo, y, cor)
	retorno = Compara(grafo)
  
	if len(grafo.node) == Falta(grafo):
		retorno = True
	i = 0
	if not retorno:
		try:
			auxiliar = copy.deepcopy(grafo.node[x]['cor'])
			while not retorno and i<len(grafo.node[x]['cor']):
				grafo.node[x]['cor'] = auxiliar[i]
				grafo.node[x]['estado'] = True
				vertice = AcharFalso(grafo)
				retorno = AcListC(grafo, vertice, x, auxiliar[i])
				if retorno:
				  solucao.append(auxiliar[i])
				  
				i = i+1
		except:
			pass
	return retorno
#retorna um vertice que esteja com o estado falso
def AcharFalso(grafo):
	for x in sorted(grafo.node):
		if grafo.node[x]['estado'] == False:
			return x
#retorna verdadeiro caso o vertice esteja com o estado falso
def Compara(grafo):
    for x in grafo.node:
        if grafo.node[x]['cor'] == []:
            return True
    return False
#atualiza o estado do vertice para verdadeiro caso a lista de cores tenha tamanho 1
#
def Atualizar(grafo):
    for node in grafo.node:
        if not grafo.node[node]['estado'] and len(grafo.node[node]['cor']) == 1:
            grafo.node[node]['estado'] = True
            grafo.node[node]['cor'] = grafo.node[node]['cor'][0]
            Remove(grafo, node, grafo.node[node]['cor'])
#tenta retirar a cor de um vertice nos seus vizinhos
def Checar(grafo):
	for x in sorted(grafo.node):
		for i in sorted(grafo.neighbors(x)):
			if grafo.node[i]['estado']:
				try:
					grafo.node[x]['cor'].remove(grafo.node[i]['cor'])
				except:
					pass

def Falta(grafo):
	a = len(grafo.node)
	for x in grafo.node:
		if grafo.node[x]['estado']:
			a = a+1
	return a

#remove a cor do vertice passado como parametro dos seus vizinhos
def Remove(grafo, x, cor):
	if cor != ' ':
		for i in sorted(grafo.neighbors(x)):
			if not grafo.node[i]['estado']:
				if grafo.node[x]['cor'] in grafo.node[i]['cor']:
					grafo.node[i]['cor'].remove(grafo.node[x]['cor'])
		Atualizar(grafo)

#imprime o grafo na forma do sudoku
def printG(grafo):
	print 'Sudoku resolvido:\n'
	for x in range(ordem):
		for y in range(ordem):
			print grafo.node[v[x][y]]['cor'],
		print

def printSudokuInicial(tabSudoku):
	print 'Sudoku Inicial:\n'
	for x in range(ordem):
		for y in range(ordem):
			print tabSudoku[x][y],
		print 
	print '\n'


#inicio


#Cada um dos 9 elementos dessa lista representa uma linha do sudoku que foi proposto a ser resolvido
entrada = ['e 2 e 5 e 1 e 9 e', '8 e e 2 e 3 e e 6', 'e 3 e e 6 e e 7 e', 'e e 1 e e e 6 e e', '5 4 e e e e e 1 9', 'e e 2 e e e 7 e e', 'e 9 e e 3 e e 8 e', '2 e e 8 e 4 e e 7', 'e 1 e 9 e 7 e 6 e']

#matriz com os vertices que representam as celulas do sudoku
v= [['00','01','02','03','04','05','06','07','08'],
    ['10','11','12','13','14','15','16','17','18'],
    ['20','21','22','23','24','25','26','27','28'],
    ['30','31','32','33','34','35','36','37','38'],
    ['40','41','42','43','44','45','46','47','48'],
    ['50','51','52','53','54','55','56','57','58'],
    ['60','61','62','63','64','65','66','67','68'],
    ['70','71','72','73','74','75','76','77','78'],
    ['80','81','82','83','84','85','86','87','88']]

#matriz que possui os vertices que sao adjacentes nas regioes 3x3	
regioes = [['00', '01', '02', '10', '11', '12', '20', '21', '22'], ['03', '04', '05', '13', '14', '15', '23', '24', '25'], ['06', '07', '08', '16', '17', '18', '26', '27', '28'], ['30', '31', '32', '40', '41', '42', '50', '51', '52'], ['33', '34', '35', '43', '44', '45', '53', '54', '55'], ['36', '37', '38', '46', '47', '48', '56', '57', '58'], ['60', '61', '62', '70', '71', '72', '80', '81', '82'], ['63', '64', '65', '73', '74', '75', '83', '84', '85'], ['66', '67', '68', '76', '77', '78', '86', '87', '88']]


#calculo da ordem do sudoku
ordem = len(entrada)

#criando o grafo
grafo = nx.Graph()

#criando a matriz com os valores do sudoku
tabSudoku = []
for linha in entrada:
	tabSudoku.append(linha.split(' '))

#criando os vertices com as cores e os seus estados
for x in range(0, ordem):
    for y in range(0, ordem):
        if tabSudoku[x][y] == 'e':
            grafo.add_node(v[x][y], cor = [1, 2, 3, 4, 5, 6, 7, 8, 9], estado = False)
        else:
            grafo.add_node(v[x][y], cor = int(tabSudoku[x][y]), estado = True)

#criando as arestas em relacao as linhas
for x in range(0, ordem):
	for y in range(0, ordem-1):
		for z in range(y+1, ordem):
			grafo.add_edge(v[x][y], v[x][z])

#criando as arestas em relacao as colunas
for x in range(0, ordem):
	for y in range(0, ordem-1):
		for z in range(y+1, ordem):
			grafo.add_edge(v[y][x], v[z][x])


#criando as arestas em relacao as regioes
for x in range(0, ordem):
	for y in range(0, ordem-1):
		for z in range(y+1, ordem):
			grafo.add_edge(regioes[x][y], regioes[x][z])


#chamada das funcoes para resolucao do Sudoku
printSudokuInicial(tabSudoku)
Checar(grafo)
Atualizar(grafo)
vertice_inicial = AcharFalso(grafo)
AcListC(grafo, vertice_inicial, vertice_inicial, ' ')
printG(grafo)
