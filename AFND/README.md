# Autômato Finito Não Determinístico (AFND) :computer::robot:

## Concepção :black_nib::

Seguindo a linha de pensamento do AFD, foi feito um algoritmo que facilite ao estudante o entendimento do funcionamento do AFND. Essa facilidade é obtida pois trazemos para o algoritmo o que encontramos na teoria.Isso é transcrito da seguinte maneira:

Levando em consideração o AFND:

<img src="https://github.com/Paul0Cesar/LFA/blob/main/AFND/imgs/afnd.png" alt="AFND"/>

Podemos observar que partindo de e1,usando 0 temos duas possibilidades:

<img src="https://github.com/Paul0Cesar/LFA/blob/main/AFND/imgs/flow_afnd.png" alt="AFND FLOW"/>

Assim, nosso algoritmo, fazendo uso de uma customização da busca em profundidade, é capaz ao se deparar com o não determinismo,escolher um dos caminhos ao acaso, e resolver este até o fim(consumindo assim toda a palavra restante), caso, aquele caminho tomado leve a um estado final,como dito na literatura, já o suficiente para dizer que aquela palavra satisfaz o autômato.Caso esse caminho não leve a um estado final ou a um estado de erro,fazemos o retorno para o ponto do não determinismo e tomamos um caminho diferente ainda não avaliado e fazemos o mesmo processo dito anteriormente.

Em essência, nosso algoritmo ,tenta os diversos caminhos possíveis até encontrar um que satisfaça a condição de consumir a palavra toda e chegar a um estado final, ou não achando esse caminho, ao consumir a palavra toda,sabemos que ela não satisfaz nosso autômato.

## Estrutura de dados utilizadas :books::

Levando em consideração o objetivo de fazer um algoritmo o mais fiel possível aos desenhados em sala, foram utilizadas duas estruturas de dados comumente conhecidas, sendo elas o Grafo e a tabela Hash para representar nosso autômato. Já para gerenciar o não determinismo fizemos o uso da pilha, pois com está em combinação com a tabela hash poderíamos percorrer o grafo até o ponto mais profundo e ir voltando a medida que fosse necessário (pop na stack) para ir a fundo em outras possibilidades, guardando na tabela hash os caminhos já percorridos para não existir loops e/ou ambiguidades.


## Algoritmo :mag_right: :chart_with_upwards_trend::

a seguir discorreremos sobre um exemplo para ficar mais claro o funcionamento do algoritmo, salientamos ao leitor que faremos uso do AFND já citado no tópico anterior:

A análise será feita por meio de tabela de depuração, onde todas as principais variáveis estarão dispostas,lembrando, que iremos escolher sempre o pior caminho, mas o algoritmo não necessariamente faz isso.Assim considerando a palavra [10], temos :

Pior Cenário:
 
| iteração  |  stack  | actual_state   | depth  |  tmp_characters  | new | visited|
|--------|-----|-----|----|-----|-----|-----|
| 0  |  [e1] | - |  0 |  - | []| {} | 
| 1  | []  | e1 |  0 |  10 |[e1] |{} |
| 2  | [e1]  | e1  | 1  | 0  |[e1,e2] | {}|
| 3  | [e1,e1]  | e1  | 2  | - |[]| {}|
| 4  | [e1]  | e1  | 1  | 0  |[e2] | {e1}|
| 5  | [e1]  | e2  | 2  | -  |[] | {e1}|

Melhor Cenário:
 
| iteração  |  stack  | actual_state   | depth  |  tmp_characters  | new | visited|
|--------|-----|-----|----|-----|-----|-----|
| 0  |  [e1] | - |  0 |  - | []| {} | 
| 1  | []  | e1 |  0 |  10 |[e1] |{} |
| 2  | [e1]  | e1  | 1  | 0  |[e2,e1] | {}|
| 3  | [e1]  | e2  | 2  | - |[]| {}|


Assim, no passo 5 ou no passo 3, o estado final é encontrado,dessa forma podemos afirmar que essa palavra satisfaz nosso autômato.