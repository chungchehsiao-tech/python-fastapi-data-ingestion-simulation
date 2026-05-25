from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the application
app = FastAPI(title = "Data Ingestion API")

# -- data validation tool --
# the descriptions and the data type from our client
class ClientData(BaseModel):
    user_id: int
    data_payload: str

# -- Endpoint 1: GET (system health check) --
@app.get("/ping")
def health_check():
    return{
        "status": "online",
        "message": "Data Ingestion API is runniing securely!"
    }

# -- Endpoint 2: POST (the ingestion route) --
@app.post("/ingest")
def ingest_data(payload: ClientData):
    return{
        "message": "data received and validate",
        "receive_id": payload.user_id,
        "content": payload.data_payload
    }