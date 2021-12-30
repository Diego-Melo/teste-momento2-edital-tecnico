# Exercício 1: Escreva um programa que, dado quatro valores, A, B, C e D, imprima o maior e o menor valor.


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


def comparar(valores: list) -> tuple:
    ''' Função que compara valores retornando o maior e menor valor.
    Parâmetros
    ----------
    valores: lista de valores que serão comparados entre si.

    Retorno
    -------
    (maior, menor): tupla de saida com seus valores correspondentes.

    '''
    maior = valores[0]
    menor = valores[0]
    for valor in valores:
        maior = maior if maior > valor else valor
        menor = menor if menor < valor else valor
    return maior, menor


# Lista de valores recebidos.
valores = [
    entrada('Digite o valor de A: '),
    entrada('Digite o valor de B: '),
    entrada('Digite o valor de C: '),
    entrada('Digite o valor de D: ')
]

# Definição dos dois maiores valores a partir da função
maior, menor = comparar(valores)

# Exibição dos resultados
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
