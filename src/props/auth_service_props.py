import pydantic

from config.utils import BaseObject


class UserObject(BaseObject, total=False):

    first_name: pydantic.constr(min_length=2)  # type: ignore
    last_name: pydantic.constr(min_length=2)  # type: ignore
    username: pydantic.constr(min_length=2, to_lower=True)  # type: ignore
    email: pydantic.constr(min_length=6)  # type: ignore
