import logging
import pytest
import requests

ENDPOINT = "http://localhost:3000"


@pytest.mark.sanity
def test_can_call_endpoint():
    logging.info("Checking if the endpoint is working or not")
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    logging.info(f"Response code post starting the server : {response.status_code}")

@pytest.mark.smoke
def test_can_create_user():
    # Create a User
    logging.info("Creating a new user")
    payload = new_user_payload()
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 201
    logging.info(f"Response of create user api : {create_user_response.status_code}")
    data = create_user_response.json()

    # Get and Validate the user
    user_id = data["id"]
    get_user_response = get_user(user_id)

    logging.info("Validating the user details created via get api ...")
    assert get_user_response.status_code == 200
    get_user_data = get_user_response.json()
    assert get_user_data["first_name"] == payload["first_name"]
    assert get_user_data["last_name"] == payload["last_name"]
    assert get_user_data["expertiseIn"] == payload["expertiseIn"]
    logging.info("User details verified successfully")

@pytest.mark.regression
def test_can_update_task():
    # creating a user
    payload = new_user_payload()
    logging.info("Creating a new user...")
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 201
    logging.info(f"Status code of the create user api : {create_user_response.status_code}")
    user_id = create_user_response.json()["id"]

    # update the user details
    logging.info("updating the user details via PATCH api...")
    updated_user_payload = {
        "last_name": "Kumar",
        "expertiseIn": "None"
    }
    update_user_response = update_user(user_id, updated_user_payload)
    update_user_data = update_user_response.json()
    assert update_user_response.status_code == 200
    logging.info(f"Response of the update api : {update_user_response.status_code}")

    # get and validate the changes
    logging.info("Validating the changes made to the user details...")
    get_user_response = get_user(user_id)
    assert get_user_response.status_code == 200
    get_user_data = get_user(user_id).json()
    assert get_user_data["last_name"] == update_user_data["last_name"]
    assert get_user_data["expertiseIn"] == update_user_data["expertiseIn"]
    logging.info("User details verified successfully post updating")

@pytest.mark.regression
def test_can_delete_user():
    # Create user
    logging.info("Creating a user")
    payload = new_user_payload()
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 201
    logging.info("User Created Successfully")
    data = create_user_response.json()

    # Get User
    user_id = data["id"]
    get_user_response = get_user(user_id)
    assert get_user_response.status_code == 200
    logging.info(f"Getting the details of the created user via GET api, response : {get_user_response.status_code}")

    # Delete User
    logging.info("Deleting the user...")
    delete_user_response = delete_user(user_id)
    assert delete_user_response.status_code == 200
    logging.info("User deleted successfully...")


def create_user(payload):
    return requests.post(ENDPOINT + "/users", json=payload)


def get_user(user_id):
    return requests.get(ENDPOINT + f"/users/{user_id}")


def new_user_payload():
    return {
        "first_name": "Ritesh",
        "last_name": "Singh",
        "expertiseIn": "Ruby"
    }


def update_user(user_id, updated_user_payload):
    return requests.patch(ENDPOINT + f"/users/{user_id}", json=updated_user_payload)


def delete_user(user_id):
    return requests.delete(ENDPOINT + f"/users/{user_id}")
