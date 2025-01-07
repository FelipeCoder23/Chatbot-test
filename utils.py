"""
utils.py

Archivo de utilidades para interactuar con Ollama.
"""

import requests

def generate_response(prompt, model_name="phi"):
    """Genera una respuesta simple usando Ollama"""
    try:
        formatted_prompt = f"""Eres un asistente que responde preguntas de conocimiento general.
    Debes responder de forma precisa y directa en español.


Pregunta: {prompt}
Respuesta corta y precisa:"""
        
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': model_name,
                'prompt': formatted_prompt,
                'stream': False,
                'options': {
                    'temperature': 0.3,  # Temperatura más baja para respuestas más consistentes
                    'num_predict': 100,  # Limitar longitud de respuesta
                }
            }
        )
        
        if response.status_code == 200:
            respuesta = response.json().get('response', '').strip()
            # Verificar si la respuesta es muy larga o parece divagar
            if len(respuesta.split()) > 30:
                return "Por favor, haz una pregunta más específica."
            return respuesta
            
        return "Error al generar la respuesta."
    except Exception as e:
        print(f"[ERROR] {e}")
        return "Error al conectar con el modelo."
