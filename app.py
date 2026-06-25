import json
from pathlib import Path
from datetime import datetime

import streamlit as st

ARQUIVO_MENSAGENS = Path("mensagens.json")

def carregar_mensagens():
    if not ARQUIVO_MENSAGENS.exists():
        return []


    try:
        with open(ARQUIVO_MENSAGENS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_mensagens(mensagens):
    with open(ARQUIVO_MENSAGENS, "w", encoding="utf-8") as f:
        json.dump(mensagens, f, indent=4, ensure_ascii=False)

def adicionar_mensagem(mensagens, mensagem):
    print()

st.title("💬 Chat entre usuários")

username = st.text_input("Digite seu nome:", key="username", value="Anônimo")

@st.fragment(run_every=3)
def renderizar_chat():

    mensagens = carregar_mensagens()
    with st.container(border=True, height=500):
        for msg in mensagens:
            st.write(f"{msg['timestamp']} - {msg['username']}: {msg['mensagem']})")

renderizar_chat()