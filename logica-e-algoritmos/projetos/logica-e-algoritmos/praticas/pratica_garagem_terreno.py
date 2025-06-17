largura_garagem = float(input("Entre com a largura da garagem em metros:"))
profundidade_garagem=float(input("Entre com a profundidade da garagem em metros:"))

area_garagem=largura_garagem * profundidade_garagem ###### Cálculo da área da garagem

largura_terreno=float(input("Entre com a largura do terreno em metros:"))
profundidade_terreno=float(input("Entre com a profundidade do terreno em metros:"))

area_terreno=largura_terreno*profundidade_terreno ###### Cálculo da área do terreno

percentual=(area_garagem/area_terreno)*100 ###### Cálculo do percentural de ocupação da garagem
##### print(f"O percentual de ocupação da garagem é: {percentual:.2f}%")

zona_cidade = input("Entre com a zona da cidade onde o terreno se encontra:")
taxa_percentual = 0
taxa_zona_norte = int(25)
taxa_zona_leste_oeste = int(30)
taxa_zona_sul = int(40)

if zona_cidade == "norte":
    taxa_percentual = taxa_zona_norte
elif zona_cidade in ("leste", "oeste"):
    taxa_percentual = taxa_zona_leste_oeste
elif zona_cidade == "sul":
    taxa_percentual = taxa_zona_sul
else:
    print("A construção está proibida")
    taxa_percentual = None

if taxa_percentual is not None:
    if percentual > taxa_percentual:
        print("A construção está proibida")
    else:
        print("A construção foi liberada")