import typing
import uuid

import pydantic

from config.utils import BaseObject
from props.auth_service_props import UserObject


class StritObject(BaseObject):

    user: UserObject
    body: str


class StritCreateProps(pydantic.BaseModel):

    user_id: uuid.UUID
    body: str


class StritUpdateProps(pydantic.BaseModel):

    body: typing.Optional[str]
