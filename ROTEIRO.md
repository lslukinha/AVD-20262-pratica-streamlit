# Roteiro das aulas

Guia passo a passo de cada aula. Antes de começar a Aula 21, siga o **Setup** no [README.md](README.md).

## Aula 21 — Streamlit, parte 1

1. Crie o seu repositório a partir deste: dê **fork** (ele já nasce na sua conta pessoal do GitHub) ou clone e publique num repositório novo seu. A entrega final precisa estar num repositório da sua conta. Tornar o repositório público é permitido nesta atividade.
2. Siga o **Setup** do README: crie o venv e instale o `requirements.txt`. `streamlit skills --yes` é opcional e só serve para preparar instruções de IA; não é necessário para executar o app.
3. Preserve e identifique os notebooks existentes conforme sua função neste projeto:
   1. `EDA_prática.ipynb` é a EDA original de cosméticos produzida pelo estudante para a Aula 11.
   2. `eda.ipynb` é a cópia de trabalho/fluxo de preparação dos dados de cosméticos utilizada para gerar `data/clean/cf_products_with_retailers.csv`, arquivo esperado pelo carregador do app.
   3. `arquivo-eda-original.ipynb` e `eda-com-downloads.ipynb` são materiais didáticos de referência sobre Heart Disease/UCI. Não são a EDA de cosméticos nem preparam o CSV usado pelo aplicativo.
   4. Para reconstruir o CSV local em outro ambiente, obtenha uma cópia compatível do dataset na fonte indicada no README, coloque-a em `data/raw/` e execute as células do fluxo `eda.ipynb` na ordem. Respeite os termos da fonte; a licença específica e a redistribuição ainda precisam ser confirmadas. `data/clean/dataset.csv` é de outro conjunto de dados e não deve ser usado pelo app.
4. Desenhe o rascunho do layout do Dashboard 1 (sidebar + filtros + correlação + distribuição) e salve em `entregas/rascunho-dashboard1.jpg` (ou `.png`). O wireframe atual está em `entregas/rascunho-dashboard1.png`; os arquivos com underscore são referências históricas e não substituem o wireframe atual.
5. Use o template em `prompts/layout-skeleton-prompt.md` para gerar o esqueleto do `app.py` a partir do rascunho.
6. Implemente pelo menos **1 seletor de variáveis** e **1 slider de intervalo** no esqueleto.
7. Rode `streamlit run app.py` e confirme que os widgets aparecem e respondem.
8. Preencha `prompts/declaracao-uso-ia.md` com o uso de IA de hoje e dê commit + push.

Veja o checklist de arquivos esperados em [entregas/README.md](entregas/README.md); o uso de IA fica em [prompts/README.md](prompts/README.md).

## Aula 22 — Streamlit, parte 2

**Antes de começar**, confira que você tem da Aula 21:
- `app.py` rodando localmente sem erro
- Repositório com remoto no GitHub e pelo menos um commit
- 1 seletor de variáveis e 1 slider de intervalo já funcionando

**Passos:**

1. Adicione os gráficos ao Dashboard 1 e mantenha o carregamento de dados com `@st.cache_data`. Nesta implementação, o Dashboard 1 usa Seaborn/Matplotlib em `st.pyplot` para o heatmap de Spearman, os histogramas e as frequências de `total_retailers`. O Dashboard 2 usa Altair. Bibliotecas alternativas, como Plotly, só são necessárias se forem escolhidas para uma implementação; não são dependência deste projeto.
2. Teste o Dashboard 1 em cenários de borda: comportamento com 0 variáveis selecionadas, 1 variável, 2 ou mais, e o recálculo da correlação/distribuição com combinações distintas de widgets. Ajuste o que quebrar.
3. Escolha a identidade visual do app (cor de fundo, cor de destaque, fonte) em `.streamlit/config.toml`.
4. Estruture o Dashboard 2, nesta ordem:
   1. Selecione as variáveis que vão entrar nos KPIs.
   2. Proponha as métricas (ligue com a Teoria de Métricas Básicas da aula).
   3. **Defina os widgets que vão controlar o dashboard** antes de codar (ex.: um seletor de período, um filtro de categoria) — mesmo princípio do Dashboard 1: sem isso definido, não dá pra desenhar o rascunho direito.
   4. Só então desenhe o rascunho da página. A página 17 do PDF original especifica `entregas/rascunho-dashboard2.jpg`; este projeto entrega esse JPG e também preserva `entregas/rascunho-dashboard2.png` com o mesmo conteúdo visual.
5. Separe Dashboard 1 e Dashboard 2 no mesmo app. O PDF da Aula 22 (p. 16) pede a criação de tabs. Esta implementação usa o seletor horizontal `st.radio`, não `st.tabs`, para que a sidebar exiba somente os filtros do dashboard ativo na versão mínima Streamlit 1.50. É uma decisão técnica que diverge do componente solicitado literalmente no PDF; não descreva o `radio` como se fosse `st.tabs`.
6. Implemente o Dashboard 2 a partir do rascunho: widgets → métricas (`st.metric`) → visuais com Altair. Os gráficos têm tooltips; o gráfico de presença por rede também realça a barra no hover. Não há seleção cruzada entre gráficos ou KPIs nesta implementação. O guia [ALTAIR-CROSSFILTER.md](ALTAIR-CROSSFILTER.md) apresenta essa funcionalidade adicional, que só deve ser descrita como implementada se as seleções realmente atualizarem outros gráficos ou métricas.
7. Documente em `entregas/justificativa-metricas.md` por que cada métrica foi escolhida e o que ela comunica ao público.
8. Atualize `prompts/declaracao-uso-ia.md` com as conversas de IA desta aula.
9. Commit + push.

