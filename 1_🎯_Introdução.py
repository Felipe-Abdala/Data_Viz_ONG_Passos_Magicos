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

# Página
st.title('Análise relatórios ONG Passos Mágicos')
st.markdown(' Pós-Tech FIAP Data Analytics | :blue[Datathon] | Grupo 59')

#st.caption("O mercado de petróleo e seus derivados traz consigo voluptuosas cifras e com enfoque em sua :blue[_produção_] e :blue[_comercialização_] que o presente trabalho se debruça.")

## Visualização no Streamlit
aba1, aba2 = st.tabs(['Introdução','Objetivos'])
with aba1:
	coluna1, coluna2 = st.columns(2)
	with coluna1:
		st.write('''#### Contextualização''')
		st.write(''' A associação :blue[__Passos Mágicos__] iniciou os seus trabalhos de apoio via educação à __crianças__ e __jovens de baixa renda__, na cidade de __Embu-Guaçu__ (no estado de São Paulo).''')
		st.write(''' O modelo de impacto social trazido pela ONG é viabilizado por meio de:
- :blue[Aceleração de conhecimento] (e.g. programas educacionais, assistência psicológica);
- :blue[Programas especiais] (e.g. apadrinhamento e intercâmbio);
- :blue[Eventos e Ações Sociais];
- :blue[Parceiros e Apoiadores.]''')

	with coluna2:
		st.write('''''')
		st.image("https://niverdobem.com.br/wp-content/uploads/2020/10/18A3D82B-2FDB-4355-A9D1-FBAA99E56F41.jpeg", caption="Logo Passos Mágicos. | Imagem disponível em: vide bibliografia")


with aba2:
	st.write('''#### Objetivos do estudo''')
	coluna1, coluna2 = st.columns(2)
	with coluna1:
		st.write('''- Analisar os dados dos relatórios da ONG Passos Mágicos sob uma ótica de :blue[análise exploratória e descrita] para demonstrar o :blue[impacto] que ela tem sobre a comunidade que atende;''')
		st.write('''- Avaliar por :blue[segmentos] dentro da população estudantil estudada quais :blue[comportamentos mais predominam], sejam eles de predomínio de notas, evasão e outros comportamentos;''')
		st.write('''- Criar um :blue[dashboard interativo], a partir dos dados oriundos de um excel que compila as informações dos Relatórios anuais da ONG, a fim de gerar :blue[*insights*] sobre a o comportamento de evasão, notas, métricas psicoeducacionais por cada aluno, durante os anos de análise;''')
		st.write('''- Criar um :blue[plano para fazer o deploy] com o Dashboard integrado;''')
		st.write('''- :blue[Disponibilizar via Streamlit] a análise exploratória e descritiva dos dados.''')

	with coluna2:
		st.image("https://passosmagicos.com.br/wp-content/uploads/2021/04/Design-sem-nome-5.png", caption = "Relatórios ONG Passos Mágicos. | Imagem disponível em: vide bibliografia ")
