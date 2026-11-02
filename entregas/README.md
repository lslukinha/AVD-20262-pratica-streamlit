# Entregáveis da Entrega 2

Esta pasta reúne os artefatos de análise e visualização. O wireframe do Dashboard 2 é entregue em JPG, como especifica o PDF da Aula 22; a versão PNG de mesmo conteúdo também foi preservada. Imagens antigas de Dashboard 1 ficam preservadas como referência histórica.

## Arquivos atuais

| Arquivo | Conteúdo | Situação |
|---|---|---|
| `rascunho-dashboard1.png` | Wireframe do Dashboard 1 conforme `app.py`: filtros na sidebar, correlação de Spearman, histogramas quantitativos e barras de frequência de `total_retailers`. | Atual |
| `rascunho-dashboard2.jpg` | Wireframe do Dashboard 2 conforme `app.py`: navegação horizontal por `st.radio`, filtros, três KPIs e três gráficos Altair. Formato/caminho solicitado na página 17 do PDF da Aula 22. | Entrega solicitada |
| `rascunho-dashboard2.png` | Versão PNG preservada, com o mesmo conteúdo visual do wireframe JPG. | Cópia preservada |
| `justificativa-metricas.md` | Fórmulas, resultados, denominadores, interpretação, público e limitações das cinco métricas do Dashboard 2. | Atual |

O wireframe atual do Dashboard 1 foi produzido depois da implementação para representar fielmente a interface vigente. Ele é o esboço atualizado da entrega, mas não comprova a sequência original de desenhar antes de codificar; a declaração de uso de IA registra essa cronologia. O wireframe do Dashboard 2 foi atualizado para acompanhar o app e convertido para o JPG solicitado, sem redesenho; o PNG original permanece preservado.

## Imagens históricas de Dashboard 1

- `rascunho_dashboard1.png` (underscore): esboço anterior à implementação completa; contém componentes que já não correspondem ao app. Preservado para histórico, não é o wireframe atual.
- `prof_rascunho_dashboard1.png`: referência visual genérica. Sua autoria não é atribuída aqui, pois não há evidência suficiente. Não representa a implementação atual.

## Checklist da Entrega 2

- [x] Wireframe atual do Dashboard 1 (`rascunho-dashboard1.png`).
- [x] Wireframe atual do Dashboard 2 no formato/caminho solicitado (`rascunho-dashboard2.jpg`); versão PNG preservada.
- [x] Justificativa das cinco métricas com fórmulas, resultados, denominadores, públicos, decisões apoiadas e ressalvas.
- [x] Wireframes coerentes com a implementação, incluindo os estados e limites descritos nos próprios desenhos.

## EDA e dados associados

A EDA original de cosméticos da Aula 11 está em `../notebooks/EDA_prática.ipynb`. `../notebooks/eda.ipynb` é o fluxo de trabalho que prepara os dados usados pelo aplicativo e também reúne análises exploratórias das métricas do Dashboard 2: presença por varejista, marcas presentes em uma ou mais redes, marcas presentes em duas ou mais redes, o KPI `All_vegan` e sua variação entre coortes de `Bad_parent_company`, além da comparação descritiva por `Black_owned`. As novas células incluem tabelas e gráficos preliminares; as análises anteriores foram preservadas. A justificativa das métricas contém as fórmulas e interpretações detalhadas. `../notebooks/arquivo-eda-original.ipynb` e `../notebooks/eda-com-downloads.ipynb` são materiais didáticos Heart Disease/UCI, não a EDA de cosméticos; eles e `EDA_prática.ipynb` foram preservados.

O app requer `data/clean/cf_products_with_retailers.csv`, que não acompanha esta entrega no Git enquanto a licença e a autorização de redistribuição não estiverem confirmadas. Consulte o [README principal](../README.md) para obter e preparar uma cópia local. Um clone sem esse arquivo não executa o app até que os dados sejam disponibilizados por um meio aprovado.
