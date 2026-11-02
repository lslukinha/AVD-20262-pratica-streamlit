import inspect

import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

from src.data_loader import load_data


st.set_page_config(page_title="Análise de marcas de cosméticos", layout="wide")

st.title("Análise de marcas de cosméticos")
st.subheader("Presença em redes varejistas e características das marcas")

df = load_data()

VAREJISTAS = ["Ulta", "Sephora", "Beauty_Bay", "Cult_Beauty", "Nordstrom"]
VARIAVEIS_DISTRIBUICAO = ["total_retailers", "total_retailers_log"]
COR_FUNDO = "#0e1117"
COR_SUPERFICIE = "#262730"
COR_TEXTO = "#fafafa"
COR_GRADE = "#41444e"
COR_DESTAQUE = "#c1121f"
COR_DESTAQUE_CLARO = "#f28482"
ROTULOS_VAREJISTAS = {
    "Ulta": "Ulta",
    "Sephora": "Sephora",
    "Beauty_Bay": "Beauty Bay",
    "Cult_Beauty": "Cult Beauty",
    "Nordstrom": "Nordstrom",
}
FILTROS_BOOLEANOS = {
    "All_vegan": "Marca 100% vegana",
    "Partial_vegan": "Marca parcialmente vegana",
    "Bad_parent_company": "Empresa-mãe testa em animais",
    "Black_owned": "Marca pertencente a pessoas negras",
}
OPCOES_BOOLEANAS = ["Todos", "Sim", "Não"]
VALOR_BOOLEANO = {"Sim": True, "Não": False}

def formatar_percentual(valor):
    return f"{valor:.2f}".replace(".", ",")


def formatar_kpi(contagem, denominador):
    percentual = formatar_percentual(contagem / denominador * 100)
    return f"{contagem} ({percentual}%)"


def tema_altair(grafico):
    return grafico.configure(
        background=COR_FUNDO,
        view=alt.ViewConfig(fill=COR_SUPERFICIE, stroke=COR_GRADE),
        axis=alt.AxisConfig(
            labelColor=COR_TEXTO,
            titleColor=COR_TEXTO,
            domainColor=COR_GRADE,
            tickColor=COR_GRADE,
            gridColor=COR_GRADE,
            gridOpacity=0.5,
        ),
        title=alt.TitleConfig(color=COR_TEXTO),
        legend=alt.LegendConfig(labelColor=COR_TEXTO, titleColor=COR_TEXTO),
    )


def exibir_grafico_altair(grafico):
    if "width" in inspect.signature(st.altair_chart).parameters:
        st.altair_chart(grafico, width="stretch")
    else:
        # Streamlit 1.50 ainda usa use_container_width.
        st.altair_chart(grafico, use_container_width=True)


OPCOES_DASHBOARD = [
    "Dashboard 1 — Análise exploratória",
    "Dashboard 2 — Presença e perfil das marcas",
]
CHAVES_FILTROS = {
    "filtro_All_vegan": "Todos",
    "filtro_Partial_vegan": "Todos",
    "filtro_Bad_parent_company": "Todos",
    "filtro_Black_owned": "Todos",
    "redes_varejistas": VAREJISTAS.copy(),
    "variaveis_distribuicao": ["total_retailers"],
    "filtro_total_retailers": (0, 5),
    "d2_redes_varejistas": VAREJISTAS.copy(),
    "d2_bad_parent_company": "Todos",
    "d2_all_vegan": "Todos",
}

# Widgets de uma aba deixam de ser renderizados quando a outra está ativa.
# Guardamos seus valores no estado de sessão e os restauramos ao voltar.
for chave, valor_inicial in CHAVES_FILTROS.items():
    chave_salva = f"_salvo_{chave}"
    if chave in st.session_state:
        st.session_state[chave_salva] = st.session_state[chave]
    elif chave_salva not in st.session_state:
        st.session_state[chave_salva] = valor_inicial

dashboard_ativo = st.radio(
    "Dashboard",
    options=OPCOES_DASHBOARD,
    horizontal=True,
    key="dashboard_ativo",
    label_visibility="collapsed",
)

