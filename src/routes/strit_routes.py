import uuid

from fastapi import APIRouter

from props.strit_service_props import StritCreateProps, StritObject, StritUpdateProps
from services.strit_service import StritService

router = APIRouter(prefix="/strit", tags=["strit"])


@router.post("/")
def create_strit_api(strit_data: StritCreateProps) -> StritObject:
    return StritService.create_strit(strit_data=strit_data)


@router.get("/")
def list_strit_api() -> list[StritObject]:
    return StritService.list_strit()


@router.get("/{strit_id}")
def get_strit_api(strit_id: uuid.UUID) -> StritObject:
    return StritService.get_strit(strit_id=strit_id)


@router.put("/{strit_id}")
def update_strit_api(strit_id: uuid.UUID, strit_data: StritUpdateProps) -> StritObject:
    return StritService.update_strit(strit_id=strit_id, strit_data=strit_data)
