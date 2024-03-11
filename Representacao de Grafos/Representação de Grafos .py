import time


# Aqui cria-se o grafo
def criar_grafo(numero_vertices):
    print("Agora defina as conexões, insira quais os vertices conectados, sem o uso de virgulas, por exemplo: '1 4 7 24 9 11'")
    time.sleep(5)
    grafo = {i + 1: input("\nDigite quais vértices estão conectadas à vértice {}: ".format(i + 1)).split() for i in range(numero_vertices)}
    return grafo


# Aqui cria-se a lista de adjacencias
def lista_de_adjacencias(grafo):
    print("\nLista de Adjacências:")
    print("Vértice | Relacionamento (Vértices Conectados)")
    print("---------------------------")
    for vertice, ligacoes in grafo.items():
        print("   {}    |        {}".format(vertice, ', '.join(ligacoes)))
    print("---------------------------")
    time.sleep(5)


# Aqui cria-se a matriz de adjacencias
def matriz_de_adjacencias(grafo):
    numero_vertices = len(grafo)
    matriz = [[0] * numero_vertices for _ in range(numero_vertices)]

    for vertice, ligacoes in grafo.items():
        for ligacao in ligacoes:
            matriz[vertice - 1][int(ligacao) - 1] = 1

    print("\nMatriz de Adjacências:")
    for linha in matriz:
        print(" ".join(map(str, linha)))
    time.sleep(5)


# Aqui conta-se os graus dos vértices
def graus(grafo):
    print("\nGraus dos Vértices:")
    print("Vértice | Graus")
    print("-----------------")
    for vertice, ligacoes in grafo.items():
        grau = len(ligacoes)
        print("   {}    |    {}".format(vertice, grau))
    print("-----------------")
    time.sleep(10)


if __name__ == "__main__":
    try:
        # Aqui o usuário personaliza o seu grafo
        numero_vertices = int(input("Digite o número de vértices do seu grafo, use valores númericos: "))
        grafo_resultante = criar_grafo(numero_vertices)

        # Aqui o usuário escolhe como deseja vizualizar seu grafo, seja por matriz ou por lista
        print("\nComo você gostaria de ver seu grafo representado?")
        print("Se você quiser vê-lo como uma matriz de adjacencias, digite 'matriz'")
        print("Se você quiser vê-lo como uma lista de adjacencias, digite 'lista'")
        escolha = input("Digite aqui sua escolha: ")

        if escolha == 'lista':
            lista_de_adjacencias(grafo_resultante)
            graus(grafo_resultante)
            # Escolheu lista de adjacencias
            # Juntamente irá aparecer o numero de graus dos vertices

        elif escolha == 'matriz':
            matriz_de_adjacencias(grafo_resultante)
            graus(grafo_resultante)
            # Escolheu matriz de adjacencias
            # Juntamente irá aparecer o numero de graus dos vertices

        else:
            print("Escolha inválida. Por favor, digite 'lista' ou 'matriz'.")
            # Escolha inválida

    except ValueError:
        print("Por favor, insira um número inteiro para o número de vértices.")
        # Número inválido