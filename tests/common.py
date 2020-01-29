"""Define common test utilities."""
import os

TEST_ACCOUNT_ID = "aabbccdd"
TEST_DEVICE_ID = "98765"
TEST_EMAIL_ADDRESS = "email@address.com"
TEST_FIRST_NAME = "Tom"
TEST_LAST_NAME = "Jones"
TEST_LOCATION_ID = "mmnnoopp"
TEST_MAC_ADDRESS = "12:34:56:ab:cd:ef"
TEST_PASSWORD = "password"
TEST_PHONE_NUMBER = "+1 123-456-7890"
TEST_TOKEN = "123abc"
TEST_USER_ID = "12345abcde"


def load_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        return fptr.read()
