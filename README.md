# Entorno
Crea una carpeta para el entorno y descarga las dependencias listadas en `requirements.txt`.

# Variables de entorno
Crea un archivo llamado `.env` y coloca las siguientes variables:

```.env
AccountSID=Sid_twilio
AuthToken=Token_twilio
FROM_PHONE=Numero_twilio
GEMINI_API_KEY=Token_gemini
```

# Versión de Python
Usa Python 3.13.0.

# Cómo ejecutar
1. **Entorno local**:
   Usa Ngrok para crear un túnel y poder usar la API en un entorno local.

2. **Configurar Twilio**:
   Regístrate en Twilio y en "Sandbox settings" coloca la URL que te da Ngrok seguida de `/api/v1/webhook` para redirigir las solicitudes a nuestra API.

3. **Ejecutar el programa**:
   Como se usa FastAPI, ejecuta el servidor con Uvicorn:
   ```sh
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

Después de ejecutar todo, escribe al número que te da Twilio y la API comenzará a funcionar.