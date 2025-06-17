print("####### BEM VINDO AO ANALISADOR DE NOTAS ESCOLARES #######")
#--------------------ENTRADA DOS DADOS---------------------#

nomes=["Luana", "Pedro", "Augusto", "Carlos", "Elisa"]
notas=[]

for i in range(len(nomes)): #### Cria um índice para cada item da lista nomes
    nota = float(input(f"Digite a nota de {nomes[i]}:")) #### Atribui o valor de input à mesma posição do índice atual
    notas.append(nota) #### Adiciona o valor do input à lista notas

#------------------TRATAMENTO DOS DADOS--------------------#

qntAlunos=0
somaNotas=0
for valor in notas:
    qntAlunos += 1
    somaNotas += valor

media=(somaNotas/qntAlunos)

#------------SELECIONA APROVADOS E REPROVADOS--------------#

reprovado=[]
aprovado=[]
for notaAluno in notas:
    if notaAluno < 5 :
        reprovado.append(notaAluno)
    else:
        aprovado.append(notaAluno)

pctAprovados=int(len(aprovado)/(qntAlunos)*100)
pctReprovados=int(len(reprovado)/(qntAlunos)*100)

#-----------APRESENTA OS RESULTADOS A ANÁLISE--------------#

print("O total de alunos é:" , qntAlunos)
print(f"A nota média dos alunos é: {media:.1f}")
print("O total de alunos aprovados é: ", len(aprovado))
print("O total de alunos reprovados é: ", len(reprovado))
print(f"A procentagem de aprovados foi de: {pctAprovados}%")
print(f"A procentagem de reprovados foi de: {pctReprovados}%")
print(f"Os alunos aprovados foram: {aprovado}")
print(f"Os alunos reprovados foram: {reprovado}")
