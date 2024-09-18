from typing import Sequence

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy import select, update, delete

from app.tracker.task.data.models.task import Task
from app.tracker.task.domain.entities.task_entity import TaskEntity
