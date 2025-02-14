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

# Título Página
st.title('Conclusão')

st.info('As conclusões expostas nessa seção referem-se à execução da análise exploratória e descritiva dos relatórios de desempenho dos alunos da ONG Passos Mágicos, vide página __"Dashboard"__.')
coluna1, coluna2 = st.columns(2)
with coluna1:
    st.info('######  Dentre os principais :blue[__impactos sociais__] trazidos pelo programa a comunidade em seu entorno destacam-se:', icon="✔️")
    st.write('''1. __Aumento no conjunto do desempenho acadêmico, psicossocial e psicopedagógico (INDE):__
    - Embora os indicadores de desempenho acadêmico tenham decaído entre 2022 e 2024, o resultado global envolvendo as áreas acadêmicas, psicossociais e psicopedagógicas totalizaram melhoras nos alunos do programa da ONG Passos Mágicos, o que corrobora com o propósito de trazer impacto social para as diversas vertentes do programa.
             ''')
with coluna2:
    st.warning('######  A partir da avaliação dos pontos a melhorar do programa, conclui-se que:', icon="⚠️")
    st.write('''1. __Dificuldade no desempenho acadêmico:__
    - Durante os anos avaliados, identificou-se que o desempenho escolar, independente do grupo ser de escola pública ou privada, apresentou queda (conforme observado no IDA, que representa o "Indicador de Desempenho Acadêmico"), quando comparados os anos de 2022 com o de 2024.
             ''')
