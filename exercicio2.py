# Exercício 2: Dados três valores distintos, fazer um algoritmo que, após a leitura destes dados imprima-os em ordem crescente.


def entrada(frase: str) -> float:
    ''' Função exige entrada de decimais com tratamento de valores. 
    Parâmetros
    ----------
    frase: mensagem a ser exibida ao solicitar entrada de dados.

    Retorno
    -------
    valor: valor decimal de entrada.

    '''

    while(True):
        try:
            valor = float(input(frase))
        except ValueError:
            print('Por favor, informe um valor do tipo numérico!\n')
            continue
        except:
            print(
                'Ocorreu um erro inesperado durante a leitura, por favor insira o valor novamente.')
            continue
        else:
            return valor


def ordernar(valores: list) -> list:
    ''' Ordena lista de números de forma crescente. 
    Parâmetros
    ----------
    valores: lista de 3 valores a serem ordenados.

    Retorno
    -------
    lista: lista contendo os três valores ordenados de forma crescente.

    '''
    maior = valores[0]
    menor = valores[0]
    meio = valores[0]
    for valor in valores:
        maior = maior if maior > valor else valor
        menor = menor if menor < valor else valor
    for valor in valores:
        meio = valor if ((valor != maior) and (valor != menor)) else meio
    return [menor, meio, maior]


# Lista de valores recebidos.
valores = [
    entrada('Digite o primeiro valor: '),
    entrada('Digite o segundo valor: '),
    entrada('Digite o terceiro valor: ')
]

# Exibição do resultado
print('Em ordem crescente:', ordernar(valores))
