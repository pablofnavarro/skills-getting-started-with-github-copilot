def test_unregister_success_removes_participant(client):
    email = "temporary@mergington.edu"

    signup_response = client.post(f"/activities/Chess%20Club/signup?email={email}")
    assert signup_response.status_code == 200

    delete_response = client.delete(f"/activities/Chess%20Club/signup?email={email}")

    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": f"Unregistered {email} from Chess Club"}

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email not in participants


def test_unregister_non_participant_returns_404(client):
    response = client.delete("/activities/Chess%20Club/signup?email=ghost@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete("/activities/Unknown%20Club/signup?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
