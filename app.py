
import streamlit as st
import requests
from typing import List

WEB_APP_URL = st.secrets["google_appscript"]["web_app_url"]

def gerar_cartoes(qtd: int) -> List[str]:
    return [f"Relato #{i}" for i in range(1, qtd+1)]

def salvar_no_sheets(cards: List[str]) -> bool:
    resp = requests.post(WEB_APP_URL, json={"cards": cards}, timeout=5)
    resp.raise_for_status()
    return True

st.title("Meu App com Sheets Privado")
qtd = st.number_input("Quantos cartões?", 1, 50, 5)
if st.button("Executar"):
    cards = gerar_cartoes(qtd)
    for idx, txt in enumerate(cards, 1):
        st.write(f"{idx}. {txt}")
    if salvar_no_sheets(cards):
        st.success("Gravado no Google Sheets!")

st.set_page_config(layout="centered")
st.title("📋 Formulário de Relatos Operacionais")

# Menu de seleção do formulário
formulario = st.selectbox("Selecione o tipo de formulário", [
    "Vi Você Fazendo Certo",
    "Registro de Falha",
    "Recusa de Tarefa",
    "Atitude Segura"
])

# Função para formatar a data
def formatar_data(data):
    return data.strftime('%d/%m/%Y')

if formulario == "Vi Você Fazendo Certo":
    st.subheader("👀 Vi Você Fazendo Certo")
    nome = st.text_input("Nome do reconhecido:")
    data = st.date_input("Data:", value=date.today())
    celula = st.text_input("Célula:")
    descricao = st.text_area("Descrição dos fatos:")

    if st.button("Enviar"):
        st.success(f"Dados enviados para: {nome} em {formatar_data(data)}")

elif formulario == "Registro de Falha":
    st.subheader("⚠️ Registro de Falha")
    nome = st.text_input("Colaborador:")
    data = st.date_input("Data:", value=date.today())
    celula = st.text_input("Célula:")
    local = st.text_input("Local da Ocorrência:")
    severidade = st.multiselect("Severidade:", ["A", "B", "C"])
    seguranca = st.multiselect("Segurança:", ["Meio Ambiente", "CDM", "Quase Acidente", "Condição Abaixo do Padrão"])
    meioamb = st.multiselect("Meio Ambiente:", ["Potencial (Risco de vazamento)", "Real (vazamento já Ocorreu)"])
    descricao = st.text_area("Descrição dos fatos:")
    acao_imediata = st.text_area("Ação imediata:")
    acao_proposta = st.text_area("Ação proposta:")

    if st.button("Enviar"):
        st.success(f"Falha registrada para {nome} em {formatar_data(data)}")

elif formulario == "Recusa de Tarefa":
    st.subheader("🙅‍♂️ Recusa de Tarefa")
    nome = st.text_input("Colaborador:")
    data = st.date_input("Data:", value=date.today())
    celula = st.text_input("Célula:")
    local = st.text_input("Local da Ocorrência:")
    tipo = st.radio("Tipo:", ["Segurança", "Meio ambiente", "Qualidade"])
    descricao = st.text_area("Descrição dos fatos:")
    acao = st.text_area("Ação Imediata:")
    parecer = st.text_area("Parecer do Coordenador:")

    if st.button("Enviar"):
        st.success(f"Tarefa recusada por {nome} em {formatar_data(data)}")

elif formulario == "Atitude Segura":
    st.subheader("🛡️ Atitude Segura")
    nome = st.text_input("Nome do observador:")
    data = st.date_input("Data:", value=date.today())
    celula = st.text_input("Célula:")
    ambiente = st.radio("Onde ocorreu?", ["No trabalho", "Em casa", "No trânsito"])
    fatores = st.multiselect("Fatores do Comportamento:", ["Velocidade inadequada (pressa)", "Falta de entusiasmo", "Fadiga", "Displicência"])
    desvios = st.multiselect("Desvio do Comportamento:", ["Distração (olhos)", "Falta de Concentração", "Posição incorreta", "Falta de Estabilidade"])
    envolvimento = st.radio("Quem?", ["Eu", "Outros"])
    potencial = st.multiselect("Potencial da Lesão:", ["Alto", "Médio", "Baixo"])
    descricao = st.text_area("Descrição dos Fatos:")

    if st.button("Enviar"):
        st.success(f"Atitude segura registrada por {nome} em {formatar_data(data)}")
