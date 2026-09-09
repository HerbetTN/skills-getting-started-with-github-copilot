from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity_name}"

    activity = client.get("/activities").json()[activity_name]
    assert email not in activity["participants"]


def test_unregister_participant_not_found_returns_404():
    activity_name = "Chess Club"
    email = "missing@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    assert response.status_code == 404
