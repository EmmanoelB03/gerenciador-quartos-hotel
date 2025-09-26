# 🏨 Gerenciador de Quartos de Hotel com Streamlit

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Um projeto web interativo para simular o gerenciamento de check-in e check-out de um hotel, utilizando estruturas de dados fundamentais como Listas Ligadas e Pilhas.

## 📜 Sobre o Projeto

Este projeto é uma aplicação web simples, desenvolvida com a biblioteca **Streamlit**, que serve como uma demonstração prática do uso de Estruturas de Dados para resolver um problema do mundo real.

A aplicação gerencia quartos de hotel, movendo-os entre listas de "Disponíveis" e "Ocupados", e mantém um registro das informações dos hóspedes. O principal objetivo é aplicar os conceitos de:

* **`LinkedList` (Lista Ligada):** Para gerenciar as listas de quartos disponíveis e ocupados de forma eficiente.
* **`Stack` (Pilha):** Para armazenar as informações dos hóspedes que realizaram check-in, seguindo o princípio LIFO (Last-In, First-Out) para exibir o último hóspede a entrar.

---

## 📸 Visão Geral

<p align="center">
  <img src="URL_DO_SEU_GIF_OU_IMAGEM_AQUI" alt="Demonstração do Gerenciador de Hotel" width="700"/>
</p>

---

## ✨ Funcionalidades

* ✔️ **Check-In de Hóspede:** Permite selecionar um quarto disponível e registrar o nome de um hóspede. O quarto é movido da lista de disponíveis para a de ocupados.
* ✔️ **Check-Out de Hóspede:** Permite selecionar um quarto ocupado para liberá-lo. O quarto retorna para a lista de disponíveis.
* ✔️ **Visualização de Status:** Exibe de forma clara as listas de quartos disponíveis e ocupados em tempo real.
* ✔️ **Registro de Informações:** Utiliza uma pilha para exibir os detalhes do último hóspede que realizou o check-in.
* ✔️ **Interface Reativa:** Interface de usuário limpa e interativa construída com Streamlit.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3
* **Framework Web:** Streamlit
* **Manipulação de Dados:** Pandas (para exibição em tabelas)
* **Estruturas de Dados Implementadas:**
    * `Node`: Estrutura base para os nós da lista e da pilha.
    * `LinkedList`: Gerenciamento dinâmico dos quartos.
    * `Stack`: Armazenamento das informações de check-in dos hóspedes.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar a aplicação em seu ambiente local.

### **Pré-requisitos**

* [Python 3.9](https://www.python.org/downloads/) ou superior
* [Git](https://git-scm.com/downloads)

### **Instalação**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/EmmanoelB03/gerenciador-quartos-hotel.git](https://github.com/EmmanoelB03/gerenciador-quartos-hotel.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd gerenciador-quartos-hotel
    ```

3.  **(Recomendado) Crie e ative um ambiente virtual:**
    Como você usa Ubuntu, os comandos são:
    ```bash
    # Criar o ambiente
    python3 -m venv venv

    # Ativar o ambiente
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### **Execução**

Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no seu terminal:

```bash
streamlit run app.py
