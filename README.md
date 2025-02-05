# Baralho de Cartas

Este projeto simula um baralho de cartas com funcionalidades para gerar, exibir e distribuir cartas entre jogadores.

## Estrutura do Projeto

O código principal está localizado no arquivo `app.py`, dentro da pasta `Baralho de Cartas`.

## Funcionalidades

O programa contém as seguintes funções:

- **`gerar_baralho(n_copias=2, coringas=True, embaralhado=True)`**
  - Cria um baralho com um número especificado de cópias.
  - Pode incluir coringas (JOCKER_1 e JOCKER_2).
  - Pode ser embaralhado automaticamente.
  - Retorna uma lista representando o baralho.

- **`mostrar_baralho(baralho)`**
  - Exibe a quantidade de cartas no baralho e as cartas presentes nele.

- **`dar_cartas(baralho, n_jogadores=4, n_cartas=5)`**
  - Distribui um número especificado de cartas para um número específico de jogadores.
  - Retorna um dicionário onde as chaves são os jogadores e os valores são suas respectivas mãos.

- **`mostrar_jogadores(jogadores)`**
  - Exibe a quantidade de cartas de cada jogador e as cartas que eles possuem.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Navegue até a pasta `Baralho de Cartas` no terminal.
3. Execute o seguinte comando:

   ```sh
   python app.py
   ```

## Exemplo de Saída

```
Há 108 cartas no baralho.
Cartas: A♠, 2♠, 3♠, ...
Há 5 cartas na mão do Jogador 1
Cartas:
 -> 10♠
 -> Q♥
...
```

## Requisitos
- Python 3.x

## Melhorias Futuras
- Implementar regras de jogos específicos (como Poker ou Truco).
- Criar uma interface gráfica para facilitar a interação com o baralho.
- Adicionar testes automatizados para validar a distribuição de cartas.
