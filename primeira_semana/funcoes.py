# ==========================================
# TÓPICO 1 - INTRODUÇÃO A FUNÇÕES
# ==========================================

# EXERCÍCIO 1.1
#
# Crie uma função chamada cumprimentar
# que imprime:
#
# "Olá! Bem-vindo ao Python!"
#
# Depois chame a função duas vezes.

def cumprimentar():
  print("Olá! Bem-vindo ao Python!")

cumprimentar()
cumprimentar()


# EXERCÍCIO 1.2
#
# Crie uma função chamada
# calcular_area_retangulo
#
# A função deve:
# 1. Solicitar a largura
# 2. Solicitar a altura
# 3. Calcular a área
# 4. Exibir o resultado
#
# Exemplo:
#
# Largura: 5
# Altura: 3
#
# A área do retângulo é: 15

def calcular_area_retangulo(largura, altura):
  area = 0
  area = largura * altura
  return area

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
print("A área é: ",calcular_area_retangulo(largura,altura))


# EXERCÍCIO 1.3
#
# Crie as funções:
#
# exibir_menu()
# mensagem_boas_vindas()
# mensagem_despedida()
# mensagem_personalizada()
#
# O menu deve ter:
#
# 1 - Boas-vindas
# 2 - Despedida
# 3 - Personalizada
# 4 - Sair
#
# Utilize while True para repetir
# até o usuário escolher sair.

def exibir_menu():
  print("1 - Boas-vindas")
  print("2 - Despedida")
  print("3 - Personalizada")
  print("4 - Sair")

def mensagem_boas_vindas():
  print("Olá! boas-vindas!")

def mensagem_despedida():
  print("Adeus! Até logo!")

def mensagem_personalizada(nome):
  print("Olá ",nome,"Tudo bem com você?")


exibir_menu()
resposta = input("Digite o que você deseja: ")
while resposta != '4':
  if resposta == '1':
    mensagem_boas_vindas()
  elif resposta == '2':
    mensagem_despedida()
  elif resposta == '3':
    user = input("Qual o seu nome? ")
    mensagem_personalizada(user)
  
  resposta = input("Digite o que você deseja: ")

# ==========================================
# TÓPICO 2 - FUNÇÕES COM PARÂMETROS
# ==========================================

# EXERCÍCIO 2.1
#
# Crie uma função:
#
# apresentar_pessoa(nome)
#
# Exiba:
#
# "Olá, meu nome é [nome]!"
#
# Teste com:
# Ana
# Carlos
# Maria

def apresentar_pessoa(nome):
  print("Olá, meu nome é:",nome,"!")

apresentar_pessoa('Ana')
apresentar_pessoa('Carlos')
apresentar_pessoa('Maria')

# EXERCÍCIO 2.2
#
# Crie uma função:
#
# calcular_media(nota1, nota2, nota3)
#
# A função deve calcular
# a média das três notas.
#
# Teste:
#
# 8.5
# 7.0
# 9.5

def calcular_media(nota1, nota2, nota3):
  media = (nota1 + nota2 + nota3) / 3
  return media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

print("A sua média ficou: ", calcular_media(nota1, nota2, nota3))




# EXERCÍCIO 2.3
#
# Crie uma função:
#
# somar_numeros(*args)
#
# A função deve somar todos
# os números recebidos.
#
# Teste:
#
# somar_numeros(1, 2, 3)
# somar_numeros(10, 20, 30, 40, 50)
# somar_numeros(5)

def somar_numeros(*args):
  soma = 0
  for i in args:
    soma = soma + i
  return soma

print("A soma ficou: ",somar_numeros(1, 2, 3))
print("A soma ficou: ",somar_numeros(10, 20, 30, 40, 50))
print("A soma ficou: ",somar_numeros(5))


# ==========================================
# TÓPICO 3 - RETURN
# ==========================================

# EXERCÍCIO 3.1
#
# Crie uma função:
#
# dobro(numero)
#
# Ela deve retornar
# o dobro do número.
#
# Teste:
#
# 5
# 10
# 15

def dobro(numero):
  return numero * 2

print("O dobro de 5 é: ",dobro(5))
print("O dobro de 10 é: ",dobro(10))
print("O dobro de 15 é: ",dobro(15))

# EXERCÍCIO 3.2
#
# Crie uma função:
#
# gerar_numeros_pares(n)
#
# Ela deve retornar
# uma lista contendo os
# primeiros n números pares.
#
# Teste:
#
# n = 5
# n = 10

def gerar_numeros_pares(n):
    pares = []

    for i in range(n):
        pares.append(i * 2)
    return pares

print("Os primeiros 5 números pares são: ", gerar_numeros_pares(5))
print("Os primeiros 10 números pares são: ", gerar_numeros_pares(10))


# EXERCÍCIO 3.3
#
# Crie uma função:
#
# criar_produto(nome, preco, quantidade)
#
# Ela deve retornar um
# dicionário contendo:
#
# nome
# preco
# quantidade
# total
#
# onde:
#
# total = preco * quantidade

def criar_produto(nome, preco, quantidade):
    produto = {
    'nome': nome,
    'preco': preco,
    'quantidade': quantidade,
    'total': preco * quantidade 
     }
    return produto

produto1 = criar_produto("Celular", 3000, 5)
produto2 = criar_produto("Notebook", 6000, 2)

print(produto1)
print(produto2)
    


# EXERCÍCIO 3.4
#
# Crie as funções:
#
# somar(a, b)
# subtrair(a, b)
# multiplicar(a, b)
# dividir(a, b)
#
# Depois crie:
#
# calcular(num1, num2, operacao)
#
# A função deve escolher
# qual operação executar.
#
# Trate divisão por zero.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def calcular(num1, num2, operacao):
    if operacao == "+":
        return somar(num1, num2)

    elif operacao == "-":
        return subtrair(num1, num2)

    elif operacao == "*":
        return multiplicar(num1, num2)

    elif operacao == "/":
        return dividir(num1, num2)

    else:
        return "Operação inválida"

print(calcular(2, 3, "+"))
print(calcular(10, 5, "-"))
print(calcular(20, 10, "*"))
print(calcular(25, 5, "/"))
