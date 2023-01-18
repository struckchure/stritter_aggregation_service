import uuid

from fastapi import HTTPException

from config import env
from config.api_client import APIClient
from props.strit_service_props import StritCreateProps, StritObject, StritUpdateProps
from services.auth_service import AuthService

strit_api = APIClient(base_url=env.STRIT_SERVICE_URL)


class StritService:
    @staticmethod
    def create_strit(strit_data: StritCreateProps) -> StritObject:
        try:
            strit_create_request = strit_api.post(
                "/api/v1/strit/", data=strit_data.json(exclude_none=True)
            )
            user = AuthService.get_users(strit_create_request.json()["user_id"])

            return StritObject(user=user[0], body=strit_create_request.json()["body"])
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def list_strit() -> list[StritObject]:
        try:
            list_strit_request = strit_api.get("/api/v1/strit/")
            user_details_list = AuthService.get_users(
                *list(map(lambda x: x["user_id"], list_strit_request.json()))
            )

            return [
                StritObject(**{**strit, "user": user})  # type: ignore
                for strit, user in zip(list_strit_request.json(), user_details_list)
            ]
        except Exception as e:
            raise e
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_strit(strit_id: uuid.UUID) -> StritObject:
        try:
            get_strit_request = strit_api.get(f"/api/v1/strit/{strit_id}").json()
            user_details = AuthService.get_users(get_strit_request["user_id"])[0]

            return StritObject(
                **{**get_strit_request, "user": user_details}  # type: ignore
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_strit(strit_id: uuid.UUID, strit_data: StritUpdateProps) -> StritObject:
        try:
            update_strit_request = strit_api.put(
                f"/api/v1/strit/{strit_id}", data=strit_data.json(exclude_none=True)
            ).json()
            user_details = AuthService.get_users(update_strit_request["user_id"])[0]

            return StritObject(
                **{**update_strit_request, "user": user_details}  # type: ignore
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
