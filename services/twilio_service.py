from services.google_service import respuesta_gemini
from models.planes import preguntas_frecuentes

def planes_formateados(planes):
    texto_formateado = ""
    for plan, detalles in planes.items():
        texto_formateado += f"Plan: {plan}\n"
        for key, value in detalles.items():
            texto_formateado += f"  {key}: {value}\n"
    return texto_formateado

async def detectar_saludo(mensaje_recibido):
    contexto = ("Si detectas un saludo, responde de manera habitual añadiendo "
                "'Bienvenido a TusPediatras'.")
    return await respuesta_gemini(mensaje_recibido, contexto)

async def detectar_pregunta_servicios(mensaje_recibido, planes):
    planes_formateado = planes_formateados(planes)
    contexto = (
        "Si el mensaje recibido hace referencia a una solicitud de servicio o plan, o cualquier cosa relacionada "
        "con prestaciones de servicios, responde normal orientado al negocio TusPediatras y usando estos planes:\n"
        f"{planes_formateado}"
        ""
    )
    return await respuesta_gemini(mensaje_recibido, contexto)

async def detectar_pregunta(mensaje_recibido):
    contexto = (
    f"Si el mensaje recibido tiene alguna similitud, sinergia o se relaciona con las siguientes preguntas frecuentes: {preguntas_frecuentes}, "
    "responde de manera profesional como si fueras un pediatra, ofreciendo una explicación clara y comprensible y de froma muy corta."
    "Y si tiene que consulatar a un pediatra, dile que ya te contanta con una de nuestras pediatras."
    )
    return await respuesta_gemini(mensaje_recibido, contexto)

