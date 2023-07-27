import streamlit as st
import pandas as pd
st.set_page_config(page_title="teste rinaldo")
with st.container():
    st.subheader("meu primeiro site")
    st.title("dashborder de Contratos")
    st.write("informacoes sobre os contratos ")
    st.write("quer aprender pyton? [clique aqui](https://www.drumond.com.br)")

@st.cache_data

def carregar_dados():
    tabela = pd.read_csv("produtos.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_vlr = st.selectbox("Selecione o periodo",["5D","10D","20D","30D"])
    num_vlr = int(qtde_vlr.replace("D", ""))
    dados=carregar_dados()
    dados= dados[-num_vlr:]

    st.area_chart(dados, x="marca", y="custo")
    
