from fastapi import Depends
from sqlalchemy.orm import Session

from app.tracker.user.data.repositories.user_repository import UserRepositoryImpl
from app.tracker.user.data.repositories.user_unit_of_work import (
    UserUnitOfWorkImpl,
)
from app.tracker.user.data.services.user_query_service import UserQueryServiceImpl
from app.tracker.user.domain.repositories.user_repository import UserRepository
from app.tracker.user.domain.repositories.user_unit_of_work import UserUnitOfWork
from app.tracker.user.domain.services.user_query_service import UserQueryService
from app.tracker.user.domain.usecases.create_user import (
    CreateUserUseCase,
    CreateUserUseCaseImpl,
)
from app.tracker.user.domain.usecases.delete_user import (
    DeleteUserUseCase,
    DeleteUserUseCaseImpl,
)
from app.tracker.user.domain.usecases.get_user import (
    GetUserUseCase,
    GetUserUseCaseImpl,
)
from app.tracker.user.domain.usecases.get_users import (
    GetUsersUseCaseImpl,
    GetUsersUseCase,
)
from app.tracker.user.domain.usecases.update_user import (
    UpdateUserUseCase,
    UpdateUserUseCaseImpl,
)
from app.core.database.database import get_sessions


def get_user_query_service(
    session: Session = Depends(get_sessions),
) -> UserQueryService:
    return UserQueryServiceImpl(session)


def get_user_repository(session: Session = Depends(get_sessions)) -> UserRepository:
    return UserRepositoryImpl(session)


def get_user_unit_of_work(
    session: Session = Depends(get_sessions),
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserUnitOfWork:
    return UserUnitOfWorkImpl(session, user_repository)


def get_delete_user_use_case(
    unit_of_work: UserUnitOfWork = Depends(get_user_unit_of_work),
) -> DeleteUserUseCase:
    return DeleteUserUseCaseImpl(unit_of_work)


def get_user_use_case(
    user_query_service: UserQueryService = Depends(get_user_query_service),
) -> GetUserUseCase:
    return GetUserUseCaseImpl(user_query_service)


def get_users_use_case(
    user_query_service: UserQueryService = Depends(get_user_query_service),
) -> GetUsersUseCase:
    return GetUsersUseCaseImpl(user_query_service)


def get_create_user_use_case(
    unit_of_work: UserUnitOfWork = Depends(get_user_unit_of_work),
) -> CreateUserUseCase:
    return CreateUserUseCaseImpl(unit_of_work)


def get_update_user_use_case(
    unit_of_work: UserUnitOfWork = Depends(get_user_unit_of_work),
) -> UpdateUserUseCase:
    return UpdateUserUseCaseImpl(unit_of_work)
