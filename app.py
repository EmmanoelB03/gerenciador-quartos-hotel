import streamlit as st
from linkedlist import LinkedList
from stack import StackInfoGuest
import pandas as pd


# Configuração da página (deve ser o primeiro comando Streamlit)
st.set_page_config(page_title="Gerenciamento de Hotel", page_icon="🏨")


# Inicialização do estado da sessão
if 'lista_quartos_disponiveis' not in st.session_state:
    st.session_state['lista_quartos_disponiveis'] = LinkedList(['101', '102', '103', '105', '106'])

if 'lista_quartos_ocupados' not in st.session_state:
    st.session_state['lista_quartos_ocupados'] = LinkedList()

if 'info_quartos_ocupados' not in st.session_state:
    st.session_state['info_quartos_ocupados'] = StackInfoGuest()

# Atalhos para acessar os objetos do session_state
s_disponiveis = st.session_state['lista_quartos_disponiveis']
s_ocupados = st.session_state['lista_quartos_ocupados']
s_info = st.session_state['info_quartos_ocupados']


# Layout principal
st.title("🏨 Gerenciamento de Quartos de Hotel")
st.markdown("---")


# Seção de Check-In
with st.container(border=True):
    st.header("Check-In de Hóspede")

    if not s_disponiveis.is_empty():
        col1, col2 = st.columns(2)

        with col1:
            nome_hospede = st.text_input("Nome do Hóspede", key="input_nome_hospede")

        with col2:
            quarto_selecionado_checkin = st.selectbox(
                "Selecione o Quarto Disponível",
                options=s_disponiveis,
                key="select_quarto_checkin"
            )

        if st.button("Realizar Check-In"):
            if nome_hospede and quarto_selecionado_checkin:
                # Processa o check-in
                s_disponiveis.remove(quarto_selecionado_checkin)
                s_ocupados.append(quarto_selecionado_checkin)
                s_info.push(quarto_selecionado_checkin, nome_hospede)
                
                st.success(f"Check-in de {nome_hospede} no quarto {quarto_selecionado_checkin} realizado!")
                st.rerun()
            else:
                st.error("Por favor, insira o nome do hóspede.")
    else:
        st.info("Todos os quartos estão ocupados no momento.")


# Seção de Check-Out
with st.container(border=True):
    st.header("Check-Out de Hóspede")

    if not s_ocupados.is_empty():
        quarto_selecionado_checkout = st.selectbox(
            "Selecione o Quarto para Check-Out",
            options=s_ocupados,
            key="select_quarto_checkout"
        )

        if st.button("Realizar Check-Out"):
            # Processa o check-out
            s_disponiveis.append(quarto_selecionado_checkout)
            s_disponiveis.ordenar()
            s_ocupados.remove(quarto_selecionado_checkout)
            
            st.success(f"Check-out do quarto {quarto_selecionado_checkout} realizado com sucesso!")
            st.rerun()
    else:
        st.info("Não há quartos ocupados para realizar check-out.")


# Seção de informações do último check-in
st.markdown("---")
with st.container(border=True):
    st.header("Informações do Último Check-In Realizado")

    if not s_info.is_empty():
        col1, col2 = st.columns(2)
        col1.metric(label="Último Quarto Ocupado", value=s_info.return_room())
        col2.metric(label="Hóspede", value=s_info.return_guest())
    else:
        st.info("Nenhum check-in foi realizado ainda.")