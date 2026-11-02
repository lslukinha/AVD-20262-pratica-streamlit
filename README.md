# AVD-20262-pratica-streamlit

Repositório utilizado para aula prática relacionada a Streamlit na disciplina Análise e Visualização de Dados da Cesar School no período de 2026.2.

Repositório-modelo das Aulas 21, 22 e 23: construção de dois dashboards em Streamlit a partir da EDA desenvolvida em sala. O deploy dos dashboards ocorrerá via Streamlit Community Cloud e serão os seguintes:

- Dashboard 1 = heatmap de correlação, histogramas das variáveis quantitativas e frequência de marcas por `total_retailers`
- Dashboard 2 = KPIs, presença por rede, distribuição por quantidade de redes e comparação descritiva por `Black_owned`

## Setup

Requer **Python 3.11 a 3.15**. Confira a sua versão antes de começar:

| Sistema | Verificar versão |
| --- | --- |
| macOS / Linux | `python3 --version` |
| Windows | `py --version` |

### 1. Criar e ativar o ambiente virtual

O nome do comando do Python muda por sistema (em muitas máquinas `python` nem existe). Use a linha do seu sistema:

| Sistema | Criar | Ativar |
| --- | --- | --- |
| macOS / Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |
| Windows (PowerShell) | `py -m venv .venv` | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `py -m venv .venv` | `.venv\Scripts\activate.bat` |

Se você tem várias versões instaladas, escolha uma compatível, por exemplo `python3.12 -m venv .venv` (macOS/Linux) ou `py -3.12 -m venv .venv` (Windows).

Com o ambiente ativo, o terminal mostra `(.venv)` no início da linha. **A partir daqui os comandos são iguais em todos os sistemas**, porque dentro do venv `python` e `pip` sempre existem.