> As entregas desta aula (rascunho do Dashboard 2 e justificativa das métricas) devem ficar completas. Se a implementação do Dashboard 2 não fechar, o que faltar termina na Aula 23.

**Objetivo para a Aula 23:** finalizar o que ficar pendente da implementação do Dashboard 2 e fazer o deploy.

Veja o checklist de arquivos esperados em [entregas/README.md](entregas/README.md); o uso de IA fica em [prompts/README.md](prompts/README.md).

## Aula 23 — Streamlit, parte 3 (continuação + Deploy)

1. Retome e finalize a implementação do Dashboard 2 (pendências da Aula 22).
2. Confira o repositório **antes** do deploy (checklist abaixo).
3. Faça o deploy no Streamlit Community Cloud (passo a passo abaixo).
4. Teste o app publicado (checklist de teste abaixo).
5. Adicione o link do app (`.streamlit.app`) no [README.md](README.md) como parte da entrega.

### Checklist antes do deploy

- [ ] O repositório está no GitHub, na sua conta, com tudo commitado e enviado (`git status` limpo, `git push` feito).
- [ ] `app.py` está na raiz e roda localmente com `streamlit run app.py` sem erro.
- [ ] O arquivo `data/clean/cf_products_with_retailers.csv` necessário ao app está disponível no ambiente de execução por um meio cuja redistribuição foi autorizada. Não use o `data/clean/dataset.csv` de Heart Disease nem publique dados com licença pendente.
- [ ] O app lê o dado pelo caminho relativo `data/clean/cf_products_with_retailers.csv`, conforme `src/data_loader.py`.
- [ ] `requirements.txt` lista as bibliotecas importadas por `app.py` e `src/`, incluindo Altair, que está declarado diretamente neste projeto.
- [ ] Nada sensível no repositório: dados pessoais, chaves, tokens. `.streamlit/secrets.toml` não deve ser versionado (já está no `.gitignore`).
- [ ] `.streamlit/config.toml` (tema) está versionado, se você customizou a identidade visual.

### Deploy no Streamlit Community Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io) e entre com a **mesma conta do GitHub** que tem o repositório.
2. Autorize o acesso ao GitHub quando pedido. Para repositório privado, autorize também o acesso a repositórios privados (e dê acesso de leitura ao professor, como no README).
3. Clique em **Create app** e escolha **Deploy a public app from GitHub** (ou equivalente; os rótulos mudam de tempos em tempos).
4. Preencha:
   - **Repository:** `seu-usuario/nome-do-repositorio`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL (opcional):** escolha um subdomínio, que vira `https://<subdominio>.streamlit.app`.
5. Em **Advanced settings**, escolha a versão do Python (use uma entre 3.11 e 3.15, a mesma do seu venv, se possível). Não há segredos para preencher neste projeto.
6. Clique em **Deploy**. A primeira publicação instala as dependências e leva alguns minutos; acompanhe pelo log na tela.
7. Copie a URL do app e cole no README, na linha **Link do app**.

**Depois do deploy:** cada `git push` na branch publicada atualiza o app automaticamente. Em **Manage app** (canto inferior direito do app publicado) você vê os logs e pode reiniciar (*Reboot*) ou apagar o app. Apps sem acesso por algum tempo entram em modo de espera e acordam com um clique ao serem abertos; isso é normal.

### Erros comuns no deploy

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| `ModuleNotFoundError` no log | Biblioteca usada no código mas ausente do `requirements.txt` | Adicione ao `requirements.txt`, commit e push |
| `FileNotFoundError` do CSV | `data/clean/cf_products_with_retailers.csv` não está disponível, ou o caminho está incorreto | Obtenha e prepare o dataset conforme o README; disponibilize-o apenas por meio autorizado e use o caminho relativo da raiz |
| App funciona local e quebra no deploy | Versão de Python ou de biblioteca diferente | Escolha o Python em *Advanced settings* e confira as versões no `requirements.txt` |
| Repositório não aparece na lista | Faltou autorizar o GitHub ou o repositório é privado sem permissão | Revise a autorização do Streamlit no GitHub (*Settings → Applications*) |
| Alteração no GitHub não aparece no app | Push não foi feito, ou foi em outra branch | Confira o `git push` e a branch configurada no app |

### Checklist de teste do app publicado

- [ ] Abre em janela anônima, sem login (o link é público).
- [ ] Todos os widgets respondem e os dois dashboards, selecionados pelo `st.radio` horizontal, carregam.
- [ ] Nenhum dado sensível aparece na tela nem no repositório.
- [ ] O link do README abre o app.

**Entregáveis finais:**
- [ ] Link do app publicado no README
- [ ] Repositório próprio e completo: notebooks, `app.py`, `entregas/`, `prompts/`
