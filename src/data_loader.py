from pathlib import Path

import pandas as pd
import streamlit as st


CAMINHO_DATASET = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "clean"
    / "cf_products_with_retailers.csv"
)


@st.cache_data
def load_data():
    """Carrega o dataset tratado de cosméticos a partir da raiz do projeto."""
    return pd.read_csv(CAMINHO_DATASET)
