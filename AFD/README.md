# Autômato Finito Determinístico (AFD) :computer::robot:

## Concepção:black_nib::

O Algoritmo foi pensado para representar o mais fielmente possivel o funcionamento dos AFD's feitos em sala(exercios), de forma que qualquer outro estudante consiga observar e captar o que está acontecendo.Diante disso
o programa foi organizado juntamente com os testes para tentar ser mais uma ferramente no entendimento do funcionando dos Autômato Finitos Determinísticos(AFD). 

## Estrutura de dados usadas :books::

Levando em consideração o objetivo de fazer um algoritmo o mais fiel possivel aos desenhados em sala, foram utlizadas duas estruturas de dados comumente conhecidas, sendo elas o Grafo e o HashMap. 

Sendo mais específico para o Grafo, usamos a representação dele como uma lista de Adjacências, onde para sua implementação foi utilizado o Dicionário do Python onde podemos comparar seu funciomamento ao HashMap, assim a representação do dado é feita usando *<Chave,Valor>*, dessa forma representando os possíveis estados do AFD.Abaixo podemos observar uma exemplo: 

```python3
{
    "0":{},
    "1":{}
}
```

Onde 0,1 são os possíveis estados desse AFD.

Para as transições entre estados tambem foi utlizado o Dicionário, já considerando as peculiaridades que iriamos ter ao tentar *"buscar"* um caminho para o proximo estado, a seguinte estrutura foi adotada: 

```python3
{
    "0":{"a":"1"},
    "1":{"a":1,"b":1}
}
```

Olhando mais de perto para o estado *"0"*:

```python3
 {"a":"1"}

```

A forma como a lista de transições foi criada, foi considerando a forma como a movimentação entre os estados acontece, de forma que a "busca" ou troca de estado fosse o mais eficiente possivel.Sabendo que a troca de estado é sempre considerando um "caracter" da palavra atual, usamos então os possiveis caracteres como chave para o novo estado, aproveitando assim o funcionamento e as vantagens do HashMap.

## Complexidade :mag_right: :chart_with_upwards_trend::

Se olharmos mais atentamente para a complexidade dos algoritmos aqui usados, temos que citar a função responsável pela analise das palavras providas na estrada do programa:

```python3
def verify_word(afd, word, start_state, end_state_list):
    ...
    for char in characters:
        vertice = afd.get_destiny_vertice_with(current_state, char)
        if (vertice is not None):
            current_state = vertice
        else:
            current_state = None
            break
    ...
```

Onde o *afd* é o Grafo já contendo os possiveis estados e suas transições, *word* é a palavra que deve ser analisada, *start_state* é o estado onde o processo começa e *end_state_list* contem a lista de estados finais.

Se o observamos de perto o custo dessa função sem analisar *get_destiny_vertice_with* é o O(n) pois desconsiderando os custos constantes o pior cenario possivel é analisar todas as letras da palavra, sendo **n** o numero de caracteres dessa palavra.

Olhando agora a função *get_destiny_vertice_with*, temos :

```python3
def get_destiny_vertice_with(self, u, way):
        try:
            return self.vertices[str(u)][str(way)]
        except KeyError:
            return None
```

Assim, como utlizamos o HashMap como base para montar nossa lista de Adjacências e sabemos que o custo de uma busca em um HashMap é constante podemos então desconsiderar seu custo. 


Assim, o custo para o processamento da palavra é dado pelo numero de caracteres que ela contem, ou seja : **O(n)**