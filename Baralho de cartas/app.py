"""
Crie um código que simula um baralho de cartas.
O código deve conter as seguintes funções:
    gerar_baralho -> retorna um baralho novo. Parâmetros da função definem quantas cópias retornar
    (1 baralho, 2 baralhos,...), se o baralho deve conter coringas, e se deve ser embaralhado
    antes de ser retornado.

    mostrar_baralho -> exibe a quantidade de cartas no baralho e mostra quais são.
    dar as cartas -> distribui as cartas do baralho entre X jogadores, de forma que cada jogador recebe Y cartas.
    mostrar_jogadores -> exibe a quantidade de cartas na mão de cada jogador e mostra quais são.
"""

import random  # Importa o módulo random para embaralhar o baralho


def gerar_baralho(n_copias=2, coringas=True, embaralhado=True):
    """
    Gera um baralho de cartas.
    
    Parâmetros:
        - n_copias (int): Número de cópias do baralho.
        - coringas (bool): Se True, adiciona coringas ao baralho.
        - embaralhado (bool): Se True, embaralha o baralho antes de retorná-lo.
    
    Retorna:
        - Uma lista representando o baralho.
    """
    baralho = []
    
    # Define os naipes e números das cartas
    naipes = list('♠♣♥♦')
    numeros = list('A23456789') + ['10'] + list('JQK')
    
    # Cria o baralho com base na quantidade de cópias desejada
    for _ in range(n_copias):
        for naipe in naipes:
            for numero in numeros:
                carta = numero + naipe
                baralho.append(carta)
        
        # Adiciona os coringas se necessário
        if coringas:
            baralho.extend(['JOCKER_1', 'JOCKER_2'])
    
    # Embaralha o baralho se especificado
    if embaralhado:
        random.shuffle(baralho)
    
    return baralho


def mostrar_baralho(baralho):
    """Exibe a quantidade de cartas no baralho e lista todas as cartas."""
    print(f'Há {len(baralho)} cartas no baralho.')
    print('Cartas: ')
    print(' , '.join(baralho))


def dar_cartas(baralho, n_jogadores=4, n_cartas=5):
    """
    Distribui cartas do baralho entre os jogadores.
    
    Parâmetros:
        - baralho (list): Lista de cartas disponíveis.
        - n_jogadores (int): Número de jogadores.
        - n_cartas (int): Quantidade de cartas para cada jogador.
    
    Retorna:
        - Um dicionário com os jogadores e suas respectivas mãos.
    """
    jogadores = {}
    
    for i in range(n_jogadores):
        mao = []
        
        # Distribui as cartas para o jogador
        while len(mao) < n_cartas:
            cartas = baralho.pop(0)  # Remove a carta do topo do baralho
            mao.append(cartas)
        
        nome_jogador = f'Jogador {i + 1}'
        jogadores[nome_jogador] = mao
    
    return jogadores


def mostrar_jogadores(jogadores):
    """Exibe as cartas na mão de cada jogador."""
    for jogador, mao in jogadores.items():
        print(f'Há {len(mao)} cartas na mão do {jogador}')
        print('Cartas: ')
        
        for carta in mao:
            print(f' -> {carta}')


# Executa as funções
baralho = gerar_baralho()  # Gera um baralho
mostrar_baralho(baralho)  # Exibe o baralho

jogadores = dar_cartas(baralho)  # Distribui as cartas para os jogadores
mostrar_jogadores(jogadores)  # Exibe as cartas dos jogadores