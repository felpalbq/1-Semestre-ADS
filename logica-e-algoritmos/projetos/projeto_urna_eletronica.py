###### PROJETO SIMULADOR DE VOTAÇÃO ######
print("###### BEM VINDO AO SIMULADOR DE VOTAÇÃO ######")

candidatos=["João", "Maria", "Lucas", "Paulo"] #### LISTA DE CANDIDATOS 
eleitores=int(5) 
votoNulo=0
votoValido=0
votos_joao=0
votos_maria=0
votos_lucas=0
votos_paulo=0

print("Os candidatos são respectivamente:")
print("1 - João")
print("2 - Maria")
print("3 - Lucas")
print("4 - Paulo")

for votacao in range(eleitores): #### LAÇO PERGUNTA E RECEBE O VOTO DE CADA ELEITOR  
    voto = int(input("Para votar, digite o número do candidato desejado: "))
    if voto == 1: #### CONDICIONAL ATRIBUI VOTO AO CANDIDATO CORRESPONDENTE 
        votos_joao += 1 #### CONTADOR DE VOTOS DO CANDIDATO
        votoValido += 1 #### CONTADOR DE VOTOS VÁLIDOS
        print("Voto no candidato João confirmado com sucesso!")
    elif voto == 2:
        votos_maria += 1
        votoValido += 1
        print("Voto na candidata Maria confirmado com sucesso!")
    elif voto == 3:
        votos_lucas += 1
        votoValido += 1
        print("Voto no candidato Lucas confirmado com sucesso!")
    elif voto == 4:
        votos_paulo += 1
        votoValido += 1
        print("Voto no candidato Paulo confirmado com sucesso!")
    else:
        votoNulo += 1
        print("Seu número não corresponde a nenhum dos candidatos e será anulado")


print("###### RELATÓRIO FINAL DA ELEIÇÃO ######")
print(f"Total de eleitores: {eleitores}")
print(f"Votos Válidos: {votoValido}")
print(f"Votos Nulos: {votoNulo}")
print(f"Total de votos candidato João: {votos_joao}")
print(f"Total de votos candidato Maria: {votos_maria}")
print(f"Total de votos candidato Lucas: {votos_lucas}")
print(f"Total de votos candidato Paulo: {votos_paulo}")

if votos_joao > votos_maria and votos_joao > votos_lucas and votos_joao > votos_paulo: #### CONDICIONAIS COMPARANDO VALOR ENTRE CANDIDATOS
    print("Candidato João foi eleito!")
elif votos_maria > votos_joao and votos_maria > votos_lucas and votos_maria > votos_paulo:
    print("Candidata Maria foi eleita!")
elif votos_lucas > votos_joao and votos_lucas > votos_maria and votos_lucas > votos_paulo:
    print("Candidato Lucas foi eleito!")
elif votos_paulo > votos_joao and votos_paulo > votos_maria and votos_paulo > votos_lucas:
    print("Candidato Paulo foi eleito!")
else:
    print("Houve um empate!")