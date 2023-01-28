from sqlalchemy import create_engine, Engine
from typing import Callable, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session
from sqlalchemy.types import Boolean, String

__all__ = ["get_engine", "Session", "TodoItem"]


def get_engine() -> Engine:
    engine = create_engine("sqlite+pysqlite:///my.db", echo=True)
    return engine


session: Callable[..., Session] = sessionmaker(get_engine())


class Base(DeclarativeBase):
    pass


class TodoItem(Base):
    __tablename__ = "todo_item"

    id: Mapped[int] = mapped_column(primary_key=True)
    finished: Mapped[bool] = mapped_column(Boolean())
    name: Mapped[str] = mapped_column(String())
    description: Mapped[Optional[str]]


def create_tables() -> None:
    Base.metadata.create_all(get_engine())
