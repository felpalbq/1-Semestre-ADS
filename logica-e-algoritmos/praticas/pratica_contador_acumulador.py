numPrimos = []
for numero in range(20): #### Percorre uma lista com 20 algarismos
    div = 0 #### Zera a contagem de divisores a cada número
    for divisor in range(1, numero+1): #### Testa divisores de 1 até número atual
        if (numero % divisor) == 0: #### Condicional para resto da divisão entre o número atual e divisor atual 
            div += 1 #### Contador de números primos (resto da divisão por 1 e por si mesmo é igual a 0)
    if div == 2: #### Condicional para definir a próxima ação baseado no contador
        numPrimos.append(numero) #### Adiciona o valor de numero (elemento atual sendo lido) à lista numPrimos

print(numPrimos) #### Imprime lista de números primos              