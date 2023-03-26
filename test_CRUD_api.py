import logging
import pytest
import requests
from utilities.customLogger import CustLogger


ENDPOINT = "http://localhost:3000"

class Test_API:
    logger = CustLogger.custLogger(loglevel=logging.INFO)
    @pytest.mark.sanity
    def test_can_call_endpoint(self):
        self.logger.info("Checking if the endpoint is working or not")
        response = requests.get(ENDPOINT)
        assert response.status_code == 200
        self.logger.info(f"Response code post starting the server : {response.status_code}")

    @pytest.mark.smoke
    def test_can_create_user(self):
        # Create a User
        self.logger.info("Creating a new user")
        payload = self.new_user_payload()
        create_user_response = self.create_user(payload)
        assert create_user_response.status_code == 201
        self.logger.info(f"Response of create user api : {create_user_response.status_code}")
        data = create_user_response.json()

        # Get and Validate the user
        user_id = data["id"]
        get_user_response = self.get_user(user_id)

        self.logger.info("Validating the user details created via get api ...")
        assert get_user_response.status_code == 200
        get_user_data = get_user_response.json()
        assert get_user_data["first_name"] == payload["first_name"]
        assert get_user_data["last_name"] == payload["last_name"]
        assert get_user_data["expertiseIn"] == payload["expertiseIn"]
        self.logger.info("User details verified successfully")

    @pytest.mark.regression
    def test_can_update_task(self):
        # creating a user
        payload = self.new_user_payload()
        self.logger.info("Creating a new user...")
        create_user_response = self.create_user(payload)
        assert create_user_response.status_code == 201
        self.logger.info(f"Status code of the create user api : {create_user_response.status_code}")
        user_id = create_user_response.json()["id"]

        # update the user details
        self.logger.info("updating the user details via PATCH api...")
        updated_user_payload = {
            "last_name": "Kumar",
            "expertiseIn": "None"
        }
        update_user_response = self.update_user(user_id, updated_user_payload)
        update_user_data = update_user_response.json()
        assert update_user_response.status_code == 200
        self.logger.info(f"Response of the update api : {update_user_response.status_code}")

        # get and validate the changes
        self.logger.info("Validating the changes made to the user details...")
        get_user_response = self.get_user(user_id)
        assert get_user_response.status_code == 200
        get_user_data = self.get_user(user_id).json()
        assert get_user_data["last_name"] == update_user_data["last_name"]
        assert get_user_data["expertiseIn"] == update_user_data["expertiseIn"]
        self.logger.info("User details verified successfully post updating")

    @pytest.mark.regression
    def test_can_delete_user(self):
        # Create user
        self.logger.info("Creating a user")
        payload = self.new_user_payload()
        create_user_response = self.create_user(payload)
        assert create_user_response.status_code == 201
        self.logger.info("User Created Successfully")
        data = create_user_response.json()

        # Get User
        user_id = data["id"]
        get_user_response = self.get_user(user_id)
        assert get_user_response.status_code == 200
        self.logger.info(f"Getting the details of the created user via GET api, response : {get_user_response.status_code}")

        # Delete User
        self.logger.info("Deleting the user...")
        delete_user_response = self.delete_user(user_id)
        assert delete_user_response.status_code == 200
        self.logger.info("User deleted successfully...")


    def create_user(self,payload):
        return requests.post(ENDPOINT + "/users", json=payload)

    def get_user(self,user_id):
        return requests.get(ENDPOINT + f"/users/{user_id}")

    def new_user_payload(self):
        return {
            "first_name": "Ritesh",
            "last_name": "Singh",
            "expertiseIn": "Ruby"
        }

    def update_user(self, user_id, updated_user_payload):
        return requests.patch(ENDPOINT + f"/users/{user_id}", json=updated_user_payload)

    def delete_user(self, user_id):
        return requests.delete(ENDPOINT + f"/users/{user_id}")




