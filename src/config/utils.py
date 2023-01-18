import typing
import uuid
from datetime import datetime


class BaseObject(typing.TypedDict, total=False):

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
