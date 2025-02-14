import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
import numpy as np
from streamlit_plotly_events import plotly_events
from IPython.display import display


#Configuração gerais das páginas
st.set_page_config(page_title='Pós-Tech FIAP | Datathon | Grupo 59', page_icon=":chart_with_upwards_trend:", layout= 'wide')


# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM 354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Datathon | Grupo 59 | Imagem disponível em: vide bibliografia")


st.header('Metodologia')


## Visualização no Streamlit
# Abas ('Tabs')
aba1, aba2 = st.tabs(['Metodologia', 'Plano para deploy'])
# aba1

with aba1:
    st.write('''#### Metodologia do modelo de Machine Learning''')
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.info('''__1. Coleta de Dados__''')
        st.write('''- :blue[__Fonte dos Dados__]: Os dados foram extraídos do arquivo __PEDE 2024 - Dataton__, encontrado no diretório do Google Drive, devidamente referenciado na seção de *"Referências bibliográficas - Base de dados: PEDE 2024 (arquivo bruto), antes de ser tratado no BigQuery"*.''')
        st.info(''' __2. Limpeza e Preparação dos Dados__''')
        st.write('''- :blue[__Tratamento dos dados__]: Utilizou-se o *BigQuery com SQL* para programar a :blue[limpeza e tratamento] dos dados.''')
        st.write('''- :blue[__Seleção das features__]: 
    - __id_aluno (String):__ idade do aluno;
    - __genero_aluno (String):__ gênero do aluno; 
    - __ano_nasc (Integer):__ ano de nascimento do aluno;
    - __ano_ingresso (Integer):__ ano que o aluno ingresso na ONG Passos Mágicos;
    - __idade_2024 (Integer):__ idade do aluno em 2024;
    - __turma_2024 (String):__ número da turma em 2024;
    - __turma_2023 (String):__ número da turma em 2023;
    - __turma_2022 (String):__ número da turma em 2022;
    - __tipo_instituicao_2024 (String):__ tipo de instituição em 2024, e.g. pública ou particular;
    - __tipo_instituicao_2023 (String):__ tipo de instituição em 2023, e.g. pública ou particular;
    - __tipo_instituicao_2022 (String):__ tipo de instituição em 2022, e.g. pública ou particular;
    - __fase_2024 (String):__ fase em 2024 do nível de aprendizado do aluno; 
    - __fase_2023 (String):__ fase em 2023 do nível de aprendizado do aluno;
    - __fase_2022 (String):__ fase em 2022 do nível de aprendizado do aluno;
    - __pedra_2024 (String):__ Classificação do aluno em 2024 baseado no nº INDE, sendo categorizado em:
        - Quartzo: de 2,405 a 5,506;
        - Ágata: de 5,506 a 6,868;
        - Ametista: de 6,868 a 8,230;
        - Topázio: de 8,230 a 9,294.
    - __pedra_2023 (String):__ Classificação do aluno em 2023 baseado no nº INDE, sendo categorizado em:
        - Quartzo: de 2,405 a 5,506;
        - Ágata: de 5,506 a 6,868;
        - Ametista: de 6,868 a 8,230;
        - Topázio: de 8,230 a 9,294.
    - __pedra_2022 (String):__ Classificação do aluno em 2022 baseado no nº INDE, sendo categorizado em:
        - Quartzo: de 2,405 a 5,506;
        - Ágata: de 5,506 a 6,868;
        - Ametista: de 6,868 a 8,230;
        - Topázio: de 8,230 a 9,294.
    - __pedra_2021 (String):__ Classificação do aluno em 2021 baseado no nº INDE, sendo categorizado em:
        - Quartzo: de 2,405 a 5,506;
        - Ágata: de 5,506 a 6,868;
        - Ametista: de 6,868 a 8,230;
        - Topázio: de 8,230 a 9,294.
    - __pedra_2020 (String):__ Classificação do aluno em 2020 baseado no nº INDE, sendo categorizado em:
        - Quartzo: de 2,405 a 5,506;
        - Ágata: de 5,506 a 6,868;
        - Ametista: de 6,868 a 8,230;
        - Topázio: de 8,230 a 9,294.
    - __inde_2024 (Float):__ índice do Desenvolvimento Educacional, como a ponderação dos indicadores IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2024;
    - __inde_2023 (Float):__ índice do Desenvolvimento Educacional, como a ponderação dos indicadores IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2023;
    - __inde_2022 (Float):__ índice do Desenvolvimento Educacional, como a ponderação dos indicadores IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2022;

''')
 
    with coluna2:
        st.write('''- :blue[__Seleção das features (continuação)__]: 
    - __vlr_iaa_2024 (Float):__ indicador de Auto Avaliça em 2024;
    - __vlr_iaa_2023 (Float):__ indicador de Auto Avaliça em 2023;
    - __vlr_iaa_2022 (Float):__ indicador de Auto Avaliça em 2022;
    - __vlr_ips_2024 (Float):__ indicador Psicossocial em 2024;
    - __vlr_ips_2023 (Float):__ indicador Psicossocial em 2023;
    - __vlr_ips_2022 (Float):__ indicador Psicossocial em 2022;
    - __vlr_ipp_2024 (Float):__ indicador Psicopedagógico em 2024;
    - __vlr_ipp_2023 (Float):__ indicador Psicopedagógico em 2023;
    - __vlr_ipp_2022 (Integer):__ indicador Psicopedagógico em 2022;
    - __vlr_ieg_2024 (Float):__ indicador de Engajamento em 2024;
    - __vlr_ieg_2023 (Float):__ indicador de Engajamento em 2023;
    - __vlr_ieg_2022 (Float):__ indicador de Engajamento em 2022;
    - __vlr_ida_2024 (Float):__ indicador de Aprendizagem em 2024;
    - __vlr_ida_2023 (Float):__ indicador de Aprendizagem em 2023;
    - __vlr_ida_2022 (Float):__ indicador de Aprendizagem em 2022;
    - __vlr_ipv_2024 (Float):__ indicador de ponto de virada em 2024;
    - __vlr_ipv_2023 (Float):__ indicador de ponto de virada em 2023;
    - __vlr_ipv_2022 (Float):__ indicador de ponto de virada em 2022;
    - __vlr_ian_2024 (Float):__ indicador de adequação ao nível em 2024;
    - __vlr_ian_2023 (Float):__ indicador de adequação ao nível em 2023;
    - __vlr_ian_2022 (Float):__ indicador de adequação ao nível em 2022;
    - __fase_ideal_2024 (String):__ fase ideal do aluno em 2024;
    - __fase_ideal_2023 (String):__ fase ideal do aluno em 2023;
    - __fase_ideal_2022 (String):__ fase ideal do aluno em 2022;
    - __defasagem_2024 (Integer):__ nível de defasagem em 2024;
    - __defasagem_2023 (Integer):__ nível de defasagem em 2023;
    - __defasagem_2022 (Integer):__ nível de defasagem em 2022;
    - __nome_instituicao_2024 (String):__ nome da instituição do aluno em 2024;
    - __status_aluno_2024 (String):__ status do aluno em 2024, e.g. se o aluno está ativo ou se saiu da escola;
''')
        st.info(''' __3. Dashboard__''')
        st.write('''- :blue[__Integração da base de dados:__] Foi utilizado o :blue[Looker] para consumo dos dados tratados no BigQuery e assim elaboração do Dashboard e criação dos indicadores.''')
        st.write('''- :blue[__Elaboração do Dashboard:__] Com o :blue[Looker] enfocou-se na criação de avaliaões por Tipos de instituições de ensino de cada aluno, média do desempenho acadêmico dos alunos e avaliação das notas por perfis de aluno.''')