if dashboard_ativo == OPCOES_DASHBOARD[0]:
    with st.sidebar:
        st.header("Filtros do Dashboard 1")
        escolhas_booleanas = {}
        for coluna, rotulo in FILTROS_BOOLEANOS.items():
            chave = f"filtro_{coluna}"
            if chave not in st.session_state:
                st.session_state[chave] = st.session_state[f"_salvo_{chave}"]
            escolhas_booleanas[coluna] = st.selectbox(
                rotulo,
                options=OPCOES_BOOLEANAS,
                key=chave,
            )

        if "redes_varejistas" not in st.session_state:
            st.session_state.redes_varejistas = st.session_state._salvo_redes_varejistas
        variaveis = st.multiselect(
            "Redes varejistas para analisar",
            options=VAREJISTAS,
            format_func=lambda valor: ROTULOS_VAREJISTAS[valor],
            key="redes_varejistas",
            help="A seleção define as redes disponíveis para a análise de correlação.",
        )
        if "variaveis_distribuicao" not in st.session_state:
            st.session_state.variaveis_distribuicao = st.session_state._salvo_variaveis_distribuicao
        variaveis_distribuicao = st.multiselect(
            "Variáveis quantitativas para distribuição",
            options=VARIAVEIS_DISTRIBUICAO,
            key="variaveis_distribuicao",
            help=(
                "Escolha a contagem de redes por marca ou sua transformação logarítmica. "
                "Os indicadores binários das redes são usados na correlação."
            ),
        )
        if "filtro_total_retailers" not in st.session_state:
            st.session_state.filtro_total_retailers = st.session_state._salvo_filtro_total_retailers
        intervalo_total = st.slider(
            "Total de redes varejistas por marca",
            min_value=0,
            max_value=5,
            step=1,
            key="filtro_total_retailers",
            help="Filtra as marcas pelo número de redes varejistas em que estão presentes.",
        )

    # Os mesmos filtros e a mesma regra de seleção do Dashboard 1.
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

    st.subheader("Correlação entre as redes varejistas")
    if len(variaveis) == 0:
        st.info("Selecione pelo menos duas redes para exibir o heatmap de correlação.")
    elif len(variaveis) == 1:
        st.info(
            "Uma variável não permite calcular correlação entre redes. "
            "Selecione pelo menos duas."
        )
    elif df_filtrado.empty:
        st.info("Nenhuma marca corresponde aos filtros; não há dados para calcular a correlação.")
    else:
        correlacao = df_filtrado[variaveis].corr(method="spearman")
        fig, ax = plt.subplots(figsize=(7, 5))
        fig.set_facecolor(COR_FUNDO)
        ax.set_facecolor(COR_SUPERFICIE)
        correlacao_exibicao = correlacao.rename(
            index=ROTULOS_VAREJISTAS,
            columns=ROTULOS_VAREJISTAS,
        )
        sns.heatmap(
            correlacao_exibicao,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            vmin=-1,
            vmax=1,
            center=0,
            square=True,
            ax=ax,
            cbar_kws={"label": "Correlação de Spearman"},
        )
        for texto, valor in zip(ax.texts, correlacao.to_numpy().flatten()):
            texto.set_color(COR_TEXTO if abs(valor) >= 0.55 else COR_FUNDO)
            texto.set_fontweight("bold")
        ax.set_title("Correlação de Spearman", color=COR_TEXTO, pad=12)
        ax.tick_params(axis="both", colors=COR_TEXTO)
        ax.set_xlabel("")
        ax.set_ylabel("")
        colorbar = ax.collections[0].colorbar
        colorbar.ax.yaxis.set_tick_params(color=COR_TEXTO)
        colorbar.ax.yaxis.label.set_color(COR_TEXTO)
        plt.setp(colorbar.ax.get_yticklabels(), color=COR_TEXTO)
        fig.tight_layout()
        st.pyplot(fig, width="stretch")
        plt.close(fig)

    st.subheader("Distribuição das variáveis quantitativas")
    if not variaveis_distribuicao:
        st.info("Selecione pelo menos uma variável quantitativa para exibir sua distribuição.")
    elif df_filtrado.empty:
        st.info("Nenhuma marca corresponde aos filtros; não há dados para exibir a distribuição.")
    else:
        colunas_histogramas = st.columns(len(variaveis_distribuicao))
        for coluna, variavel in zip(colunas_histogramas, variaveis_distribuicao):
            fig, ax = plt.subplots(figsize=(6, 4))
            fig.set_facecolor(COR_FUNDO)
            ax.set_facecolor(COR_SUPERFICIE)
            if variavel == "total_retailers":
                sns.histplot(
                    data=df_filtrado,
                    x=variavel,
                    bins=[valor - 0.5 for valor in range(7)],
                    color=COR_DESTAQUE,
                    edgecolor=COR_TEXTO,
                    linewidth=0.8,
                    ax=ax,
                )
                ax.set_xticks(range(6), labels=[str(valor) for valor in range(6)])
                ax.set_xlim(-0.5, 5.5)
            else:
                sns.histplot(
                    data=df_filtrado,
                    x=variavel,
                    bins=20,
                    color=COR_DESTAQUE,
                    edgecolor=COR_TEXTO,
                    linewidth=0.8,
                    ax=ax,
                )
            rotulo_variavel = {
                "total_retailers": "Quantidade de redes varejistas",
                "total_retailers_log": "Quantidade de redes varejistas (escala logarítmica)",
            }[variavel]
            ax.set_title(f"Distribuição: {rotulo_variavel}", color=COR_TEXTO, pad=10)
            ax.set_xlabel(rotulo_variavel, color=COR_TEXTO)
            ax.set_ylabel("Número de marcas", color=COR_TEXTO)
            ax.tick_params(axis="both", colors=COR_TEXTO)
            ax.grid(axis="y", color=COR_GRADE, alpha=0.55)
            ax.set_axisbelow(True)
            fig.tight_layout()
            coluna.pyplot(fig, width="stretch")
            plt.close(fig)

    st.subheader("Marcas por quantidade de redes varejistas")
    frequencias = (
        df_filtrado["total_retailers"]
        .value_counts()
        .reindex(range(6), fill_value=0)
        .rename_axis("Quantidade de redes")
        .rename("Número de marcas")
    )
    fig, ax = plt.subplots(figsize=(8, 3.8))
    fig.set_facecolor(COR_FUNDO)
    ax.set_facecolor(COR_SUPERFICIE)
    barras = ax.barh(
        [str(valor) for valor in frequencias.index],
        frequencias.values,
        color=COR_DESTAQUE,
        edgecolor=COR_DESTAQUE_CLARO,
        linewidth=0.8,
    )
    ax.bar_label(
        barras,
        labels=[str(valor) for valor in frequencias.values],
        padding=6,
        color=COR_TEXTO,
    )
    ax.set_title("Marcas por quantidade de redes varejistas", color=COR_TEXTO, pad=10)
    ax.set_xlabel("Número de marcas", color=COR_TEXTO)
    ax.set_ylabel("Quantidade de redes", color=COR_TEXTO)
    ax.tick_params(axis="both", colors=COR_TEXTO)
    ax.grid(axis="x", color=COR_GRADE, alpha=0.55)
    ax.set_axisbelow(True)
    ax.set_xlim(0, max(int(frequencias.max()) * 1.18, 1))
    fig.tight_layout()
    st.pyplot(fig, width="stretch")
    plt.close(fig)


