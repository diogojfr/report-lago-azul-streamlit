import os

import streamlit as st
from dotenv import load_dotenv

# ── Authentication ───────────────────────────────────────────────────────
load_dotenv()


def _get_app_password():
    """Senha vem do st.secrets (Streamlit Cloud) ou do .env/variável de ambiente (local)."""
    try:
        if "APP_PASSWORD" in st.secrets:
            return st.secrets["APP_PASSWORD"]
    except Exception:
        # Nenhum arquivo de secrets configurado (ex.: rodando localmente)
        pass
    return os.getenv("APP_PASSWORD")


APP_PASSWORD = _get_app_password()

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Acesso Restrito")
    password = st.text_input("Digite a senha", type="password")
    if st.button("Entrar"):
        if APP_PASSWORD and password == APP_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Senha incorreta")
    st.stop()

# ── Main App ─────────────────────────────────────────────────────────────
def _logo_path():
    """Logo com as tintas clareadas no tema dark (o azul da marca fica ilegivel la).

    O config.toml vem primeiro: quando ele fixa um `base`, esse e o tema que o
    usuario ve. st.context.theme.type reflete a preferencia do browser, que
    diverge do tema aplicado justamente quando o config forca um base.
    """
    theme = st.get_option("theme.base")
    if theme not in ("light", "dark"):
        try:
            theme = st.context.theme.type
        except Exception:
            # versoes antigas do Streamlit nao expoem st.context.theme
            theme = "light"
    return "logo-lago-azul-dark.png" if theme == "dark" else "logo-lago-azul.png"


st.image(_logo_path(), width=340)

st.set_page_config(
    page_title="Easy Pallet – Lago Azul Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)


image_url_sidebar = "https://easypallet.com.br/assets/imgs/logos/logo_easypallet.png"
st.sidebar.image(image_url_sidebar, caption=' ', width=250)



# define navigation pages explicitly
pages = [
    st.Page("pages/painel_geral.py", title="📊  Painel Geral"),
    st.Page("pages/painel_montagem.py", title="🔧  Painel Montagem"),
    st.Page("pages/painel_conferencia.py", title="✅  Painel Conferência"),
    st.Page("pages/painel_erros.py", title="⚠️  Painel Erros"),
    st.Page("pages/painel_operacoes.py", title="⏱️  Painel Operações"),
]

current = st.navigation(pages)
current.run()

