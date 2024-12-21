import google.generativeai as genai

async def respuesta_gemini(mensaje_recibido, contexto):
    modelo = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = modelo.generate_content(mensaje_recibido + "\n" + contexto)
    return response.text
