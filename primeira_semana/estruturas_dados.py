# ==========================================
# TÓPICO 1 - LISTAS
# ==========================================

# EXERCÍCIO 1.1 - CRIANDO E ACESSANDO LISTAS
#
# Crie uma lista chamada frutas com:
# ['maçã', 'banana', 'laranja', 'uva', 'morango']
#
# 1. Exiba o primeiro elemento
# 2. Exiba o último elemento
# 3. Exiba o terceiro elemento
# 4. Verifique se 'banana' está na lista usando in
# 5. Modifique o segundo elemento para 'abacaxi'

frutas = ['maçã', 'banana', 'laranja', 'uva', 'morango']
print("Primeiro elemento: ",frutas[0])
print("Último elemento: ",frutas[-1])
print("Terceiro elemento: ",frutas[2])
if 'banana' in frutas:
  print("Tem banana!")

print("Antes: ",frutas)
frutas[1] = 'abacaxi'
print("Depois: ",frutas)
  


# EXERCÍCIO 1.2 - MANIPULANDO LISTAS COM MÉTODOS
#
# Lista inicial:
# ['arroz', 'feijão', 'macarrão']
#
# 1. Adicione 'açúcar' usando append()
# 2. Insira 'óleo' na posição 1 usando insert()
# 3. Crie:
#    outros_itens = ['sal', 'pimenta']
#    e adicione usando extend()
# 4. Remova 'macarrão' usando remove()
# 5. Remova o último elemento usando pop()
#    e armazene em uma variável
# 6. Exiba o tamanho usando len()

#%%
alimentos = ['arroz', 'feijão', 'macarrão']
print(alimentos)
alimentos.append("açúcar")
alimentos.insert(1,"óleo")
outros_itens = ['sal', 'pimenta']
print(outros_itens)
alimentos.extend(outros_itens)
alimentos.remove('macarrão')
removida = alimentos.pop(0)
print(removida)
print(len(alimentos))
print(alimentos)





# EXERCÍCIO 1.3 - PERCORRENDO E FATIANDO LISTAS
#
# notas = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5]
#
# 1. Percorra usando:
#    for item in lista
#
# 2. Percorra usando:
#    for x in range(len(lista))
#
# 3. Obtenha os 3 primeiros elementos
# 4. Obtenha os 3 últimos elementos
# 5. Obtenha elementos de 2 em 2
# 6. Inverta a lista usando fatiamento

#%%
notas = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5]
for item in notas:
  print(notas)

for i in range(len(notas)):
    print(notas[i])

print(notas[:3])
print(notas[-3:])

print(notas[::2])
print(notas[::-1])



# EXERCÍCIO 1.4 - LISTAS ANINHADAS
#
# Crie:
#
# alunos = [
#     ['Nome', 'Idade', 'Nota'],
#     ['Ana', 20, 8.5],
#     ['Bruno', 19, 7.0],
#     ['Carla', 21, 9.0],
#     ['Diego', 20, 6.5]
# ]
#
# 1. Exiba a idade de Bruno
# 2. Exiba a nota de Carla usando índice negativo
# 3. Modifique a nota de Diego para 7.5
# 4. Percorra toda a matriz usando laços aninhados
# 5. Exiba:
#    "Nome tem idade anos e nota nota"
# 6. Adicione:
#    ['Elena', 22, 8.0]

alunos = [
 ['Nome', 'Idade', 'Nota'],
 ['Ana', 20, 8.5],
 ['Bruno', 19, 7.0],
 ['Carla', 21, 9.0],
 ['Diego', 20, 6.5]
]

print("Idade do Bruno: ",alunos[2][1])
print("Nota de Carla: ",alunos[3][-1])
alunos[-1][-1] = 7.5 

for aluno in alunos:
   for item in aluno:
      print(item)

for aluno in alunos[1:]:
    print(f"{aluno[0]} tem {aluno[1]} anos e nota {aluno[2]}")

