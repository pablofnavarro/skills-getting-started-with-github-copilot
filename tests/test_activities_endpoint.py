def test_get_activities_returns_success(client):
    response = client.get("/activities")

    assert response.status_code == 200


def test_get_activities_contains_expected_keys(client):
    response = client.get("/activities")
    activities = response.json()

    assert "Chess Club" in activities
    assert "Programming Class" in activities
    assert "Gym Class" in activities


def test_get_activities_returns_expected_schema(client):
    response = client.get("/activities")
    activities = response.json()

    for details in activities.values():
        assert set(details.keys()) == {
            "description",
            "schedule",
            "max_participants",
            "participants",
        }
        assert isinstance(details["description"], str)
        assert isinstance(details["schedule"], str)
        assert isinstance(details["max_participants"], int)
        assert isinstance(details["participants"], list)