else:
    with st.sidebar:
        st.header("Filtros do Dashboard 2")
        if "d2_redes_varejistas" not in st.session_state:
            st.session_state.d2_redes_varejistas = st.session_state._salvo_d2_redes_varejistas
        redes_selecionadas = st.multiselect(
            "Redes varejistas",
            options=VAREJISTAS,
            format_func=lambda valor: ROTULOS_VAREJISTAS[valor],
            key="d2_redes_varejistas",
            help="Define quais colunas 0/1 entram nas contagens de presença.",
        )
        if "d2_bad_parent_company" not in st.session_state:
            st.session_state.d2_bad_parent_company = st.session_state._salvo_d2_bad_parent_company
        filtro_parent = st.selectbox(
            "Empresa-mãe testa em animais",
            options=OPCOES_BOOLEANAS,
            key="d2_bad_parent_company",
        )
        if "d2_all_vegan" not in st.session_state:
            st.session_state.d2_all_vegan = st.session_state._salvo_d2_all_vegan
        filtro_vegan = st.selectbox(
            "Marca 100% vegana",
            options=OPCOES_BOOLEANAS,
            key="d2_all_vegan",
        )
        st.caption(
            "Pertencimento a pessoas negras é dimensão da comparação, não um filtro. "
            "Os filtros de coorte são aplicados igualmente aos dois grupos."
        )

    st.header("Presença e perfil das marcas")
    st.caption(
        "A presença é a registrada na base; não representa vendas, demanda ou "
        "disponibilidade atual de produtos."
    )

    df_coorte_kpi_vegano = df
    if filtro_parent != "Todos":
        df_coorte_kpi_vegano = df_coorte_kpi_vegano[
            df_coorte_kpi_vegano["Bad_parent_company"]
            == VALOR_BOOLEANO[filtro_parent]
        ]

    tamanho_coorte_kpi_vegano = len(df_coorte_kpi_vegano)
    marcas_veganas = int(df_coorte_kpi_vegano["All_vegan"].sum())

    df_coorte = df_coorte_kpi_vegano
    if filtro_vegan != "Todos":
        df_coorte = df_coorte[df_coorte["All_vegan"] == VALOR_BOOLEANO[filtro_vegan]]

    tamanho_coorte = len(df_coorte)
    if redes_selecionadas:
        quantidade_redes = df_coorte[redes_selecionadas].sum(axis=1).astype(int)
    else:
        quantidade_redes = pd.Series(index=df_coorte.index, dtype="int64")

    presenca_em_rede = quantidade_redes >= 1
    presenca_em_duas_redes = quantidade_redes >= 2
    valor_presenca = "—"
    valor_duas_redes = "—"
    valor_veganas = (
        "—"
        if tamanho_coorte_kpi_vegano == 0
        else formatar_kpi(marcas_veganas, tamanho_coorte_kpi_vegano)
    )
    ajuda_presenca = "Selecione pelo menos uma rede para calcular este KPI."
    ajuda_duas_redes = "Selecione redes para calcular este KPI."
    ajuda_veganas = (
        "Percentual calculado após os demais filtros de coorte e antes do filtro "
        "Marca 100% vegana. A seleção de redes também não altera este KPI. "
        f"Denominador: {tamanho_coorte_kpi_vegano} marcas."
    )

    if tamanho_coorte > 0 and redes_selecionadas:
        total_presenca = int(presenca_em_rede.sum())
        valor_presenca = formatar_kpi(total_presenca, tamanho_coorte)
        ajuda_presenca = f"{total_presenca} de {tamanho_coorte} marcas da coorte atual."
        if len(redes_selecionadas) >= 2:
            total_duas_redes = int(presenca_em_duas_redes.sum())
            valor_duas_redes = formatar_kpi(total_duas_redes, tamanho_coorte)
            ajuda_duas_redes = f"{total_duas_redes} de {tamanho_coorte} marcas da coorte atual."
        else:
            valor_duas_redes = "N/A"
            ajuda_duas_redes = "Inaplicável com uma rede; selecione pelo menos duas."

    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    with col_kpi1:
        st.metric("Marcas presentes em pelo menos uma rede", valor_presenca, help=ajuda_presenca)
    with col_kpi2:
        st.metric("Marcas presentes em duas ou mais redes", valor_duas_redes, help=ajuda_duas_redes)
    with col_kpi3:
        st.metric("Marcas marcadas como 100% veganas", valor_veganas, help=ajuda_veganas)

    st.caption(
        f"Coorte dos KPIs de presença e dos gráficos: N = {tamanho_coorte} marcas. "
        f"O KPI vegano usa N = {tamanho_coorte_kpi_vegano}, após os demais filtros "
        "de coorte e antes do filtro Marca 100% vegana."
    )

    if tamanho_coorte == 0:
        st.warning("A coorte está vazia com os filtros selecionados. Ajuste os filtros para ver os gráficos.")
    elif not redes_selecionadas:
        st.info("Selecione pelo menos uma rede. Os KPIs de presença e os gráficos de varejo aguardam essa seleção.")
    elif len(redes_selecionadas) == 1:
        st.info("Com uma rede selecionada, o KPI de duas ou mais redes é inaplicável.")

    st.subheader("Presença registrada por rede varejista")
    if tamanho_coorte == 0:
        st.info("Não há marcas na coorte para calcular presença por rede.")
    elif not redes_selecionadas:
        st.info("Selecione pelo menos uma rede para exibir este gráfico.")
    else:
        contagens_rede = df_coorte[redes_selecionadas].sum().astype(int)
        percentuais_rede = contagens_rede / tamanho_coorte * 100
        dados_rede = pd.DataFrame(
            {
                "Rede": [ROTULOS_VAREJISTAS[rede] for rede in contagens_rede.index],
                "Contagem": contagens_rede.to_numpy(),
                "Percentual": percentuais_rede.to_numpy(),
            }
        )
        dados_rede["PercentualFormatado"] = dados_rede["Percentual"].map(
            lambda valor: f"{formatar_percentual(valor)}%"
        )
        dados_rede["Rotulo"] = [
            f"{contagem} ({formatar_percentual(percentual)}%)"
            for contagem, percentual in zip(
                dados_rede["Contagem"], dados_rede["Percentual"]
            )
        ]
        hover_rede = alt.selection_point(
            name="hover_rede",
            fields=["Rede"],
            on="pointerover",
            clear="pointerout",
        )
        limite_rede = max(int(contagens_rede.max()) * 1.4, 1)
        barras_rede = (
            alt.Chart(dados_rede)
            .mark_bar(stroke=COR_DESTAQUE_CLARO, strokeWidth=0.8)
            .encode(
                x=alt.X(
                    "Contagem:Q",
                    title="Número de marcas",
                    scale=alt.Scale(domain=[0, limite_rede]),
                ),
                y=alt.Y("Rede:N", title="Rede varejista", sort=dados_rede["Rede"].tolist()),
                color=alt.condition(
                    hover_rede,
                    alt.value(COR_DESTAQUE_CLARO),
                    alt.value(COR_DESTAQUE),
                ),
                tooltip=[
                    alt.Tooltip("Rede:N", title="Rede"),
                    alt.Tooltip("Contagem:Q", title="Quantidade de marcas", format="d"),
                    alt.Tooltip("PercentualFormatado:N", title="Percentual"),
                ],
            )
            .add_params(hover_rede)
        )
        rotulos_rede = alt.Chart(dados_rede).mark_text(
            align="left", dx=6, color=COR_TEXTO, fontSize=11
        ).encode(
            x=alt.X("Contagem:Q", scale=alt.Scale(domain=[0, limite_rede])),
            y=alt.Y("Rede:N", sort=dados_rede["Rede"].tolist()),
            text=alt.Text("Rotulo:N"),
        )
        grafico_rede = tema_altair(
            (barras_rede + rotulos_rede).properties(
                height=max(180, 42 * len(redes_selecionadas)),
            )
        )
        exibir_grafico_altair(grafico_rede)

    col_distribuicao, col_comparacao = st.columns([1, 1])
    with col_distribuicao:
        st.subheader("Distribuição por quantidade de redes")
        if tamanho_coorte == 0:
            st.info("Não há marcas na coorte para exibir a distribuição.")
        elif not redes_selecionadas:
            st.info("Selecione redes para definir as categorias da distribuição.")
        else:
            categorias = range(len(redes_selecionadas) + 1)
            frequencias = quantidade_redes.value_counts().reindex(categorias, fill_value=0)
            dados_distribuicao = pd.DataFrame(
                {
                    "Quantidade": list(categorias),
                    "Marcas": frequencias.to_numpy(dtype=int),
                }
            )
            dados_distribuicao["Percentual"] = (
                dados_distribuicao["Marcas"] / tamanho_coorte * 100
            )
            dados_distribuicao["PercentualFormatado"] = dados_distribuicao[
                "Percentual"
            ].map(lambda valor: f"{formatar_percentual(valor)}%")
            dados_distribuicao["Cor"] = [
                COR_DESTAQUE if quantidade == 0 else COR_DESTAQUE_CLARO
                for quantidade in dados_distribuicao["Quantidade"]
            ]
            limite_distribuicao = max(int(frequencias.max()) * 1.1, 1)
            barras_distribuicao = (
                alt.Chart(dados_distribuicao)
                .mark_bar(stroke=COR_TEXTO, strokeWidth=0.6)
                .encode(
                    x=alt.X(
                        "Quantidade:O",
                        title="Redes com presença registrada",
                        sort=list(categorias),
                        axis=alt.Axis(labelAngle=0),
                    ),
                    y=alt.Y(
                        "Marcas:Q",
                        title="Número de marcas",
                        scale=alt.Scale(domain=[0, limite_distribuicao]),
                    ),
                    color=alt.Color("Cor:N", scale=None, legend=None),
                    tooltip=[
                        alt.Tooltip("Quantidade:Q", title="Quantidade de redes", format="d"),
                        alt.Tooltip("Marcas:Q", title="Número de marcas", format="d"),
                        alt.Tooltip(
                            "PercentualFormatado:N",
                            title="Percentual da coorte",
                        ),
                    ],
                )
            )
            rotulos_distribuicao = alt.Chart(dados_distribuicao).mark_text(
                dy=-7, color=COR_TEXTO, fontSize=11
            ).encode(
                x=alt.X("Quantidade:O", sort=list(categorias)),
                y=alt.Y("Marcas:Q", scale=alt.Scale(domain=[0, limite_distribuicao])),
                text=alt.Text("Marcas:Q", format="d"),
            )
            grafico_distribuicao = tema_altair(
                (barras_distribuicao + rotulos_distribuicao).properties(
                    height=330,
                )
            )
            exibir_grafico_altair(grafico_distribuicao)
            st.caption(f"Categorias de 0 a {len(redes_selecionadas)} · N = {tamanho_coorte}.")

    with col_comparacao:
        st.subheader("Comparação por pertencimento a pessoas negras")
        if tamanho_coorte == 0:
            st.info("Não há marcas na coorte para comparar os grupos.")
        elif not redes_selecionadas:
            st.info("Selecione pelo menos uma rede para comparar a presença entre os grupos.")
        else:
            grupos = []
            grupos_vazios = []
            for rotulo, valor_black_owned in [
                ("Marcas pertencentes a pessoas negras", True),
                ("Demais marcas", False),
            ]:
                grupo = df_coorte[df_coorte["Black_owned"] == valor_black_owned]
                denominador = len(grupo)
                if denominador == 0:
                    grupos_vazios.append(rotulo)
                    continue
                presentes = int((grupo[redes_selecionadas].sum(axis=1) >= 1).sum())
                percentual = presentes / denominador * 100
                grupos.append((rotulo, presentes, denominador, percentual))

            if grupos_vazios:
                st.info(
                    "Sem marcas no grupo: " + ", ".join(grupos_vazios) + ". "
                    "O grupo não foi usado como filtro."
                )

            if grupos:
                dados_grupos = pd.DataFrame(
                    [
                        {
                            "Grupo": rotulo,
                            "Presentes": presentes,
                            "Denominador": denominador,
                            "Percentual": percentual,
                            "Cor": (
                                COR_DESTAQUE
                                if rotulo == "Marcas pertencentes a pessoas negras"
                                else COR_DESTAQUE_CLARO
                            ),
                            "Rotulo": (
                                f"{presentes}/{denominador} "
                                f"({formatar_percentual(percentual)}%)"
                            ),
                        }
                        for rotulo, presentes, denominador, percentual in grupos
                    ]
                )
                limite_grupos = max(max(grupo[3] for grupo in grupos) * 1.45, 1)
                barras_grupos = alt.Chart(dados_grupos).mark_bar(
                    stroke=COR_TEXTO, strokeWidth=0.6
                ).encode(
                    x=alt.X(
                        "Percentual:Q",
                        title="Marcas presentes no grupo (%)",
                        scale=alt.Scale(domain=[0, limite_grupos]),
                    ),
                    y=alt.Y(
                        "Grupo:N",
                        title="Grupo",
                        sort=dados_grupos["Grupo"].tolist(),
                    ),
                    color=alt.Color("Cor:N", scale=None, legend=None),
                    tooltip=[
                        alt.Tooltip("Grupo:N", title="Grupo"),
                        alt.Tooltip("Presentes:Q", title="Numerador", format="d"),
                        alt.Tooltip("Denominador:Q", title="Denominador", format="d"),
                        alt.Tooltip("Rotulo:N", title="Percentual"),
                    ],
                )
                rotulos_grupos = alt.Chart(dados_grupos).mark_text(
                    align="left", dx=6, color=COR_TEXTO, fontSize=10
                ).encode(
                    x=alt.X("Percentual:Q", scale=alt.Scale(domain=[0, limite_grupos])),
                    y=alt.Y("Grupo:N", sort=dados_grupos["Grupo"].tolist()),
                    text=alt.Text("Rotulo:N"),
                )
                grafico_grupos = tema_altair(
                    (barras_grupos + rotulos_grupos).properties(
                        height=250,
                    )
                )
                exibir_grafico_altair(grafico_grupos)
            else:
                st.info("Nenhum dos grupos tem marcas na coorte atual.")

            st.caption(
                "Comparação descritiva; não demonstra causalidade. "
                "Os rótulos mostram numerador e denominador próprios de cada grupo."
            )