alunos.append(["Elena", 22, 8.0])

print(alunos)


# ==========================================
# TÓPICO 2 - TUPLAS
# ==========================================

# EXERCÍCIO 2.1 - CRIANDO E ACESSANDO TUPLAS
#
# coordenadas = (10, 20, 30)
#
# 1. Exiba a tupla
# 2. Exiba o tipo
# 3. Exiba o primeiro elemento
# 4. Exiba o último elemento
# 5. Verifique se 20 está na tupla
# 6. Exiba o tamanho

coordenadas = (10, 20, 30)
print(coordenadas)
print(type(coordenadas))
print("Primeiro elemento: ",coordenadas[0])
print("Último elemento: ",coordenadas[-1])

if 20 in coordenadas:
    print("20 está na tupla!")

print("O tamanho da tupla é: ",len(coordenadas))


# EXERCÍCIO 2.3 - OPERAÇÕES COM TUPLAS
#
# frutas1 = ('maçã', 'banana', 'laranja')
# frutas2 = ('uva', 'morango', 'abacaxi', 'kiwi')
#
# 1. Concatene usando +
# 2. Percorra usando for
# 3. numeros = (1, 2, 3, 2, 4, 2, 5)
# 4. Conte quantas vezes o 2 aparece
# 5. Descubra o índice de 'abacaxi'
# 6. Exiba o tamanho da tupla

frutas1 = ('maçã', 'banana', 'laranja')
frutas2 = ('uva', 'morango', 'abacaxi', 'kiwi')
frutasall = frutas1 + frutas2
print(frutasall)

for frut in frutasall:
   print(frut)

numbers = (1, 2, 3, 2, 4, 2, 5)

cont = 0
for num in numbers:
    if num == 2:
        cont += 1


print("O 2 aparece: ",cont,"vezes")   
   
print(frutasall.index("abacaxi"))

print("O tamanho da tupla é: ",len(frutasall))

# ==========================================
# TÓPICO 3 - DICIONÁRIOS
# ==========================================

# EXERCÍCIO 3.1 - CRIANDO E ACESSANDO DICIONÁRIOS
#
# Crie:
#
# pessoa = {
#     'nome': 'Maria Silva',
#     'idade': 28,
#     'altura': 1.65,
#     'habilitado': True
# }
#
# 1. Exiba o dicionário
# 2. Exiba o tipo
# 3. Exiba cada valor individualmente
# 4. Modifique idade para 29
# 5. Adicione cidade = São Paulo
# 6. Exiba o tamanho

pessoa = {
 'nome': 'Maria Silva',
 'idade': 28,
 'altura': 1.65,
 'habilitado': True
}

