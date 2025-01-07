"""
utils.py

Archivo de utilidades para interactuar con Ollama.
"""

import requests
import json

def load_model(model_name="phi"):
    """
    Verifica que el modelo esté disponible en Ollama.
    """
    # Ollama maneja los modelos automáticamente
    return model_name

def generate_response(prompt, model_name, max_length=150):
    """
    Genera una respuesta usando Ollama API.
    """
    # Preparar el prompt
    input_text = (
        "Instrucción: Actúa como un asistente virtual amable y útil. "
        "Responde siempre en español de manera clara y precisa.\n\n"
        "Usuario: " + prompt + "\n"
        "Asistente:"
    )
    
    # Llamada a la API de Ollama
    response = requests.post('http://localhost:11434/api/generate',
        json={
            'model': model_name,
            'prompt': input_text,
            'stream': False,
            'options': {
                'temperature': 0.7,
                'top_p': 0.95,
                'top_k': 40,
            }
        })
    
    if response.status_code == 200:
        return response.json()['response'].strip()
    else:
        return "Lo siento, hubo un error al generar la respuesta."
