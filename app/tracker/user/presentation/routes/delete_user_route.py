from fastapi import Depends, HTTPException, status

from app.core.error.user_exception import UserNotFoundError
from app.tracker.user.dependencies import get_delete_user_use_case
from app.tracker.user.domain.entities.user_query import UserReadModel
from app.tracker.user.domain.usecases.delete_user import DeleteUserUseCase
from app.tracker.user.presentation.routes import router
from app.tracker.user.presentation.schemas.user_error_message import (
    ErrorMessageUserNotFound,
)


@router.delete(
    "/{id_}/",
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageUserNotFound}},
)
def delete_user(
    id_: int,
    delete_user_use_case: DeleteUserUseCase = Depends(get_delete_user_use_case),
):
    try:
        user = delete_user_use_case((id_,))
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return user
