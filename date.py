import datetime
import os
from dotenv import load_dotenv
import streamlit as st

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a senha e a palavra secreta do arquivo .env
senha = os.getenv("SENHA")
segredo = os.getenv("SEGREDO")

# Lista de dicas muito discretas
dicas = [
    "Dica 1: A jornada começa com algo aparentemente simples.",
    "Dica 2: Há uma relação importante entre diferentes pontos de vista.",
    "Dica 3: O ambiente pode ser mais impactante do que se imagina.",
    "Dica 4: Uma transformação significativa acontece ao longo do caminho.",
    "Dica 5: Algo que parece impossível, na verdade, é muito possível.",
    "Dica 6: Pequenos detalhes podem mudar o curso de tudo.",
    "Dica 7: Um momento decisivo envolve decisões difíceis.",
    "Dica 8: Às vezes, a melhor maneira de viajar é sem sair do lugar.",
    "Dica 10: O grande momento chegou!"
]

# Função para exibir a dica do dia
def exibir_dica():
    hoje = datetime.datetime.now()
    dia_10_janeiro = datetime.datetime(hoje.year, 1, 10)
    
    if hoje <= dia_10_janeiro:
        dias_ate_surpresa = (hoje - datetime.datetime(hoje.year, 1, 1)).days
        if dias_ate_surpresa < len(dicas):
            return dicas[dias_ate_surpresa]
        else:
            return "O grande momento chegou!"
    else:
        return "A data já passou!"

# Configuração do Streamlit
st.title("✨ Date Surpresa ✨")
st.write("Descubra uma dica por dia até o grande momento!")

# Mostra a dica do dia
dica_atual = exibir_dica()
st.subheader("Dica do Dia")
st.write(dica_atual)

# Se for o dia final, permite revelar o segredo com a senha
if dica_atual == "O grande momento chegou!":
    st.subheader("A revelação final!")
    senha_informada = st.text_input("Digite a senha para revelar o segredo:", type="password")
    
    if senha_informada == senha:
        st.markdown(f'<h1 style="color: purple; text-align: center;">{segredo}</h1>', unsafe_allow_html=True)
        st.balloons()  # Efeito de confetes
    elif senha_informada:
        st.error("Senha incorreta. Tente novamente!")
