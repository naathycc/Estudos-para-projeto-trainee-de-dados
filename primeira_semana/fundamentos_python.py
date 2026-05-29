# ==========================================
# EXERCÍCIO 1.1 - CRIANDO VARIÁVEIS E VERIFICANDO TIPOS
# ==========================================

# Crie variáveis para armazenar:
# - Seu nome
# - Sua idade
# - Sua altura
# - Se você é estudante ou não
#
# Depois:
# 1. Exiba o valor de cada variável
# 2. Exiba o tipo de cada variável usando type()

nome = "Nathalia"
idade = 23
altura = 1.60
estudante = True
print("Nome: ",nome)
print("Tipo: ",type(nome))
print("Idade: ",idade)
print("Tipo: ",type(idade))
print("Altura: ",altura)
print("Tipo: ",type(altura))
print("É estudante?: ",estudante)
print("Tipo: ",type(estudante))



# ==========================================
# EXERCÍCIO 1.2 - FORMULÁRIO DE CADASTRO
# ==========================================

# Peça ao usuário para digitar:
# - Nome
# - Idade
# - Cidade
#
# Depois exiba:
# Cadastro realizado:
# Nome: ...
# Idade: ...
# Cidade: ...

Nome = input("Por favor, digite seu nome: ")
Idade = input("Digite a sua idade: ")
Cidade = input("Digite a sua cidade: ")
print("Cadastro realizado")
print("Nome: ",Nome)
print("Idade: ",Idade)
print("Cidade: ",Cidade)

# ==========================================
# EXERCÍCIO 1.3 - CALCULADORA DE IMC
# ==========================================

# Solicite ao usuário:
# - Peso (kg)
# - Altura (m)
#
# Calcule:
# IMC = peso / altura ** 2
#
# Exiba o resultado com duas casas decimais.
peso = float(input("Digite o seu peso(kg): "))
altura = float(input("Digite a sua altura(m): "))
IMC = peso / altura ** 2
print(f"O seu IMC é: {IMC:.2f}")

# ==========================================
# EXERCÍCIO 2.1 - TRANSFORMAÇÕES DE TEXTO
# ==========================================

# Solicite uma frase ao usuário.
#
# Exiba:
# 1. Toda em maiúsculo
# 2. Toda em minúsculo
# 3. Quantidade de caracteres
# 4. Quantidade de palavras

frase = input("Digite uma frase: ")
print(frase.upper())
print(frase.lower())
print(len(frase))
print(len(frase.split()))


# ==========================================
# EXERCÍCIO 2.2 - VALIDADOR DE EMAIL
# ==========================================

# Solicite um email.
#
# Verifique se ele possui:
# - "@"
# - "."
#
# Se possuir ambos:
# Email válido
#
# Caso contrário:
# Email inválido

email = input("Digite seu email: ")

if "@" in email and "." in email:
  print("Email válido")
else:
  print("Email inválido")
  


# ==========================================
# EXERCÍCIO 2.3 - EXTRAINDO INFORMAÇÕES DE UMA STRING
# ==========================================

# Solicite o nome completo do usuário.
#
# Exiba:
# - Nome completo
# - Quantidade de caracteres
# - Primeiro caractere
# - Último caractere
# - Nome em maiúsculo

nomeinteiro = input("Digite o seu nome completo: ")
print("Nome completo: ",nomeinteiro)
print("Quantidade de caracteres: ",len(nomeinteiro))
print("Primeiro caractere: ",nomeinteiro[0])
print("Último caractere: ",nomeinteiro[-1])
print("Nome em maiúsculo ",nomeinteiro.upper())


# ==========================================
# EXERCÍCIO 3.1 - CALCULADORA DE OPERAÇÕES ARITMÉTICAS
# ==========================================

# Solicite dois números.
#
# Exiba:
# - Soma
# - Subtração
# - Multiplicação
# - Divisão
# - Potência

primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
print("Soma: ",primeiro + segundo)
print("Subtração: ",primeiro - segundo)
print("Multiplicação: ",primeiro * segundo)
print("Divisão: ",primeiro / segundo)
print("Potência: ",primeiro ** segundo)

# ==========================================
# EXERCÍCIO 3.3 - SISTEMA DE VALIDAÇÃO COM OPERADORES LÓGICOS
# ==========================================

# Solicite:
# - Idade
# - Possui CNH? (sim/não)
#
# Verifique se a pessoa pode dirigir.
#
# Condições:
# - Ter 18 anos ou mais
# - Possuir CNH
#
# Exiba o resultado.

age = int(input("Digite a sua idade "))
cnh = (input("Digite se você tem CNH "))

if age >= 18 and (cnh=="sim" or cnh=="Sim"):
  print("Você pode dirigir")
else: 
  print("Você não pode dirigir")


# ==========================================
# EXERCÍCIO 3.4 - CALCULADORA DE DESCONTO PROGRESSIVO
# ==========================================

# Solicite o valor da compra.
#
# Regras:
# Até R$100 -> sem desconto
# Acima de R$100 -> 10% de desconto
# Acima de R$500 -> 20% de desconto
#
# Exiba:
# - Valor original
# - Desconto aplicado
# - Valor final

valor = float(input("Digite o valor da compra: "))

if valor <= 100:
  desconto = 0
elif valor > 100 and valor <= 500:
  desconto = valor*0.10
else:
  desconto = valor*0.20

print("Valor original: ",valor)
print("Desconto: ",desconto)
print("Valor com desconto: ",valor - desconto)

  

# ==========================================
# EXERCÍCIO 4.1 - CLASSIFICADOR DE IDADE
# ==========================================

# Solicite a idade do usuário.
#
# Classifique como:
#
# Criança -> até 12 anos
# Adolescente -> 13 a 17 anos
# Adulto -> 18 a 59 anos
# Idoso -> 60 anos ou mais
#
# Exiba a classificação correspondente.

IDADE = int(input("Digite a sua idade: "))
if IDADE <= 12:
  print("É criança!")
elif IDADE > 12 and IDADE <= 17:
  print("É adolescente!")
elif IDADE > 17 and IDADE <= 59:
  print("É adulto")
else:
  print("É idoso")


# ==========================================
# EXERCÍCIO 4.2 - GERADOR DE TABUADA
# ==========================================

# Solicite um número ao usuário.
#
# Utilize um laço for para exibir a tabuada
# desse número de 1 até 10.

tabuada = int(input("Digite a tabuada que você quer ver: "))

for i in range(1,11):
  print(f"{tabuada} X {i} = {tabuada * i}")


# ==========================================
# EXERCÍCIO 4.3 - VALIDADOR DE SENHA COM WHILE
# ==========================================

# Solicite uma senha repetidamente até que ela seja válida.
#
# A senha deve:
#
# - Ter pelo menos 8 caracteres
# - Possuir pelo menos uma letra maiúscula
# - Possuir pelo menos uma letra minúscula
# - Possuir pelo menos um número
#
# Enquanto a senha não for válida:
# Exiba:
#
# "Senha inválida! Tente novamente."
#
# Quando for válida:
#
# "Senha válida! Cadastro realizado com sucesso."

while True:
    senha = input("Digite uma senha: ")

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True

        if caractere.islower():
            tem_minuscula = True

        if caractere.isdigit():
            tem_numero = True

    if len(senha) >= 8 and tem_maiuscula and tem_minuscula and tem_numero:
        print("Senha válida! Cadastro realizado com sucesso.")
        break
    else:
        print("Senha inválida! Tente novamente.")