import streamlit as st
import streamlit.components.v1 as components
import requests


#Configuração gerais das páginas
st.set_page_config(page_title='Pós-Tech FIAP | Datathon | Grupo 59', page_icon=":chart_with_upwards_trend:", layout= 'wide')
st.header('Modelo interativo e resultados')

# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM 354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Datathon | Grupo 59 | Imagem disponível em: vide bibliografia")


# início - Aba Dashboard
st.info("No Dashboard do Looker, navegue pelas *métricas psicológicas*, *educacionais* e de *desempenho* dos alunos.")
looker_studio_url = "https://lookerstudio.google.com/embed/reporting/8bd13cb3-08c7-4e95-8530-d992440e4f21/page/b8jlE"
components.iframe(looker_studio_url, width=1000, height=600)

# Fim - Aba 2 - Corpo da página
