#Comando com controle de cadastro 
#
#total = int(input("Digite quantos alunos você quer calcular: "))
#cont = 1
#
#while cont <= total:
#
#    nome = input("Nome: ")
#    n1 = float(input("Nota da primeira prova: "))
#    n2 = float(input("Nota da segunda prova: "))
#
#    media = round((n1 + n2) / 2,1)
#    if media > 7:
#       print(f"O aluno (nome) %s foi aprovado com media %.2f" % (nome, media))
#    else:
#        print(f"O aluno (nome) %s foi reprovado com media %2f" % (nome, media))
#
#    cont += 1
#
#
#
#Comando com brake
#
#total = int(input("Digite quantos alunos você quer calcular: "))
#cont = 1
#
#while cont <= total:
#
#    nome = input("Nome: ")
#    if nome == '-1':
#        break
#    n1 = float(input("Nota da primeira prova: "))
#    n2 = float(input("Nota da segunda prova: "))
#
#    media = round((n1 + n2) / 2,1)
#    if media > 7:
#       print(f"O aluno (nome) %s foi aprovado com media %.2f" % (nome, media))
#    else:
#        print(f"O aluno (nome) %s foi reprovado com media %2f" % (nome, media))
#
#    cont += 1



#cont = 1
#soma = 0
#total = int(input("Digite quantos produtos você quer comprar: "))
#while cont <= total:
#    
#    valproduto = int(input("Digite o valor do seu Produto em R$: "))
#    soma += valproduto
#    cont += 1
#
#print("A soma de seus produtos é R$ %d" % soma)

total = 3
cont = 1
while True:
    nome = input("nome: ")
    if len(nome) == 0:
        continue
    if nome =='-1':
        break
    n1 = float(input("Nota da primeira prova: "))
    n2 = float(input("Nota da segunda prova: "))

    media = round((n1 + n2) / 2,1)
    if media > 7:
       print(f"O aluno (nome) %s foi aprovado com media %.2f" % (nome, media))
    else:
        print(f"O aluno (nome) %s foi reprovado com media %2f" % (nome, media))

    cont += 1













