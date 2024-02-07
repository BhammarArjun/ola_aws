import pytest #type: ignore
from app import app

@pytest.fixture()
def client():
    return app.test_client()

def test_welcome(client):
    inp_data = {
    "Age": 25,
    "Education_Level": "Graduate",
    "Firstreport_leadtime":56,
    "Grade": 1,
    "Income": 56000,
    "Joining Designation": 1,
    "Quarterly Rating": 1,
    "service_days": 400
        }
    resp = client.post("/predict", json = inp_data)
    assert resp.text == f"CHURN"
    
    