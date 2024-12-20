from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def get_items():
    return {
        "items":
            [
                {"title": "Foo", "description": "Bar"}
            ]
    }


@router.get("/latest")
def get_latest_item():
    return {"items": [{"id": "0", "description": "Latest"}]}


@router.get("/{item_id}")
def get_item(item_id: Annotated[int, Path(ge=1, le=1_000_000)]):
    return {"item_id": item_id}