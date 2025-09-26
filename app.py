import streamlit as st
from linkedlist import LinkedList
from stack import StackInfoGuest
import pandas as pd

# --- 1. Configuração da Página ---
# Deve ser o primeiro comando Streamlit do script
st.set_page_config(page_title="Gerenciamento de Hotel", page_icon="🏨")


# --- 2. Inicialização e Gerenciamento de Estado (Session State) ---
# Este bloco garante que nossas estruturas de dados sejam criadas apenas uma vez,
# na primeira execução do aplicativo.

if 'lista_quartos_disponiveis' not in st.session_state:
    st.session_state['lista_quartos_disponiveis'] = LinkedList(['101', '102', '103', '105', '106'])

if 'lista_quartos_ocupados' not in st.session_state:
    st.session_state['lista_quartos_ocupados'] = LinkedList()

if 'info_quartos_ocupados' not in st.session_state:
    st.session_state['info_quartos_ocupados'] = StackInfoGuest()

# Criamos "atalhos" para acessar os objetos no session_state de forma mais limpa
s_disponiveis = st.session_state['lista_quartos_disponiveis']
s_ocupados = st.session_state['lista_quartos_ocupados']
s_info = st.session_state['info_quartos_ocupados']


# --- 3. Layout Principal da Interface ---

st.title("🏨 Gerenciamento de Quartos de Hotel")
st.markdown("---")


# --- 4. Seção de Check-In ---
with st.container(border=True):
    st.header("Check-In de Hóspede")

    # Verifica se há quartos disponíveis antes de mostrar as opções
    if not s_disponiveis.is_empty(): 

        col1, col2 = st.columns(2)

        with col1:
            nome_hospede = st.text_input(
                "Nome do Hóspede",
                key="input_nome_hospede"
            )

        with col2:
            quarto_selecionado_checkin = st.selectbox(
                "Selecione o Quarto Disponível",
                options=s_disponiveis, 
                key="select_quarto_checkin"
            )

        if st.button("Realizar Check-In"):
            if nome_hospede and quarto_selecionado_checkin:
                # Lógica de negócio (não foi alterada)
                s_disponiveis.remove(quarto_selecionado_checkin)
                s_ocupados.append(quarto_selecionado_checkin)
                s_info.push(quarto_selecionado_checkin, nome_hospede)
                
                st.success(f"Check-in de {nome_hospede} no quarto {quarto_selecionado_checkin} realizado!")
                st.rerun()  # Força a atualização da interface
            else:
                st.error("Por favor, insira o nome do hóspede.")
    else:
        st.info("Todos os quartos estão ocupados no momento.")


# --- 5. Seção de Check-Out ---
with st.container(border=True):
    st.header("Check-Out de Hóspede")

    # Verifica se há quartos ocupados antes de mostrar as opções
    if not s_ocupados.is_empty(): # Supondo que sua classe tenha o método is_empty()
        quarto_selecionado_checkout = st.selectbox(
            "Selecione o Quarto para Check-Out",
            options=s_ocupados,
            key="select_quarto_checkout"
        )

        if st.button("Realizar Check-Out"):
            # Lógica de negócio (não foi alterada)
            s_disponiveis.append(quarto_selecionado_checkout)
            s_ocupados.remove(quarto_selecionado_checkout)
            
            st.success(f"Check-out do quarto {quarto_selecionado_checkout} realizado com sucesso!")
            st.rerun()  # Força a atualização da interface
    else:
        st.info("Não há quartos ocupados para realizar check-out.")



st.markdown("---")
with st.container(border=True):
    # MUDANÇA 1: O título agora é mais específico.
    st.header("Informações do Último Check-In Realizado")

    # Verifica se a pilha de informações não está vazia
    if not s_info.is_empty(): 
    
        

        col1, col2 = st.columns(2)
        col1.metric(label="Último Quarto Ocupado", value=s_info.return_room())
        col2.metric(label="Hóspede", value=s_info.return_guest())
        

    else:
        # MUDANÇA 4: Mensagem de "else" um pouco mais clara.
        st.info("Nenhum check-in foi realizado ainda.")