with aba2:
    st.write('''#### Passo-a-passo para deploy''')
    coluna1, coluna2 = st.columns(2)
    with coluna1:
       #st.write('''###### Localmente''')
        #st.info(''' :blue[__1. Desenvolver um script para subir no Streamlit__]: ''')
        st.info(''' ##### Localmente
:gray-background[__1. Desenvolver um script para subir no Streamlit__]
- Via VS Code desenvolver o script a ser disponibilizado no Streamlit
                
:gray-background[__2. Criação do espaço virtual no VS Code__]
- Com o terminal do VS Code aberto, rodar o seguinte comando:
                
        python -m venv venv

:gray-background[__3. Ativação da pasta “Scripts”__]
                
- Ainda no terminal do VS Code aberto, rodar os seguintes comandos:
                  
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
        
-  E em seguida, rodar:
                
        venv\Scripts\ activate

:gray-background[__4. Inicializando o Streamlit__]
- E por fim, rodar o comando:
                
        streamlit run arquivo_script.py''')
    with coluna2:
        st.success('''##### Produção (deploy)
:gray-background[__1. Desenvolver um script para subir no Streamlit__]
- Via VS Code desenvolver o script a ser disponibilizado no Streamlit

:gray-background[__2. Versione o código com Git (via GitHub)__]

Fazer o upload no GitHub do:
- Script.py;
- Arquivo "requirements.txt"
    - Com o nome das bibliotecas e suas respectivas versões a serem executadas em produção.
                   
E se aplicável ao projeto, fazer o upload no GitHub da:
- Pasta "pages":
    - Para armazenar as diferentes páginas do projeto.
- Pasta ".streamlit":
    - Com o arquivo config.toml, que contem as configurações do design das páginas.
                   
:gray-background[__3. Configurar e executar o ambiente de Deploy (Streamlit)__]:
- Entrar no site do Streamlit Cloud "https://streamlit.io/"
- Conectar via opção "Continue with GitHub";
- Selecionar o repositório e o script.py;
- Configurar versão do python e nome da página ainda na interface do Streamlit.''')
