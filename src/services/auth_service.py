import uuid

from fastapi import HTTPException

from config import env
from config.api_client import APIClient
from props.auth_service_props import UserObject

api_client = APIClient(base_url=env.AUTH_SERVICE_URL)


class AuthService:
    @staticmethod
    def get_users(*user_id: uuid.UUID) -> list[UserObject]:
        try:
            if user_id:
                get_users_request = api_client.get(
                    "/api/v1/user/", params={"user_ids": user_id}
                )
                return [UserObject(**user) for user in get_users_request.json()]
            return []
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
