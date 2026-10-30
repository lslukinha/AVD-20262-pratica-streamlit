# AVD-20262-pratica-streamlit

Repositório utilizado para aula prática relacionada a Streamlit na disciplina Análise e Visualização de Dados da Cesar School no período de 2026.2.

Repositório-modelo das Aulas 21, 22 e 23: construção de dois dashboards em Streamlit a partir da EDA desenvolvida em sala. O deploy dos dashboards ocorrerá via Streamlit Community Cloud e serão os seguintes:

- Dashboard 1 = correlação + distribuição das variáveis quantitativas
- Dashboard 2 = KPIs

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

### 2. Instalar, configurar a IA e rodar

```bash
python -m pip install -r requirements.txt

# Skills de IA do Streamlit (ver seção "IA neste projeto")
streamlit skills --yes

streamlit run app.py
```

Antes de executar o aplicativo, obtenha e prepare o dataset conforme a seção [Dados usados pelo aplicativo](#dados-usados-pelo-aplicativo).

### Problemas comuns

- **`python: command not found` / `python` não é reconhecido:** use `python3` (macOS/Linux) ou `py` (Windows) só para criar o venv; depois de ativado, `python` funciona.
- **Linux (Debian/Ubuntu): `ensurepip is not available` ou `No module named venv`:** instale `sudo apt install python3-venv` (ou `python3.X-venv` para a sua versão).
- **Windows: "a execução de scripts foi desabilitada" ao ativar no PowerShell:** rode uma vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, ou use o cmd.
- **Python fora de 3.11–3.15:** instale uma versão compatível em [python.org](https://www.python.org/downloads/) e crie o venv com ela, como no exemplo acima.
- **Apareceu `ModuleNotFoundError` ou `streamlit: command not found`:** o venv provavelmente não está ativo. Ative de novo e confira o `(.venv)` no prompt.
- **Erro de certificado no `pip install` (macOS, Python do python.org):** rode `Install Certificates.command`, na pasta Python 3.X em Aplicativos.
- **`DatasetNotFoundError` ao baixar o dataset no notebook (macOS, Python do python.org):** é o mesmo problema de certificado SSL (o `pandas` não consegue ler o CSV da UCI). Rode `Install Certificates.command` e reinicie o kernel. O notebook `eda-com-downloads.ipynb` já define `SSL_CERT_FILE` com o `certifi` como contorno.

## Estrutura de dados: `data/raw` vs `data/clean`

- `data/raw/`: o dataset **bruto**, como foi baixado. Nunca é editado à mão.
- `data/clean/`: datasets **já tratados**, exportados na última célula dos notebooks de EDA. O aplicativo atual lê `cf_products_with_retailers.csv` desta pasta, por meio de `src/data_loader.py`.

### O que vai para o Git

| Pasta | Versionada? | Por quê |
| --- | --- | --- |
| `data/raw/` | **Não** (só o `.gitkeep`) | O bruto pode ser grande ou ter dados sensíveis, e o app não o usa. |
| `data/clean/` | **Seletivamente** | A pasta inteira não é ignorada. O CSV específico usado pelo app fica local e é ignorado enquanto sua licença de redistribuição não estiver confirmada; outros arquivos tratados podem ser versionados após revisão. |

## Dados usados pelo aplicativo

O aplicativo utiliza o dataset **Cruelty Free Brands**, publicado por **mhapich** no [Kaggle](https://www.kaggle.com/datasets/mhapich/crueltyfree-brands). A licença e a autorização para redistribuir o arquivo preparado ainda não foram confirmadas. Por precaução, `data/clean/cf_products_with_retailers.csv` não é incluído no repositório; isso não significa que a licença proíba sua redistribuição.

Para executar o projeto em outro clone, obtenha os dados na fonte original e disponibilize um CSV preparado e compatível com o aplicativo neste caminho:

```text
data/clean/cf_products_with_retailers.csv
```

O notebook `notebooks/eda.ipynb` lê a entrada local `data/raw/cf_products_with_retailers.csv` e exporta o dataset tratado para o caminho acima. Se o arquivo de origem obtido não for compatível com as colunas esperadas pelo notebook, prepare um CSV equivalente antes de iniciar o app. Sem `data/clean/cf_products_with_retailers.csv`, o carregador não consegue ler os dados e o aplicativo não funciona. Como o arquivo não está no GitHub, um deploy no Streamlit Community Cloud também precisará de uma forma aprovada de disponibilizar esses dados em tempo de execução.

### Antes de versionar outros dados tratados

- **O dado é público ou pode ser compartilhado?** Se não for claramente público, use um **repositório privado** (o Community Cloud permite conectar repositórios privados ao autorizar o GitHub; confirme na hora do deploy). Nesse caso, dê acesso de leitura ao professor (como colaborador ou pela organização).
- **Dado sensível** (nomes, CPF, e-mail, telefone, localização exata etc.): remova ou anonimize na EDA, antes de exportar para `data/clean/`. Isso vale mesmo em repositório privado.
- **Tamanho:** o GitHub rejeita arquivos acima de **100 MB**. Se o CSV tratado for grande, reduza colunas e linhas na EDA ou exporte em Parquet (`df.to_parquet(...)`, exige `pyarrow`).
- **Revise cada arquivo individualmente:** confirme a origem, licença e necessidade antes de adicioná-lo ao repositório. O CSV do aplicativo citado acima permanece excluído enquanto a redistribuição não for confirmada.

## Passo a passo

O passo a passo detalhado de cada aula (Aulas 21, 22 e 23), com pré-requisitos e objetivos, está em [ROTEIRO.md](ROTEIRO.md). Comece por ele depois do Setup.

**Link do app (Aula 23):** _(preencher após o deploy)_

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

A pasta [entregas/](entregas) guarda os artefatos de entrega que não são sobre IA: os rascunhos de layout de cada dashboard (`.jpg` ou `.png`) e a justificativa das métricas do Dashboard 2. Veja [entregas/README.md](entregas/README.md) para o detalhe de cada arquivo e o checklist por aula. Não coloque esses arquivos no `.gitignore`.
