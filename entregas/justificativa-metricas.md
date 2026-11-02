# Justificativa das métricas — Dashboard 2

## Contexto e denominadores

O aplicativo carrega `data/clean/cf_products_with_retailers.csv`. A base completa contém 922 marcas, sem valores ausentes. As cinco colunas de redes (`Ulta`, `Sephora`, `Beauty_Bay`, `Cult_Beauty` e `Nordstrom`) são indicadores de presença registrados como 0/1. `total_retailers` é a soma desses cinco indicadores.

Para os cálculos interativos, `R` representa o conjunto de redes selecionadas; `N` é o número de marcas na coorte atual, depois dos filtros que selecionam marcas; e `nᵢ(R)` é a quantidade de redes de `R` em que a marca `i` tem presença registrada. Para o KPI vegano, `N_veg` representa a coorte após os demais filtros de marca, mas antes do filtro `All_vegan`. Os resultados numéricos abaixo usam a base completa (`N = N_veg = 922`) e todas as cinco redes.

Presença no dataset significa apenas que o indicador daquela rede está marcado como presente. Não representa vendas, demanda, participação de mercado, quantidade de produtos ou disponibilidade atual. `All_vegan` e `Black_owned` são tratados como marcadores existentes no dataset, sem afirmação de verificação independente.

## Métrica 1 — Marcas presentes em pelo menos uma rede selecionada

- **Objetivo:** resumir quantas marcas da coorte têm presença registrada em ao menos uma das redes escolhidas.
- **Variáveis:** os indicadores 0/1 das redes selecionadas.
- **Fórmula:** contar marcas com `nᵢ(R) >= 1`; proporção = `contagem / N × 100`.
- **Resultado na base completa:** **225 marcas de 922 (24,40%)**.
- **Interpretação:** 225 marcas da base têm presença marcada em uma ou mais das cinco redes analisadas.
- **Relevância para o dashboard:** apresenta um resumo direto do alcance registrado no recorte selecionado.
- **Público interessado:** pessoas que analisam portfólio, varejo, distribuição registrada ou dados de marcas.
- **Decisão/análise apoiada:** escolher redes ou grupos que merecem investigação mais detalhada.
- **Limitações e cuidados:** o indicador não informa vendas nem disponibilidade real; cobre somente as redes presentes no dataset. O denominador deve ser exibido junto do percentual.

## Métrica 2 — Presença registrada por rede varejista

- **Objetivo:** comparar a quantidade e a proporção de marcas marcadas como presentes em cada rede selecionada.
- **Variáveis:** `Ulta`, `Sephora`, `Beauty_Bay`, `Cult_Beauty` e `Nordstrom`, conforme seleção.
- **Fórmula:** para cada rede `j`, contar `xᵢⱼ = 1`; percentual da rede = `contagem na rede / N × 100`.
- **Resultado na base completa:**

  | Rede | Marcas com presença registrada | % de 922 |
  |---|---:|---:|
  | Ulta | 141 | 15,29% |
  | Sephora | 92 | 9,98% |
  | Nordstrom | 51 | 5,53% |
  | Cult Beauty | 48 | 5,21% |
  | Beauty Bay | 40 | 4,34% |

- **Interpretação:** na base, Ulta tem a maior contagem de marcas marcadas como presentes e Beauty Bay, a menor.
- **Relevância para o dashboard:** mostra como a presença registrada se distribui entre as redes, complementando o KPI agregado.
- **Público interessado:** pessoas que comparam a cobertura registrada entre redes ou estudam o conjunto de marcas.
- **Decisão/análise apoiada:** selecionar diferenças ou redes para análises posteriores.
- **Limitações e cuidados:** não chamar os valores de participação de mercado, vendas ou desempenho. Cada percentual usa a coorte atual como denominador, e as redes podem compartilhar marcas.

## Métrica 3 — Marcas presentes em duas ou mais redes selecionadas

- **Objetivo:** destacar a amplitude da presença registrada dentro do conjunto de redes selecionadas.
- **Variáveis:** indicadores das redes selecionadas, somados por marca para obter `nᵢ(R)`.
- **Fórmula:** contar marcas com `nᵢ(R) >= 2`; proporção = `contagem / N × 100`.
- **Resultado na base completa:** **85 marcas de 922 (9,22%)**.
- **Interpretação:** 85 marcas têm presença marcada em pelo menos duas das cinco redes analisadas. A distribuição completa é: 0 redes = 697; 1 = 140; 2 = 44; 3 = 24; 4 = 13; 5 = 4.
- **Relevância para o dashboard:** diferencia presença em uma única rede de presença em várias, acrescentando contexto ao primeiro KPI.
- **Público interessado:** pessoas que analisam a amplitude da presença registrada das marcas no recorte.
- **Decisão/análise apoiada:** decidir quais grupos de marcas ou redes investigar mais profundamente.
- **Limitações e cuidados:** “duas ou mais” é um limiar analítico, não uma definição de sucesso. O resultado depende do número de redes selecionadas e não inclui outros canais.

## Métrica 4 — Marcas marcadas como 100% veganas

