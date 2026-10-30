# Declaração de Uso de IA

**Nome:** Lucas Rodrigues Campos \
**Data:** 30/10/2026

## Ferramenta

### ChatGPT

Usei o ChatGPT para compreender as instruções da atividade, organizar as etapas e esclarecer dúvidas sobre Python, pandas, Streamlit e Git. Também discuti com a ferramenta a EDA de cosméticos, incluindo a distribuição das variáveis, valores extremos, correlações entre varejistas, gráficos e interpretação dos resultados. Usei o ChatGPT para gerar o rascunho visual do Dashboard 1; depois da implementação inicial do aplicativo, coloquei o arquivo em `entregas/` (`rascunho_dashboard1.png`, grafia atual do nome). Portanto, o rascunho não foi produzido antes de começar a implementação.

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
