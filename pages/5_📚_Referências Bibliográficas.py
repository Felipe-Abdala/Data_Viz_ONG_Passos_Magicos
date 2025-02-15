import streamlit as st
import streamlit.components.v1 as components
import requests


#Configuração gerais das páginas
st.set_page_config(page_title='Pós-Tech FIAP | Datathon | Grupo 59', page_icon=":chart_with_upwards_trend:", layout= 'wide')


# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM 354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Datathon | Grupo 59 | Imagem disponível em: vide bibliografia")
##REVISAR#######################################
# Título Página
st.title('Referências bibliográficas')
st.info('''__Bibliotecas e Ferramentas__''')
st.write('''- BigQuery: Base de dados tratada |  Disponível em: https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1stech-challenge-fase-5!2s03_consumer_pede!3scz_inde_completo | Data de criação: 09/02/2025
- Looker: Dashboard | Disponível em:  | Data de criação: 11/02/2025
- GitHub: repositório com o Dashboard e configurações Streamlit | Disponível em: https://github.com/Felipe-Abdala/PEDE_ONG_Passos_Magicos | Data de criação: 11/02/2025''')
st.write('''''')

st.info('''__Fonte de Dados: Dicionários de dados, base de dados, relatórios anuais__''')
st.write('''- Diretório com dicionário e bases de dados: Disponível em: https://drive.google.com/drive/folders/1Z1j6uzzCOgjB2a6i3Ym1pmJRsasfm7cD | Data de acesso: 05/02/2025
- Base de dados: PEDE 2024 (arquivo bruto), antes de ser tratado no BigQuery | https://docs.google.com/spreadsheets/d/1td91KoeSgXrUrCVOUkLmONG9Go3LVcXpcNEw_XrL2R0/edit?gid=90992733#gid=90992733 | Data de acesso: 05/02/2025''')
st.write('''''')

st.info('''__Fonte de imagens__''')
st.write('''-  Disponível em: https://passosmagicos.org.br/wp-content/uploads/2020/10/Passos-magicos-icon-cor.png | Data de acesso: 10/02/2025
- Disponível em: https://niverdobem.com.br/wp-content/uploads/2020/10/18A3D82B-2FDB-4355-A9D1-FBAA99E56F41.jpeg | Data de acesso: 10/02/2025
- Disponível em: https://passosmagicos.com.br/wp-content/uploads/2021/04/Design-sem-nome-5.png | Data de acesso: 10/02/2025''')
st.write('''''')

st.info('''__Conceitos de Storytelling e boas práticas em uso de gráficos e apresentações__''')
st.write('''- Disponível em: https://www.storytellingwithdata.com/chart-guide | Data de acesso: 10/02/2025''')
