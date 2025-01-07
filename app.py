"""
app.py

Aplicación principal de Streamlit para el chatbot con Ollama.
"""

import streamlit as st
from utils import generate_response

# Configuración de la página
st.set_page_config(page_title="Chat AI", page_icon="💬")

# Estilo CSS personalizado
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
</style>
""", unsafe_allow_html=True)

st.markdown("# 💬 Chat AI")
st.markdown("---")

# Inicializar el historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input del usuario
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

# Botón para limpiar chat
if st.sidebar.button("Limpiar Chat"):
    st.session_state.messages = []
    st.rerun()
