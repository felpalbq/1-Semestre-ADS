lista = (1, 2, 3, 4, 5) #### tupla
soma = 0
qntd = 0
for valor in lista: #### percorre cada item da tupla
    #### print("Valor atual: ", valor) mostra o que 'for in' faz
    soma += valor
    qntd += 1
print("Soma: ", soma)
print("Quantidade: ", qntd)
mediaDec = soma / qntd
mediaInt = int(soma / qntd)
print(f"Média (decimal):  {mediaDec:.1f}")
print("Média inteira:" , mediaInt)


nome = "Felipe" #### Ler a string, trazer a quantidade de caracteres e imprimir seu conteúdo
qntdLetras = 0
for letra in nome:
    qntdLetras += 1
print("A quantidade de letras é: ", qntdLetras)
print(letra)

for i in range(10): #### Criar uma lista com 10 itens
    print(i)

for numero in range(10): #### Criar uma lista e caso seja um número par (resto 0), imprima-o
    if numero % 2 == 0:
        print(numero)