from fastapi import FastAPI
from controllers.twilio_controller import router as twilio_router

app = FastAPI()

app.include_router(twilio_router, prefix="/api/v1", tags=["Twilio Webhook"])
