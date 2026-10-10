from pathlib import Path

import streamlit as st
from PIL import Image

# ---------- Configuración de página ----------
st.set_page_config(
    page_title="Interfaces Multimodales · Daniel Flórez",
    page_icon="🌊",
    layout="centered",
)

# ---------- Estilo (paleta fría basada en #3f71a6) ----------
PRIMARIO = "#3f71a6"
OSCURO = "#1b2f45"
CLARO = "#eaf2f9"
SUAVE = "#a9c7e3"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"], .stApp {{
        font-family: 'Inter', sans-serif;
        font-size: 1.08rem;
    }}
    .stApp {{
        background: linear-gradient(180deg, #f6fafd 0%, {CLARO} 100%);
    }}

    /* Columna central más ancha */
    .block-container {{
        max-width: 860px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }}

    /* Hero */
    .hero {{
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }}
    .hero .saludo {{
        color: {PRIMARIO};
        letter-spacing: .25em;
        text-transform: uppercase;
        font-size: .85rem;
        font-weight: 600;
    }}
    .hero h1 {{
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        color: {OSCURO};
        margin: .3rem 0 .6rem 0;
        line-height: 1.1;
    }}
    .hero p {{
        color: #4d6479;
        font-size: 1.2rem;
        max-width: 640px;
        margin: 0 auto;
    }}
    .linea {{
        width: 70px;
        height: 4px;
        border-radius: 4px;
        background: {PRIMARIO};
        margin: 1.4rem auto;
    }}

    /* Títulos de sección */
    h2, h3 {{
        font-family: 'Playfair Display', serif !important;
        color: {OSCURO} !important;
    }}

    /* Tarjetas */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: white;
        border: 1px solid {SUAVE}66 !important;
        border-radius: 18px !important;
        box-shadow: 0 8px 24px rgba(63, 113, 166, .08);
        padding: .6rem .8rem;
    }}

    /* Imagen */
    [data-testid="stImage"] img {{
        border-radius: 20px;
        box-shadow: 0 12px 32px rgba(27, 47, 69, .18);
    }}
    [data-testid="stImageCaption"] {{
        text-align: center;
        color: #6b8399;
        font-style: italic;
    }}

    /* Botones */
    .stButton > button {{
        background: {PRIMARIO};
        color: white;
        border: none;
        border-radius: 999px;
        padding: .7rem 2.2rem;
        font-size: 1.05rem;
        font-weight: 600;
        transition: all .2s ease;
    }}
    .stButton > button:hover {{
        background: {OSCURO};
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(27, 47, 69, .25);
    }}

    /* Inputs */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
        border-radius: 12px;
        border: 1px solid {SUAVE};
        font-size: 1.05rem;
    }}

    /* Mensajes de respuesta */
    [data-testid="stAlert"] {{
        border-radius: 14px;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: {OSCURO};
    }}
    [data-testid="stSidebar"] * {{
        color: #e6f0f9 !important;
    }}

    /* Ocultar menú y pie por defecto */
    #MainMenu, footer {{ visibility: hidden; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar ----------
with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica"),
    )
    st.caption(f"Modalidad activa: **{mod_radio}**")

# ---------- Hero ----------
st.markdown(
    """
    <div class="hero">
        <div class="saludo">Hola, soy</div>
        <h1>Daniel Flórez</h1>
        <p>En este espacio comenzaré a desarrollar mis aplicaciones para
        interfaces multimodales. Puedo trabajar tanto el backend como el frontend.</p>
        <div class="linea"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

try:
    ruta_imagen = Path(__file__).parent / "sergey-kolesov-mermaid-sharpen.jpg"
    image = Image.open(ruta_imagen)
    st.image(image, caption="Interfaces multimodales", use_container_width=True)
except FileNotFoundError:
    st.info("Agrega la imagen 'sergey-kolesov-mermaid-sharpen.jpg' al repositorio para verla aquí.")

st.write("")

# ---------- Texto ----------
with st.container(border=True):
    st.subheader("Tu mensaje")
    texto = st.text_input("Escribe algo", "Este es mi texto")
    st.write(f"El texto escrito es: **{texto}**")

st.write("")

# ---------- Dos columnas ----------
col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("Primera idea")
        st.write("Las interfaces multimodales mejoran la experiencia de usuario.")
        resp = st.checkbox("Estoy de acuerdo")
        if resp:
            st.success("¡Correcto!")

with col2:
    with st.container(border=True):
        st.subheader("Segunda idea")
        modo = st.radio(
            "¿Qué modalidad es la principal en tu interfaz?",
            ("Visual", "Auditiva", "Táctil"),
        )
        mensajes = {
            "Visual": "La vista es fundamental para tu interfaz.",
            "Auditiva": "El audio es fundamental para tu interfaz.",
            "Táctil": "El tacto es fundamental para tu interfaz.",
        }
        st.info(mensajes[modo])

st.write("")

# ---------- Botón ----------
with st.container(border=True):
    st.subheader("Uso de botones")
    if st.button("Presiona el botón"):
        st.success("Gracias por presionar")
    else:
        st.caption("Aún no has presionado el botón.")

st.write("")

# ---------- Selectbox ----------
with st.container(border=True):
    st.subheader("Selectbox")
    in_mod = st.selectbox(
        "Selecciona la modalidad",
        ("Audio", "Visual", "Háptico"),
    )
    acciones = {
        "Audio": "Reproducir audio",
        "Visual": "Reproducir video",
        "Háptico": "Activar vibración",
    }
    st.write(f"La acción es: **{acciones[in_mod]}**")
