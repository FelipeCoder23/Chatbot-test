"""
app.py

Aplicación principal de Streamlit para el chatbot con Ollama.
"""

import streamlit as st
from utils import generate_response

# Configuración de la página
st.set_page_config(
    page_title="Chat con Phi",
    page_icon="🤖",
    layout="wide"
)

# Sidebar con información y controles
with st.sidebar:
    st.title("🤖 Configuración")
    st.markdown("---")
    
    # Información del chat
    st.markdown("### Información del Modelo")
    st.markdown("""
    Este chatbot utiliza el modelo **Phi** de Microsoft a través de Ollama.
    
    **Características:**
    - Modelo: Phi
    - Proveedor: Microsoft/Ollama
    - Idioma: Español
    - Tipo: Modelo de lenguaje conversacional
    """)
    
    # Contador de mensajes
    if "messages" in st.session_state:
        st.markdown(f"### Mensajes: {len(st.session_state.messages)}")
    
    st.markdown("---")
    
    # Botón de limpiar chat
    if st.button("🗑️ Limpiar Conversación", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Contenedor principal
st.markdown("# 🤖 Chat con Phi")
st.markdown("*Un modelo de lenguaje conversacional de Microsoft*")
st.markdown("---")

# Estilo CSS mejorado
st.markdown("""
<style>
.chat-container {
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}
.user-message {
    background-color: #E3F2FD;
    margin-left: 20%;
    margin-right: 5%;
    border: 1px solid #90CAF9;
    color: #1565C0;
}
.bot-message {
    background-color: #FFFFFF;
    margin-right: 20%;
    margin-left: 5%;
    border: 1px solid #E0E0E0;
    color: #333333;
}
.stChatMessage {
    background-color: rgba(240, 242, 246, 0.5);
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1rem;
}
.stChatInput {
    border-radius: 20px;
    border: 1px solid #E0E0E0;
    padding: 10px 20px;
}
.stButton button {
    border-radius: 20px;
    padding: 5px 20px;
}
</style>
""", unsafe_allow_html=True)

# Inicializar el historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Contenedor para los mensajes con altura máxima y scroll
chat_container = st.container()
with chat_container:
    # Mostrar mensajes anteriores
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Input del usuario (fuera del contenedor para que quede fijo abajo)
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Agregar mensaje del usuario
    st.chat_message("user").write(prompt)
    
    # Obtener respuesta
    response = generate_response(prompt)
    
    # Mostrar respuesta del bot
    with st.chat_message("assistant"):
        st.write(response)
    
    # Guardar la conversación
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})
