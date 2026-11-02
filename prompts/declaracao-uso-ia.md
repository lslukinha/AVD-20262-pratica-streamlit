# Declaração de Uso de IA

**Nome:** Lucas Rodrigues Campos \
**Data:** 30/10/2026

## Ferramenta

### ChatGPT

Usei o ChatGPT para compreender as instruções da atividade, organizar as etapas e esclarecer dúvidas sobre Python, pandas, Streamlit e Git. Também discuti com a ferramenta a EDA de cosméticos, incluindo a distribuição das variáveis, valores extremos, correlações entre varejistas, gráficos e interpretação dos resultados. Usei o ChatGPT para gerar o rascunho visual do Dashboard 1; depois da implementação inicial do aplicativo, coloquei o arquivo em `entregas/` (`rascunho_dashboard1.png`, grafia atual do nome). Portanto, o rascunho não foi produzido antes de começar a implementação.

**Atualização do artefato:** a referência acima ao nome com underscore descreve a imagem histórica usada naquela etapa. O wireframe vigente, criado depois da implementação para corresponder ao app, é `entregas/rascunho-dashboard1.png`; as imagens anteriores foram preservadas.

Modelo/versão do ChatGPT: a confirmar. Não encontrei os registros dessas conversas nos arquivos locais consultados.

### Codex

Nas sessões locais de 29 e 30/10/2026, usei o Codex, modelo `gpt-6-luna`, pela versão 0.164.0-alpha.11.1 do CLI. Os registros locais contêm os pedidos feitos ao Codex; para manter esta declaração concisa, descrevo abaixo o conteúdo deles em resumo, não como transcrições literais.

## Prompt usado

### ChatGPT — resumos dos pedidos

- Compreender as instruções da atividade, organizar o trabalho e esclarecer conceitos de Python, pandas, Streamlit e Git.
- Discutir e revisar a EDA de cosméticos, incluindo distribuições, valores extremos, correlações entre redes varejistas, visualizações e interpretações.
- Gerar um rascunho visual para o Dashboard 1. O rascunho foi feito depois da implementação inicial do app e posteriormente colocado em `entregas/`.

### Codex — resumos dos pedidos registrados nas sessões

- **Preparar a EDA:** analisar o roteiro e preservar `notebooks/EDA_prática.ipynb` e o notebook didático da professora; criar `notebooks/eda.ipynb` como cópia de trabalho, acrescentando carregamento, inspeção, preparação e exportação dos dados de cosméticos. Pedi que a coluna `Unnamed: 0` só fosse removida se fosse um índice sequencial e que nenhuma marca fosse excluída por ser classificada como outlier.
- **Analisar e adaptar o app:** primeiro inspecionar `app.py`, `src/data_loader.py`, `src/__init__.py`, `requirements.txt` e `ROTEIRO.md`; depois adaptar o carregador para `data/clean/cf_products_with_retailers.csv` e o `app.py` para a Aula 21, com filtros booleanos, multiselect das cinco redes, slider de `total_retailers`, contagem de marcas e placeholders para correlação e distribuição.
- **Executar e testar:** executar o notebook, conferir os dados exportados e preservados, testar os filtros e widgets com o `AppTest`, verificar o carregador a partir de outra pasta e iniciar `streamlit run app.py`.
- **Revisar e corrigir a EDA:** analisar código, saídas, gráficos e interpretações de `notebooks/eda.ipynb`; depois substituir o diagnóstico de outliers por frequências, adicionar o gráfico de distribuição, comparar proporções de `Bad_parent_company` por `All_vegan`, usar rótulos neutros, validar os indicadores binários e remover o título bivariado sem conteúdo.
- **Auditar para o GitHub:** conferir arquivos, `.gitignore` e estado do Git. A pasta `.git` estava vazia e o projeto não era reconhecido como repositório; não inicializei Git, não configurei remoto e não fiz commit ou push.

## O que foi aceito, modificado ou rejeitado e por quê

