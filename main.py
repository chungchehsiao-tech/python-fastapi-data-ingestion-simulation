import os
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

# Initialize the application
app = FastAPI(title = "Data Ingestion API")

# Get the key from the environment (default to None if missing)
API_KEY = os.getenv("API_KEY");

# -- data validation tool --
# the descriptions and the data type from our client
class ClientData(BaseModel):
    user_id: int
    data_payload: str

# -- Endpoint 1: GET (system health check) --
@app.get("/ping")
def health_check():
    return{
        "status": "active",
        "message": "Data Ingestion API is runniing securely!"
    }

# -- Endpoint 2: POST (the ingestion route) --
@app.post("/ingest")
def ingest_data(payload: ClientData, authorization: str = Header(None)):
    if not API_KEY or authorization != API_KEY:
        raise HTTPException(status_code = 401, detail ="Unauthorized: Invalid or missing API key")
    return{
        "message": "data received and validate",
        "receive_id": payload.user_id,
        "content": payload.data_payload
    }