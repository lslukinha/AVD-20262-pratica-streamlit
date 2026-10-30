import streamlit as st

from src.data_loader import load_data


st.set_page_config(page_title="Análise de marcas de cosméticos", layout="wide")

st.title("Análise de marcas de cosméticos")
st.subheader("Presença em redes varejistas e características das marcas")

df = load_data()

VAREJISTAS = ["Ulta", "Sephora", "Beauty_Bay", "Cult_Beauty", "Nordstrom"]
FILTROS_BOOLEANOS = {
    "All_vegan": "Marca 100% vegana",
    "Partial_vegan": "Marca parcialmente vegana",
    "Bad_parent_company": "Empresa-mãe testa em animais",
    "Black_owned": "Marca pertencente a pessoas negras",
}
OPCOES_BOOLEANAS = ["Todos", "Sim", "Não"]
VALOR_BOOLEANO = {"Sim": True, "Não": False}

with st.sidebar:
    st.header("Filtros")

    escolhas_booleanas = {
        coluna: st.selectbox(
            rotulo,
            options=OPCOES_BOOLEANAS,
            index=0,
            key=f"filtro_{coluna}",
        )
        for coluna, rotulo in FILTROS_BOOLEANOS.items()
    }

    variaveis = st.multiselect(
        "Redes varejistas para analisar",
        options=VAREJISTAS,
        default=VAREJISTAS,
        help="A seleção define as redes disponíveis para a análise de correlação da Aula 22.",
    )

    intervalo_total = st.slider(
        "Total de redes varejistas por marca",
        min_value=0,
        max_value=5,
        value=(0, 5),
        step=1,
        help="Filtra as marcas pelo número de redes varejistas em que estão presentes.",
    )

# Aplica os filtros categóricos e o intervalo à tabela de marcas.
df_filtrado = df
for coluna, escolha in escolhas_booleanas.items():
    if escolha != "Todos":
        df_filtrado = df_filtrado[df_filtrado[coluna] == VALOR_BOOLEANO[escolha]]

inicio_total, fim_total = intervalo_total
df_filtrado = df_filtrado[
    df_filtrado["total_retailers"].between(inicio_total, fim_total)
]

st.caption(
    f"{len(df_filtrado)} de {len(df)} marcas correspondem aos filtros selecionados."
)

# Estrutura do Dashboard 1: os gráficos serão incluídos na Aula 22.
col_correlacao, col_distribuicao = st.columns([1, 1.5])

with col_correlacao:
    st.subheader("Correlação entre as redes varejistas")
    if len(variaveis) < 2:
        st.info("Selecione pelo menos duas redes para preparar a análise de correlação.")
    else:
        st.info(
            "Placeholder da Aula 21: a visualização de correlação entre "
            f"{len(variaveis)} redes será implementada na Aula 22."
        )

with col_distribuicao:
    st.subheader("Distribuição de total_retailers")
    st.info(
        "Placeholder da Aula 21: a visualização da distribuição do total de redes "
        "por marca será implementada na Aula 22."
    )
