from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.user_exception import UserNotFoundError
from app.tracker.user.domain.entities.user_query import UserReadModel
from app.tracker.user.domain.services.user_query_service import UserQueryService


class GetUserUseCase(BaseUseCase[Tuple[int], UserReadModel]):
    service: UserQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> UserReadModel:
        raise NotImplementedError()


class GetUserUseCaseImpl(GetUserUseCase):

    def __init__(self, service: UserQueryService):
        self.service: UserQueryService = service

    def __call__(self, args: Tuple[int]) -> UserReadModel:
        (id_,) = args

        try:
            user = self.service.find_by_id(id_)
            if user is None:
                raise UserNotFoundError()
        except Exception:
            raise

        return user
