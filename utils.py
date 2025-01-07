"""
utils.py

Archivo de utilidades para interactuar con Ollama.
"""

import requests

def generate_response(prompt, model_name="phi"):
    """Genera una respuesta simple usando Ollama"""
    try:
        formatted_prompt = f"""Solo responde en español.
Pregunta: {prompt}
Respuesta:"""
        
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': model_name,
                'prompt': formatted_prompt,
                'stream': False,
                'options': {
                    'temperature': 0.1,  # Temperatura más baja para respuestas más precisas
                    'stop': ['User:', 'Assistant:', '(', 'Question:']
                }
            }
        )
        
        if response.status_code == 200:
            respuesta = response.json().get('response', '').strip()
            print(f"[DEBUG] Respuesta del modelo: {respuesta}")
            
            # Verificar si la respuesta es válida
            if not respuesta or 'User:' in respuesta or 'Assistant:' in respuesta:
                return "Lo siento, intenta hacer la pregunta de otra forma."
            return respuesta
            
        return "Error al generar la respuesta."
    except Exception as e:
        print(f"[ERROR] {e}")
        return "Error al conectar con el modelo."
