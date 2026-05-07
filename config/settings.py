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

SCREENSHOTS_DIR = ROOT_DIR / "screenshots"
REPORTS_DIR = ROOT_DIR / "reports"
LOGS_DIR = ROOT_DIR / "Logs"

for dir_path in [SCREENSHOTS_DIR, REPORTS_DIR, LOGS_DIR]:
    dir_path.mkdir(exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": LOGS_DIR / "automation.log",
            "formatter": "default",
            "level": "DEBUG"
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO"
        }
    },
    "root": {
        "handlers": ["file", "console"],
        "level": "INFO"
    }
}