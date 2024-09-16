from typing import cast
from abc import abstractmethod

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.user_exception import UserAlreadyExistsError
from app.tracker.user.domain.entities.user_entity import UserEntity
from app.tracker.user.domain.entities.user_query import UserReadModel
from app.tracker.user.domain.repositories.user_unit_of_work import UserUnitOfWork


class CreateUserUseCase(BaseUseCase):
    unit_of_work: UserUnitOfWork

    @abstractmethod
    def __call__(self, *args):
        raise NotImplementedError


class CreateUserUseCaseImpl(CreateUserUseCase):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args) -> UserReadModel:
        (data,) = args

        user = UserEntity(
            id=None,
            **data.dict(),
        )

        existing_user = self.unit_of_work.repository.find_by_email(email=user.email)
        if existing_user is not None:
            raise UserAlreadyExistsError()

        try:
            self.unit_of_work.repository.create(user)
        except Exception as ex:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        created_user = self.unit_of_work.repository.find_by_email(email=user.email)
        return UserReadModel.from_entity(cast(UserEntity, created_user))
