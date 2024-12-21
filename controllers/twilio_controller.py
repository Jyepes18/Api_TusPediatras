from fastapi import APIRouter, Request
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse
from services.twilio_service import detectar_saludo, detectar_pregunta_servicios, detectar_pregunta
from models.planes import planes, saludos, solicitudes_servicios

router = APIRouter()

@router.post("/webhook")
async def obtener_mensaje_twilio(request: Request):
    datos_servi = await request.form()
    mensaje_recibido = datos_servi.get("Body", "").strip().lower()
    telefono_remitente = datos_servi.get("From", "")

    print(f"Datos recibidos del webhook: {mensaje_recibido}")
    print(f"Teléfono remitente: {telefono_remitente}")

    respuesta = MessagingResponse()

    palabras = mensaje_recibido.split()
    procesado = False

    for palabra in palabras:
        print(f"Palabra procesada: {palabra}")
        if palabra in saludos:
            respuesta_saludo = await detectar_saludo(mensaje_recibido)
            print(f"Respuesta generada por AI: {respuesta_saludo}")
            respuesta.message(respuesta_saludo)
            procesado = True
            break

        elif palabra in solicitudes_servicios:
            respuesta_servicios = await detectar_pregunta_servicios(mensaje_recibido, planes)
            print(f"Respuesta generada por AI: {respuesta_servicios}")
            respuesta.message(respuesta_servicios)
            procesado = True
            break 
    
    if procesado == False:
        respuesta_pregunta = await detectar_pregunta(mensaje_recibido)
        print(f"Respuesta generada por AI: {respuesta_pregunta}")
        respuesta.message(respuesta_pregunta)

    print(f"Respuesta enviada: {str(respuesta)}")
    return Response(content=str(respuesta), media_type="application/xml")
