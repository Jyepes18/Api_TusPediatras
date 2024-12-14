from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
FROM_PHONE = os.getenv("FROM_PHONE")

app = FastAPI()

@app.post("/webhook")
async def webhook_whatsapp(request: Request):
    datos_servi = await request.form()
    mensaje_recibido = datos_servi.get("Body", "").strip().lower()
    telefono_remitente = datos_servi.get("From", "")

    print(f"Datos recibidos del webhook: {mensaje_recibido}")
    print(telefono_remitente)

    respuesta = MessagingResponse()

    try:
        modelo = genai.GenerativeModel("gemini-1.5-flash")
        mensaje_recibido = mensaje_recibido

        response = modelo.generate_content(mensaje_recibido)
        print("Respuesta generada por AI:", response.text)

        respuesta.message(response.text)
    except Exception as e:
        print(f"Error al generar contenido: {e}")
        respuesta.message("Lo siento, hubo un problema al procesar tu mensaje.")

    
    print(f"Respuesta enviada: {str(respuesta)}")

    return Response(content=str(respuesta), media_type="application/xml")