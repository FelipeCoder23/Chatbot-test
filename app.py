"""
app.py

Aplicación principal de Streamlit para el chatbot.
"""

import streamlit as st
from utils import load_model, generate_response

# 1. Configuración de la página de Streamlit
st.set_page_config(page_title="Chatbot Open Source", page_icon="💬", layout="centered")

# 2. Título y descripción
st.title("Chatbot Open Source con Streamlit")
st.markdown("Este es un ejemplo de chatbot utilizando un modelo de lenguaje open source.")

# 3. Carga (en caché) del modelo
tokenizer, model = load_model("distilgpt2")  # Puedes cambiar el modelo si deseas uno en español

# 4. Manejo de estado de la conversación
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# 5. Input de usuario
user_input = st.text_input("Escribe tu mensaje aquí:", "")

# 6. Botón de envío
if st.button("Enviar"):
    # Añadimos la entrada del usuario al historial
    st.session_state.conversation_history.append(f"Usuario: {user_input}")

    # Construimos un prompt sencillo a partir del historial
    # (Opcional: concatenar todo el historial, o simplemente usar la última pregunta)
    context = "\n".join(st.session_state.conversation_history) + f"\nBot:"
    
    # Generamos respuesta
    respuesta = generate_response(context, tokenizer, model)

    # Guardamos la respuesta en el historial
    st.session_state.conversation_history.append(f"Bot: {respuesta}")

# 7. Mostrar el historial de conversación
if st.session_state.conversation_history:
    st.write("## Conversación")
    for line in st.session_state.conversation_history:
        if line.startswith("Usuario:"):
            st.markdown(f"**{line}**")
        else:
            st.markdown(line)
