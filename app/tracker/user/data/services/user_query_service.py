from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.tracker.user.data.models.user import User
from app.tracker.user.domain.entities.user_query import UserReadModel
from app.tracker.user.domain.services.user_query_service import UserQueryService


class UserQueryServiceImpl(UserQueryService):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> UserReadModel | None:
        result = self.session.get(User, id_)

        if result is None:
            return None

        return result.to_read_model()

    def findall(self) -> Sequence[UserReadModel]:
        statement = select(User).filter_by(is_deleted=False)

        result = self.session.execute(statement).scalars().all()

        return [user.to_read_model() for user in result]
