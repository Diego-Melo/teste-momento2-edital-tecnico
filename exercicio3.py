# Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo.


def entrada(frase: str) -> int:
    ''' Função exige entrada de inteiros com tratamento de valores. 
    Parâmetros
    ----------
    frase: mensagem a ser exibida ao solicitar entrada de dados.

    Retorno
    -------
    valor: valor inteiro de entrada.

    '''

    while(True):
        try:
            valor = int(input(frase))
        except ValueError:
            print('Por favor, informe um valor do tipo inteiro!\n')
            continue
        except:
            print(
                'Ocorreu um erro inesperado durante a leitura, por favor insira o valor novamente.')
            continue
        else:
            return valor


# Entrada
numero = entrada("Digite um número para ser analisado: ")

# Formação da frase de saida
frase = "O número é "
frase += "par" if numero % 2 == 0 else "ímpar"  # Verifica se o número é par
frase += " e "

frase += "positivo." if numero > 0 else "negativo."  # Verifica se o número é positivo

# Exibição
print(frase)
