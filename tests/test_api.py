import json
import pytest
from library.api_client import APIClient
from library.response_validator import ResponseValidator
from utils.logging import get_logger

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

logger = get_logger()

def load_test_data():
    with open("data/test_data.json") as f:
        return json.load(f)

# TC001 - Get all posts
def test_get_all_posts(session):
    logger.info("TC001 - Get all posts started")
    client = APIClient(session)
    response = client.get_all_posts()
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)
    ResponseValidator.verify_json_length(response, 100)

# TC002 - Get post by id(1)
def test_get_post_by_id_1(session):
    logger.info("TC002 - Get post by id(1)")
    client = APIClient(session)
    response = client.get_post_by_id(1)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)
    ResponseValidator.verify_json_value(response, "id", 1)
    ResponseValidator.verify_json_value(response, "id", 1)
    ResponseValidator.compare_two_json(
        response.json(),
        {"id": 1}
    )
# TC003 - Get post by id(35)
def test_get_post_by_id_35(session):
    logger.info("TC003 - Get post by id(35)")
    client = APIClient(session)
    response = client.get_post_by_id(35)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)
    ResponseValidator.verify_json_value(response, "id", 35)

# TC004 - Create Post
@pytest.mark.parametrize("post_data", load_test_data()["create_post_valid"])
def test_create_post(session, post_data):
    logger.info("TC004 - Create Post")
    client = APIClient(session)
    response = client.create_post(post_data)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 201)
    ResponseValidator.verify_json_value(response, "title", post_data["title"])
    ResponseValidator.verify_json_value(response, "title", post_data["title"])
    ResponseValidator.compare_two_json(
        response.json(),
        {"title": post_data["title"]}
    )

# TC005 - Update post(1)
def test_update_post_1(session):
    logger.info("TC005 - Update post(1)")
    client = APIClient(session)
    data = load_test_data()["update_post_1"]
    response = client.update_post(1, data)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)
    ResponseValidator.verify_json_value(response, "title", data["title"])

# TC006 - Update post(25)
def test_update_post_25(session):
    logger.info("TC006 - Update post(25)")
    client = APIClient(session)
    data = load_test_data()["update_post_25"]
    response = client.update_post(25, data)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)
    ResponseValidator.verify_json_value(response, "title", data["title"])
    ResponseValidator.verify_json_value(response, "body", data["body"])
    ResponseValidator.verify_json_value(response, "title", data["title"])
    ResponseValidator.verify_json_value(response, "body", data["body"])
    ResponseValidator.compare_two_json(
        response.json(),
        {
            "title": data["title"],
            "body": data["body"]
        }
    )

# TC007 - Delete post(2)
def test_delete_post(session):
    logger.info("TC007 - Delete post(2)")
    client = APIClient(session)
    response = client.delete_post(2)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)

# TC008 - Delete multiple posts
@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_delete_multiple_posts(session, post_id):
    logger.info(f"TC008 - Delete post({post_id})")
    client = APIClient(session)
    response = client.delete_post(post_id)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)

# TC009 - Get non-existent post
def test_get_non_existent_post(session):
    logger.info("TC009 - Get non-existent post")
    client = APIClient(session)
    response = client.get_post_by_id(9945)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 404)

# TC010 - Create invalid post
def test_create_post_invalid_data(session):
    logger.info("TC010 - Create invalid post")
    client = APIClient(session)
    data = load_test_data()["invalid_post"]
    response = client.create_post(data)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 201)

# TC011 - Get all users
def test_get_all_users(session):
    logger.info("TC011 - Get all users")
    client = APIClient(session)
    response = client.get_all_users()
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)

# TC012 - Validate user structure
def test_user_structure(session):
    logger.info("TC012 - Validate user structure")
    client = APIClient(session)
    response = client.get_all_users()
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)
    user = response.json()[0]
    assert "id" in user
    assert "name" in user
    assert "username" in user
    assert "email" in user

# TC013 - Get all comments
def test_get_all_comments(session):
    logger.info("TC013 - Get all comments")
    client = APIClient(session)
    response = client.get_all_comments()
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)
    assert len(response.json()) > 0

# TC014 - Get post comments
def test_get_post_comments(session):
    logger.info("TC014 - Get post comments")
    client = APIClient(session)
    response = client.get_post_comments(1)
    logger.info(f"Status Code: {response.status_code}")
    ResponseValidator.verify_status_code(response, 200)
    assert len(response.json()) > 0