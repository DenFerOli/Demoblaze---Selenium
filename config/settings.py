import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

BASE_URL = "https://www.demoblaze.com/"
BASE_API_URL = "https://api.demoblaze.com"

DEFAULT_TIMEOUT = 10
INPLICIT_WAIT = 5
PAGE_LOAD_TIMEOUT = 30

HEADLESS_MODE = False
WINDOW_SIZE = "1920,1080"

TEST_USERS = {
    "standard_user": {
        "username": "qa_tester_den",
        "password": "teste123"
    },
    "invalid_user": {
        "username": "wrong_user",
        "password": "wrong_password"
    }
}