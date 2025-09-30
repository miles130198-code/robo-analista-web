import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from analise import aplicar_indicadores
from simulador import decidir_operacao, simular_operacoes

st.set_page_config(page_title="Robô Analista", layout="wide")
st.title("📊 Robô Analista de Trading")

ticker = st.text_input("Digite o ativo (ex: AAPL, BTC-USD):", value="AAPL")

if st.button("Simular"):
df = yf.download(ticker, period='30d', interval='15m')

if df.empty or 'Close' not in df.columns:
    st.error("Não foi possível baixar os dados. Verifique se o ativo digitado é válido.")
    st.stop()

df = aplicar_indicadores(df)

    df = decidir_operacao(df)
    resultado = simular_operacoes(df)
    st.success(f"Resultado da simulação: R$ {resultado:.2f}")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['Close'], label='Preço')
    ax.plot(df['sma_20'], label='SMA 20')
    ax.plot(df['sma_50'], label='SMA 50')
    ax.legend()
    st.pyplot(fig)