### 2. Instalar e executar

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Antes de executar o aplicativo, obtenha e prepare o dataset conforme a seção [Dados usados pelo aplicativo](#dados-usados-pelo-aplicativo).
O comando `streamlit skills --yes`, descrito em “IA neste projeto”, é opcional e não é necessário para executar o aplicativo.

### Problemas comuns

- **`python: command not found` / `python` não é reconhecido:** use `python3` (macOS/Linux) ou `py` (Windows) só para criar o venv; depois de ativado, `python` funciona.
- **Linux (Debian/Ubuntu): `ensurepip is not available` ou `No module named venv`:** instale `sudo apt install python3-venv` (ou `python3.X-venv` para a sua versão).
- **Windows: "a execução de scripts foi desabilitada" ao ativar no PowerShell:** rode uma vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, ou use o cmd.
- **Python fora de 3.11–3.15:** instale uma versão compatível em [python.org](https://www.python.org/downloads/) e crie o venv com ela, como no exemplo acima.
- **Apareceu `ModuleNotFoundError` ou `streamlit: command not found`:** o venv provavelmente não está ativo. Ative de novo e confira o `(.venv)` no prompt.
- **Erro de certificado no `pip install` (macOS, Python do python.org):** rode `Install Certificates.command`, na pasta Python 3.X em Aplicativos.
- **`DatasetNotFoundError` ao baixar o exemplo Heart Disease/UCI no notebook `eda-com-downloads.ipynb` (macOS, Python do python.org):** é o mesmo problema de certificado SSL. Rode `Install Certificates.command` e reinicie o kernel. Esse notebook é um exemplo didático separado e não prepara o dataset de cosméticos usado pelo app.

## Estrutura de dados: `data/raw` vs `data/clean`

- `data/raw/`: o dataset **bruto**, como foi baixado. Nunca é editado à mão.
- `data/clean/`: datasets **já tratados**, exportados na última célula dos notebooks de EDA. O aplicativo atual lê `cf_products_with_retailers.csv` desta pasta, por meio de `src/data_loader.py`.

### O que vai para o Git

| Pasta | Versionada? | Por quê |
| --- | --- | --- |
| `data/raw/` | **Não** (só o `.gitkeep`) | O bruto pode ser grande ou ter dados sensíveis, e o app não o usa. |
| `data/clean/` | **Seletivamente** | A pasta inteira não é ignorada. O CSV tratado usado pelo app está versionado para o deploy; outros datasets tratados, como `dataset.csv`, devem ser revisados individualmente antes de versionar. |

## Dados usados pelo aplicativo

O aplicativo utiliza o dataset **Cruelty Free Brands**, publicado por **mhapich** no [Kaggle](https://www.kaggle.com/datasets/mhapich/crueltyfree-brands). Para permitir a execução no Streamlit Community Cloud, `data/clean/cf_products_with_retailers.csv` está incluído no repositório. A licença específica e a autorização de redistribuição ainda não foram confirmadas; a inclusão técnica não confirma esses direitos. Confira os termos da fonte antes de compartilhar ou publicar os dados.

O arquivo local `data/clean/dataset.csv`, quando presente, corresponde ao exemplo Heart Disease/UCI e não é usado pelo app. Não o use como substituto do dataset de cosméticos nem o publique como dado desta aplicação.

Para preparar uma cópia local a partir da fonte, disponibilize um CSV bruto compatível em `data/raw/cf_products_with_retailers.csv` e execute o notebook conforme os passos abaixo. O CSV tratado usado pelo aplicativo fica em `data/clean/cf_products_with_retailers.csv`:

```text
data/clean/cf_products_with_retailers.csv
```

Para preparar uma cópia local:

1. Obtenha o CSV na fonte indicada, observando os termos aplicáveis, e coloque-o em `data/raw/cf_products_with_retailers.csv`.
2. Execute as células de `notebooks/eda.ipynb` na ordem, a partir da raiz do projeto ou de `notebooks/`. O notebook valida e trata os dados e exporta `data/clean/cf_products_with_retailers.csv`.
3. Ative o ambiente virtual, instale `requirements.txt` e execute `streamlit run app.py`.

### Função dos notebooks

- `notebooks/EDA_prática.ipynb` é a EDA original de cosméticos produzida para a Aula 11.
- `notebooks/eda.ipynb` é a cópia de trabalho e o fluxo de preparação que valida/trata os dados e exporta o CSV consumido pelo aplicativo.
- `notebooks/arquivo-eda-original.ipynb` e `notebooks/eda-com-downloads.ipynb` são materiais didáticos de referência sobre Heart Disease/UCI. Eles não são a EDA de cosméticos e não preparam o dataset do app.

`notebooks/eda.ipynb` recebeu complementações exploratórias para as métricas do Dashboard 2 e saídas dessas execuções; as análises anteriores foram preservadas. Os demais notebooks foram preservados. O fluxo de `eda.ipynb` precisa de uma cópia local do arquivo de origem em `data/raw/` para reconstruir o CSV tratado. A execução local com o CSV disponível foi testada. A licença específica e os direitos de redistribuição ainda não foram confirmados.

O arquivo de origem precisa ter as colunas esperadas pelo notebook; se a versão obtida for diferente, não renomeie outro dataset para esse caminho: confirme e prepare uma entrada compatível com o fluxo de cosméticos. O carregador precisa do arquivo em `data/clean/cf_products_with_retailers.csv`; o deploy depende de esse caminho existir no repositório publicado ou ser fornecido por outro meio configurado.

São situações distintas: obter e usar o arquivo localmente continua sujeito aos termos da fonte; colocar o arquivo em um repositório privado ainda o compartilha com os usuários autorizados; publicar no GitHub ou disponibilizar o app publicamente amplia o acesso. Nem acesso privado nem uso acadêmico, por si só, confirmam direitos de redistribuição ou publicação. Confirme a licença específica e, se necessário, obtenha autorização do responsável pela fonte antes de compartilhar dados ou resultados derivados publicamente.

### Antes de versionar outros dados tratados

- **A licença permite redistribuição?** Confirme a licença e a autorização para o dataset incluído no GitHub, mesmo em um repositório privado. A privacidade do repositório controla quem acessa o conteúdo, mas não concede autorização para redistribuí-lo. Se a autorização não for confirmada, combine uma forma aprovada de disponibilizar os dados para avaliação e execução.
- **Dado sensível** (nomes, CPF, e-mail, telefone, localização exata etc.): remova ou anonimize na EDA, antes de exportar para `data/clean/`. Isso vale mesmo em repositório privado.
- **Tamanho:** o GitHub rejeita arquivos acima de **100 MB**. Se o CSV tratado for grande, reduza colunas e linhas na EDA ou exporte em Parquet (`df.to_parquet(...)`, exige `pyarrow`).
- **Revise cada arquivo individualmente:** confirme a origem, licença e necessidade antes de adicioná-lo ao repositório. A licença e a autorização de redistribuição do CSV do aplicativo continuam pendentes de confirmação.

## Passo a passo

O passo a passo detalhado de cada aula (Aulas 21, 22 e 23), com pré-requisitos e objetivos, está em [ROTEIRO.md](ROTEIRO.md). Comece por ele depois do Setup.

## Deploy (Aula 23)

O aplicativo será publicado no Streamlit Community Cloud a partir da branch `main`, com `app.py` como arquivo principal. Após a publicação, registre aqui a URL pública final:

**Link do app:** _(preencher após o deploy; URL no formato `https://<subdominio>.streamlit.app`)_

## IA neste projeto

Este projeto usa o **streamlit skills**: um conjunto de instruções (arquivos `SKILL.md`) que a ferramenta de IA lê para escrever código Streamlit seguindo boas práticas (estrutura de layout, cache, widgets, etc.).

**Como instalar:** depois do `pip install -r requirements.txt`, rode na raiz do projeto:

```bash
streamlit skills        # interativo
streamlit skills --yes  # sem confirmações
```

O comando cria *symlinks* para as skills que acompanham a sua instalação do Streamlit, então elas se atualizam sozinhas quando você atualiza o pacote. (A opção `--global` instala para todos os projetos, em vez de só este.)

**Onde fica instalado:**

- `.claude/skills/`: lido pelo Claude Code.
- `.agents/skills/`: lido pelo Gemini CLI, que já encontra essa pasta sozinho.

Essas pastas **não são versionadas** (ver `.gitignore`): os symlinks apontam para o seu ambiente virtual e não funcionam em outra máquina. Cada pessoa roda `streamlit skills` no próprio clone.

**Se você usa outra ferramenta** (ChatGPT, Copilot Chat, etc.): abra o `SKILL.md` correspondente em `.agents/skills/` e cole o conteúdo manualmente no início do chat, antes do seu pedido.

O uso de IA deve ser declarado conforme a seção abaixo.

## Pasta `prompts/`

A pasta [prompts/](prompts) guarda só o que é sobre **uso de IA**: o template de prompt para transformar o rascunho de layout em esqueleto de código e a **Declaração de Uso de IA** exigida pelo Plano de Ensino. Veja [prompts/README.md](prompts/README.md).

## Pasta `entregas/`

A pasta [entregas/](entregas) guarda os artefatos de entrega que não são sobre IA: `rascunho-dashboard1.png` e `rascunho-dashboard2.png` representam os layouts atuais; `justificativa-metricas.md` documenta as métricas do Dashboard 2. O wireframe atual do Dashboard 1 foi atualizado após a implementação e não comprova que o rascunho precedeu o código. As imagens antigas são preservadas como referências históricas, não como representação da interface atual. Veja [entregas/README.md](entregas/README.md) para o checklist. Não coloque os entregáveis atuais no `.gitignore`.