print(pessoa)
print(type(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['habilitado'])
pessoa['idade'] = 29
pessoa['cidade'] = 'São Paulo'
print(pessoa['idade'])
print(pessoa['cidade'])
print(len(pessoa))

# EXERCÍCIO 3.2 - MANIPULANDO DICIONÁRIOS
#
# produto = {
#     'nome': 'Notebook',
#     'preco': 2500.00,
#     'estoque': 10
# }
#
# 1. Use get('preco')
# 2. Use get('desconto')
# 3. Verifique se estoque existe
# 4. Atualize preço para 2200
# 5. Adicione categoria = Eletrônicos
# 6. Remova estoque usando pop()
# 7. Use popitem()

produto = {
     'nome': 'Notebook',
     'preco': 2500.00,
     'estoque': 10
}

print(produto.get('preco'))
print(produto.get('desconto'))

if 'estoque' in produto:
    print("A chave estoque existe")

produto['preco'] = 2200
produto['categoria'] = 'Eletrônicos'
estoque_removido = produto.pop('estoque')
print(estoque_removido)
item_removido = produto.popitem()
print(item_removido)
print(produto)


# EXERCÍCIO 3.3 - PERCORRENDO DICIONÁRIOS
#
# aluno = {
#     'nome': 'João',
#     'idade': 22,
#     'curso': 'Engenharia',
#     'nota': 8.5
# }
#
# 1. Percorra as chaves
# 2. Percorra os valores
# 3. Percorra usando items()
# 4. Use keys()
# 5. Faça uma cópia usando copy()
# 6. Modifique a cópia e compare

aluno = {
    'nome': 'João',
    'idade': 22,
    'curso': 'Engenharia',
    'nota': 8.5
}

for chave in aluno:
    print(chave)

for valor in aluno.values():
    print(valor)

for chave, valor in aluno.items():
    print(chave, valor)

print(aluno.keys())

copia = aluno.copy()

copia['nome'] = 'Maria'

print(aluno)
print(copia)


# ==========================================
# TÓPICO 4 - CONJUNTOS (SETS)
# ==========================================

# EXERCÍCIO 4.1 - CRIANDO E MANIPULANDO CONJUNTOS
#
# frutas = {'banana', 'laranja', 'uva'}
#
# 1. Exiba o conjunto
# 2. Exiba o tipo
# 3. Adicione melancia
# 4. Tente adicionar banana novamente
# 5. Verifique se laranja existe
# 6. Remova uva
# 7. Use discard() para remover abacaxi
# 8. Exiba o tamanho

fruits = {'banana', 'laranja', 'uva'}
print(fruits)
print(type(fruits))
fruits.add('melancia')
print(fruits)
fruits.add('banana')
print(fruits)

if 'laranja' in fruits:
    print("Existe laranja no conjunto!")
else:
    print("Não existe laranja no conjunto!")

fruits.remove('uva')
print(fruits)
fruits.discard('abacaxi')
print(fruits)
print("Tamanho do conjunto: ",len(fruits))




# EXERCÍCIO 4.2 - OPERAÇÕES BÁSICAS COM CONJUNTOS
#
# conjunto1 = {'a', 'b', 'c'}
# conjunto2 = {'c', 'd', 'e'}
#
# 1. Faça update()
# 2. Crie conjunto3 = {'f', 'g'}
# 3. Faça update()
# 4. Remova 'a'
# 5. Faça discard('z')
# 6. Faça uma cópia
# 7. Limpe o original usando clear()

conjunto1 = {'a', 'b', 'c'}
conjunto2 = {'c', 'd', 'e'}

conjunto1.update(conjunto2)
print(conjunto1)

conjunto3 = {'f','g'}
conjunto1.update(conjunto3)
print(conjunto1)

conjunto1.remove('a')
print(conjunto1)

conjunto1.discard('z')

conjunto4 = conjunto1.copy()
print(conjunto4)
conjunto1.clear()
print(conjunto1)


# EXERCÍCIO 4.3 - TEORIA DE CONJUNTOS
#
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# C = {7, 8, 9, 10}
#
# 1. União (union e |)
# 2. Interseção (intersection e &)
# 3. Diferença (difference e -)
# 4. Diferença simétrica
# 5. Interseção entre B e C
# 6. União entre A, B e C

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {7, 8, 9, 10}

print("União entre A e B: ",A.union(B))
print("União entre B e C: ",B.union(C))
print("União entre A e C: ",A.union(C))
print("União entre A,B e C: ",A.union(B,C))
print("Intersecção entre A e B: ",A.intersection(B))
print("Intersecção entre B e C: ",B.intersection(C))
print("Intersecção entre A e C: ",A.intersection(C))
print("Diferença entre A e B: ",A.difference(B))
print("Diferença entre B e C: ",B.difference(C))
print("Diferença entre A e C: ",A.difference(C))
print("Diferença simétrica entre A e B: ",A.symmetric_difference(B))
print("Diferença simétrica entre B e C: ",B.symmetric_difference(C))
print("Diferença simétrica entre A e C: ",A.symmetric_difference(C))






