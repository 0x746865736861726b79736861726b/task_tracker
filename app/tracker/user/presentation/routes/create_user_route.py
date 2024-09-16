from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.user_exception import UserAlreadyExistsError
from app.tracker.user.dependencies import get_create_user_use_case
from app.tracker.user.domain.entities.user_model import UserCreateModel
from app.tracker.user.domain.entities.user_query import UserReadModel
from app.tracker.user.domain.usecases.create_user import CreateUserUseCase
from app.tracker.user.presentation.routes import router
from app.tracker.user.presentation.schemas.user_error_message import (
    ErrorMessageUserAlreadyExists,
)


@router.post(
    "/",
    response_model=UserReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_409_CONFLICT: {"model": ErrorMessageUserAlreadyExists}},
)
def create_user(
    data: UserCreateModel,
    response: Response,
    request: Request,
    create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case),
):
    try:
        user = create_user_use_case((data,))
    except UserAlreadyExistsError as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=exception.message
        )
    except Exception as _exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    response.headers["location"] = f"{request.url.path}{user.id}"
    return user