- **Aceito:** usei as sugestões do Codex para preparar e executar a cópia de trabalho da EDA, exportar o dataset tratado e construir o esqueleto funcional do Dashboard 1. No notebook, aceitei a descrição das frequências de zero a cinco redes, o gráfico de distribuição, a comparação proporcional entre `All_vegan` e `Bad_parent_company`, os rótulos neutros e a validação de que os indicadores das cinco redes contêm apenas 0 ou 1. Mantive `log1p` como comparação exploratória; não removi marcas.
- **Modificado:** `notebooks/eda.ipynb` foi criado a partir de `notebooks/EDA_prática.ipynb`, preservando as células originais e acrescentando o preparo dos dados. Depois, a EDA foi revisada e alterada com minha solicitação: a regra de IQR deixou de classificar observações, o título vazio da seção bivariada foi retirado e os gráficos e rótulos foram ajustados. O `app.py` e `src/data_loader.py` foram adaptados para os dados de cosméticos; o Dashboard 1 ficou com filtros, contagem e placeholders, sem heatmap ou histograma. O Codex também criou `data/raw/cf_products_with_retailers_original.csv` como cópia local dos dados de entrada. O CSV bruto de entrada não foi alterado.
- **Rejeitado:** não encontrei sugestões explicitamente recusadas nos registros locais do Codex. Não registrei rejeições que não consigo confirmar.

O notebook foi executado sem erros e sua exportação foi validada com 922 linhas e 12 colunas. Os testes do `AppTest` verificaram os quatro filtros booleanos, o slider, o multiselect e os casos com zero ou uma rede selecionada; também confirmei o carregamento do CSV a partir de outra pasta. O app iniciou em `http://localhost:8501`. Para instalar dependências e executar o notebook e o Streamlit, houve solicitações de autorização para sair do sandbox. As dependências foram instaladas no ambiente local `.venv`.

**Ponto a conferir com as orientações da disciplina:** a sequência do rascunho — gerado depois da implementação inicial — pode não corresponder à orientação de desenhá-lo antes de codar. Também houve participação de IA na discussão analítica e visual da EDA; esta declaração registra esse uso sem afirmar que ele é permitido pelas regras da professora.

## Registro de uso de IA — planejamento do Dashboard 2 (01/11/2026)

Usei o Codex como apoio para organizar a análise exploratória já realizada do dataset de cosméticos e preparar a documentação e o esboço visual do Dashboard 2. A ferramenta ajudou a explicitar as fórmulas, resultados, público, usos possíveis e limitações das cinco métricas; discutir o efeito da seleção de redes e os denominadores; preservar `Black_owned` como dimensão de comparação; e definir que o KPI `All_vegan` representa a coorte atual e não muda apenas pela seleção de redes.

Também usei o Codex para estruturar o wireframe `entregas/rascunho-dashboard2.png`, com três KPIs, barras de presença por rede, distribuição por quantidade de redes e comparação descritiva entre grupos `Black_owned`. O desenho usa os valores apurados para a base completa e registra que presença na base não representa vendas, demanda ou disponibilidade atual. O texto desta declaração resume o pedido desta etapa; não é uma transcrição literal de prompt.

O planejamento adotou essas métricas e regras para produzir a justificativa e o wireframe. Não foi implementada a segunda aba nem alterado o código do aplicativo nesta etapa. Não foram registradas sugestões rejeitadas nesta etapa.

## Registro de uso de IA — implementação e migração do Dashboard 2

Depois do planejamento, usei o Codex para orientar a implementação do Dashboard 2 e migrar seus três gráficos de Matplotlib para Altair: presença registrada por rede, distribuição por quantidade de redes e comparação entre marcas marcadas como `Black_owned` e as demais. Mantive os cálculos, KPIs, filtros e regras existentes.

