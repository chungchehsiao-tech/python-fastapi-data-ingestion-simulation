import os
from fastapi.testclient import TestClient
from main import app

#create a testing web client to send request to our app
client = TestClient(app)

#create the API_KEY to test
os.environ["API_KEY"] = "good_key"

#Test1: Health Status 200 Check
def test_read_root():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status":"active","message":"Data Ingestion API is running securely!"}

#Test2: unauthorize user without header
def test_ingest_data_unauthorized():
    test_send_data = {"user_id":1,"data_payload":"I'm good guy."}
    response = client.post("/ingest", json = test_send_data)
    assert response.status_code == 401

#Test3: unauthorize user with invalid API key
def test_ingest_data_unauthorized_wrong_key():
    test_send_data = {"user_id":1,"data_payload":"Good things here."}
    test_headers = {"authorization":"not_a_good_key"}
    response = client.post("/ingest", json = test_send_data, headers = test_headers)
    assert response.status_code == 401

#Test4: authorize user with Valid API key
def test_ingest_data_authorized():
    test_send_data =  {"user_id":0, "data_payload":"validTest"}
    test_headers = {"authorization":"good_key"}
    response = client.post("/ingest", json = test_send_data, headers = test_headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["content"] == "validTest"
    assert response_data["receive_id"] == 0
    assert response_data["message"] == "data received and validate"