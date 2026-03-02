from utils.logging import get_logger

logger = get_logger()
class ResponseValidator:
    @staticmethod
    def verify_status_code(response, expected_code):
        assert response.status_code == expected_code, \
            f"Expected {expected_code}, got {response.status_code}"
    @staticmethod
    def verify_json_length(response, expected_length):
        assert len(response.json()) == expected_length, \
            f"Expected length {expected_length}, got {len(response.json())}"
    @staticmethod
    def verify_json_value(response, key, expected_value):
        assert response.json()[key] == expected_value, \
            f"Expected {expected_value}, got {response.json()[key]}"
    @staticmethod
    def verify_key_present(response, key):
        assert key in response.json(), f"{key} not found in response"
    @staticmethod
    def compare_two_json(json1, json2):
        differences = {}
        for key in json1:
            if key not in json2:
                differences[key] = "Missing in second JSON"
            elif json1[key] != json2[key]:
                differences[key] = {
                    "json1": json1[key],
                    "json2": json2[key]
                }
        for key in json2:
            if key not in json1:
                differences[key] = "Missing in first JSON"
        if differences:
            logger.info(f"JSON differences found: {differences}")
        else:
            logger.info("No JSON differences found")
        return differences