Com apoio do Codex, acrescentei tooltips aos três gráficos e realce visual no hover do gráfico de presença por rede. Também configurei explicitamente fundo, superfície, texto, eixos, títulos, legendas e grades para manter o tema escuro e as cores da aplicação. Incluí Altair diretamente em `requirements.txt`, com uma faixa compatível com a versão mínima de Streamlit declarada no projeto.

Usei o `AppTest` para comparar os dados serializados nos gráficos novos com os agregados anteriores e conferir valores da base completa, combinações de filtros, nenhuma ou uma rede selecionada, categorias com frequência zero, coorte vazia, grupos vazios e alternância entre dashboards com filtros independentes e persistentes. Verifiquei também a especificação dos gráficos, incluindo a configuração de tooltip e hover. Não automatizei o movimento do cursor no navegador; portanto, o hover foi verificado na especificação Altair, não por um teste de interação visual com o cursor.

O registro acima resume o uso de IA nesta etapa, sem transcrever prompts literalmente. Não implementei filtros cruzados nesta migração.

## Registro de uso de IA — revisão de consistência da Entrega 2

Usei o Codex para revisar a implementação e os documentos existentes e corrigir a regra do KPI vegano conforme a decisão tomada: calculei esse KPI após os demais filtros de coorte e antes do filtro `All_vegan`, mantendo esse filtro ativo para os indicadores de presença e os gráficos. Também atualizei a justificativa para explicitar o denominador independente e os estados de coorte vazia.

Usei o Codex para identificar e corrigir referências desatualizadas ao caminho `data/clean/dataset.csv`, esclarecer a navegação por seletor horizontal `st.radio` e diferenciar tooltips/hover de seleção cruzada, que não foi implementada. Revisei ainda a orientação sobre licença para não sugerir que um repositório privado autoriza redistribuição. Preservei os registros anteriores e não alterei notebooks, imagens ou dados nesta revisão. Este parágrafo resume o uso da ferramenta, sem transcrever o pedido literalmente.

## Registro de uso de IA — investigação dos entregáveis e reprodutibilidade

Usei o Codex para comparar visualmente os wireframes com a implementação, ler e comparar o conteúdo dos quatro notebooks, revisar os caminhos do dataset, dependências e instruções de execução, e testar uma cópia temporária do app sem o CSV local. Também usei a busca para consultar a página do Kaggle e a documentação de licenças da plataforma; a licença específica deste dataset não pôde ser confirmada pelos dados acessíveis na página. Não alterei nem executei notebooks, não alterei dados e não substituí ou renomeei imagens.

Com apoio do Codex, atualizei apenas instruções comprovadamente confusas sobre a instalação opcional das Streamlit skills, o papel do exemplo Heart Disease, a preparação do CSV de cosméticos e a diferença entre uso local, acesso privado e redistribuição pública. A origem dos notebooks de referência e a decisão final sobre o wireframe do Dashboard 1 continuam sem confirmação. Este registro resume o uso da ferramenta, sem transcrever o pedido literalmente.

## Registro de uso de IA — conclusão da documentação e dos wireframes da Entrega 2

Depois, esclareci que `notebooks/EDA_prática.ipynb` é minha EDA original de cosméticos da Aula 11 e que `notebooks/eda.ipynb` é o fluxo de trabalho usado para preparar os dados consumidos pelo app. Também identifiquei `arquivo-eda-original.ipynb` e `eda-com-downloads.ipynb` como materiais didáticos de referência sobre Heart Disease/UCI, sem tratá-los como minha EDA. Usei o Codex para alinhar o README, o roteiro e o checklist a essa distinção; os quatro notebooks foram preservados e não executei suas células.

Usei o Codex para comparar `app.py` com os wireframes e gerar uma nova imagem atual do Dashboard 1, preservando as imagens antigas como referências históricas, e atualizar o wireframe do Dashboard 2 com a regra vigente do KPI vegano, os filtros, valores e gráficos existentes. Os desenhos foram produzidos como representações planejadas da interface a partir do código e dos dados locais, não como capturas reais do navegador. A revisão do wireframe do Dashboard 2 também registra tooltips e hover sem afirmar seleção cruzada entre gráficos.

