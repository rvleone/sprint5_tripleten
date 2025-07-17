# Analisador de Anúncios de Carros

Este é um projeto de análise de dados para a Sprint 5 do curso da TripleTen. O objetivo é criar uma aplicação web interativa com Streamlit para visualizar dados de anúncios de veículos.

A aplicação carrega um conjunto de dados de anúncios de carros e permite ao usuário gerar visualizações interativas para explorar as características dos veículos.

## Funcionalidades

- **Carregamento de Dados**: Utiliza a biblioteca Pandas para carregar os dados de um arquivo CSV (`vehicles.csv`).
- **Interface Interativa**: Construída com Streamlit, a aplicação oferece uma interface simples e amigável com botões para gerar os gráficos.
- **Visualização de Dados**: O usuário pode escolher entre duas opções de visualização:
  - **Histograma**: Gera um histograma interativo da quilometragem (`odometer`) dos veículos, permitindo analisar a distribuição dos dados.
  - **Gráfico de Dispersão**: Cria um gráfico de dispersão que mostra a relação entre a quilometragem (`odometer`) e o preço (`price`) dos veículos.

## Como Executar o Projeto

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/rvleone/sprint5_tripleten.git
    cd sprint5_tripleten
    ```

2.  **Instale as dependências:**
    Certifique-se de ter o Python instalado. Em seguida, instale as bibliotecas necessárias:

    ```bash
    pip install -r requirements.txt
    ```

    _(Se não houver um arquivo `requirements.txt`, instale manualmente: `pip install pandas plotly-express streamlit`)_

3.  **Execute a aplicação:**
    No terminal, navegue até a pasta raiz do projeto e execute o seguinte comando:

    ```bash
    streamlit run app.py
    ```

    A aplicação será aberta automaticamente no seu navegador.

    Para acessar direto pelo navegador através do Render use a URL abaixo
    https://sprint5-tripleten.onrender.com

## Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Plotly Express