- **Objetivo:** apresentar a proporção da coorte cujo campo `All_vegan` está marcado como verdadeiro.
- **Variável:** `All_vegan`.
- **Fórmula:** na coorte após os demais filtros de marca e antes do filtro `All_vegan`, contar `All_vegan = True`; percentual = `contagem / N_veg × 100`.
- **Resultado na base completa:** **367 marcas de 922 (39,80%)**.
- **Interpretação:** essa fração da base está marcada como 100% vegana no campo disponível.
- **Relevância para o dashboard:** acrescenta um atributo das marcas à leitura de presença em redes.
- **Público interessado:** pessoas que exploram atributos declarados no dataset, pesquisa de marcas ou curadoria de portfólio.
- **Decisão/análise apoiada:** escolher grupos para comparar descritivamente, por exemplo, a presença registrada de marcas marcadas como veganas.
- **Limitações e cuidados:** o campo não comprova certificação nem verificação independente. A seleção de redes e o próprio filtro `All_vegan` não alteram este KPI. Os demais filtros de coorte, como `Bad_parent_company`, alteram `N_veg` e podem alterar o resultado.

## Métrica 5 — Comparação de presença entre marcas `Black_owned` e as demais

- **Objetivo:** comparar a proporção com presença registrada entre as marcas marcadas como `Black_owned = True` e as demais marcas.
- **Variáveis:** `Black_owned` e os indicadores das redes selecionadas.
- **Fórmula:** em cada grupo, contar marcas com `nᵢ(R) >= 1` e dividir pelo total de marcas daquele grupo na coorte. Exibir também numerador e denominador.
- **Resultado na base completa, com as cinco redes:** `Black_owned = True`: **3/51 (5,88%)**; demais marcas: **222/871 (25,49%)**. Diferença descritiva: **−19,61 pontos percentuais** no grupo marcado.
- **Interpretação:** nesta base e neste recorte, a fração com presença registrada é menor entre as marcas marcadas como `Black_owned`.
- **Relevância para o dashboard:** permite examinar uma diferença entre grupos registrada nos dados, sem ocultar o tamanho de cada grupo.
- **Público interessado:** pessoas que pesquisam representação e presença registrada de marcas em redes varejistas.
- **Decisão/análise apoiada:** apontar uma questão para investigação adicional sobre cobertura e composição do dataset.
- **Limitações e cuidados:** a comparação não identifica causa, não comprova discriminação e não caracteriza o mercado inteiro. O grupo marcado tem apenas 51 marcas; mostre os valores absolutos e os denominadores. `Black_owned` é um marcador do dataset, sem verificação independente afirmada.

## Regras dos filtros e dos percentuais

- A seleção de redes define quais indicadores de presença entram em `nᵢ(R)`.
- O denominador dos percentuais é `N`, a quantidade de marcas da coorte atual, e não somente as marcas que têm presença registrada. Mostrar contagens e denominadores junto aos percentuais.
- Com nenhuma rede selecionada, os KPIs de presença devem orientar a seleção; não devem exibir zero como se fosse um resultado observado. Apresentar o KPI como indisponível até que uma rede seja escolhida.
- Com apenas uma rede selecionada, o KPI “duas ou mais redes” é inaplicável, pois não há duas redes no recorte. Orientar a seleção de pelo menos duas redes.
- `Black_owned` deve ser dimensão para separar os dois grupos da comparação, e não filtro global que remova um deles. Aplicar filtros de coorte igualmente aos dois grupos.
- O KPI vegano é `marcas com All_vegan = True / N_veg`, calculado depois dos demais filtros de coorte e antes de aplicar o filtro `All_vegan`. Esse filtro continua atuando nos KPIs de presença e nos gráficos, mas não no próprio KPI vegano. A seleção de redes também não o altera. Se os demais filtros deixarem `N_veg = 0`, o KPI exibe indisponibilidade; se apenas o filtro `All_vegan` deixar vazia a coorte dos gráficos, o KPI vegano continua calculado sobre `N_veg`.
- A distribuição de quantidade de redes usa `nᵢ(R)`: com as cinco redes, as categorias são 0 a 5; com um subconjunto, o máximo é o número de redes selecionadas.
- `Black_owned` é dimensão da comparação e não é filtro global. `All_vegan` pode filtrar a coorte usada pelos KPIs de presença e pelos gráficos, mas é excluído da coorte e do denominador do próprio KPI vegano.

## Organização visual proposta

1. **Topo, três KPIs:** marcas presentes em pelo menos uma rede; marcas presentes em duas ou mais; marcas marcadas como 100% veganas. Mostrar contagem, percentual e denominador.
2. **Centro, barras horizontais em Altair:** presença por rede selecionada, com rótulos de contagem e percentual. A tabela de resultados desta justificativa está ordenada por contagem; o gráfico preserva a ordem do seletor: Ulta, Sephora, Beauty Bay, Cult Beauty e Nordstrom. O tooltip informa rede, quantidade de marcas e percentual, e a barra recebe realce visual no hover.
3. **Parte inferior, dois gráficos em Altair:** distribuição de marcas por quantidade de redes (0–5 quando todas as redes estiverem selecionadas), com tooltip de quantidade de redes, número de marcas e percentual da coorte; e comparação percentual de presença entre `Black_owned` e demais marcas. O tooltip da comparação informa grupo, numerador, denominador e percentual.

O seletor de redes define o recorte dos indicadores de varejo e dos dois gráficos de presença. Os percentuais de presença usam o tamanho da coorte filtrada atual; o KPI vegano usa `N_veg`, explicitado separadamente. `All_vegan` filtra os indicadores de presença e gráficos, mas não o KPI vegano; `Black_owned` separa os grupos, sem filtrar um deles. Essa ordem apresenta primeiro o panorama, depois a distribuição por rede e, por fim, a amplitude e a comparação entre grupos. Os três gráficos do Dashboard 2 usam Altair; os tooltips dão acesso aos detalhes numéricos e o hover destaca a barra do gráfico de presença por rede. Não há seleção cruzada entre gráficos ou KPIs.