Também pedi a inspeção das dependências e das instruções de instalação. Como a busca no aplicativo, no código-fonte e nos notebooks não encontrou uso de Plotly e o roteiro não o exige, removi sua declaração direta de `requirements.txt`; mantive as demais dependências. Ao testar a versão mínima declarada do Streamlit, encontrei opções de tema não reconhecidas no arquivo de configuração. Com apoio do Codex, converti a configuração para a sintaxe compatível com Streamlit 1.50 e preservei base escura, fundo, superfície, texto e vermelho de destaque, sem elevar a versão mínima. Registrei que o CSV necessário não está incluído nesta etapa, que a execução local com o arquivo disponível pode ser testada e que a reprodução de um clone sem os dados depende de uma forma aprovada de disponibilização. Este registro resume o uso de IA, sem inventar datas ou transcrever prompts literalmente.

## Registro de uso de IA — ajustes finais da Entrega 2

Usei o Codex para conferir o PDF original da Aula 22 e comparar seus requisitos de entrega com o projeto. A partir do wireframe PNG existente, gerei `entregas/rascunho-dashboard2.jpg` por conversão, sem redesenhar seu conteúdo, e preservei o PNG. Revisei `entregas/README.md` e `ROTEIRO.md` para registrar o JPG pedido na página 17, distinguir o pedido literal de tabs da escolha técnica atual por `st.radio` e deixar explícito que há tooltips e realce por hover, sem seleção cruzada.

Também usei o Codex para inspecionar `notebooks/eda.ipynb` e `notebooks/EDA_prática.ipynb`. Como não encontrei uma comparação exploratória de presença por `Black_owned`, acrescentei em `eda.ipynb` uma tabela com numeradores, denominadores e percentuais dos dois grupos e um gráfico de barras. Conferi os resultados com o CSV local e validei a execução dessa célula isoladamente, sem executar o notebook inteiro, cujas células exportam arquivos de dados. Não alterei `EDA_prática.ipynb`, os CSVs nem o código do aplicativo. Este registro resume o uso da ferramenta e não reproduz um prompt literal.

## Registro de uso de IA — complementação exploratória das métricas do Dashboard 2

Usei o Codex para comparar as cinco métricas documentadas com os cálculos e gráficos já presentes em `notebooks/eda.ipynb`, `app.py` e `entregas/justificativa-metricas.md`. Acrescentei ao notebook uma tabela e um gráfico de presença registrada por rede, uma conferência explícita da métrica de duas ou mais redes e uma análise do KPI `All_vegan` com seus numeradores, denominadores, percentuais e visualização por coortes de `Bad_parent_company`. Também registrei uma tabela de cenários que demonstra que o filtro `All_vegan` altera as marcas exibidas nos gráficos, mas não o KPI calculado antes desse filtro, enquanto o filtro `Bad_parent_company` pode alterar o numerador e o denominador.

Conferi os resultados com o CSV local e com a regra implementada no app. Não executei o notebook inteiro nem alterei código do aplicativo, dados, dependências ou a EDA original. O ambiente Python disponível naquela sessão não tinha pandas e matplotlib, então naquele momento não executei as novas células nem gerei suas saídas; validei o JSON, a sintaxe das células e os cálculos equivalentes diretamente pelas linhas do CSV usando a biblioteca padrão. Este registro resume o uso de IA e não transcreve um prompt literal.

Em uma etapa posterior, usei o Codex para executar as três células de código novas de `notebooks/eda.ipynb` no ambiente virtual existente `.venv`, com as dependências que já estavam instaladas, sem instalar ou atualizar pacotes. As células produziram tabelas e dois gráficos. Conferi os resultados com o CSV, os cálculos do aplicativo e `entregas/justificativa-metricas.md`; depois, as saídas da execução foram salvas nas células correspondentes do notebook. Executei somente essas células, com a preparação dos dados em memória, sem rodar o notebook inteiro.
