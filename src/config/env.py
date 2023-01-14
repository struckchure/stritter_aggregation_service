import os
from typing import Any

import dotenv

dotenv.load_dotenv()


def get_var(key: str, default: Any = None) -> int | str:
    try:
        return os.environ[key]
    except KeyError:
        if default:
            return default
        raise Exception("%s not found" % key)


API_PORT: int = int(get_var("API_PORT", 8000))

DEBUG: bool = bool(int(get_var("DEBUG", 1)))
