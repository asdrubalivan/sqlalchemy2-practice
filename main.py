from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import Boolean, String


def get_engine() -> Engine:
    engine = create_engine("sqlite+pysqlite:///my.db", echo=True)
    return engine


class Base(DeclarativeBase):
    pass


class TodoItem(Base):
    __tablename__ = "todo_item"

    finished: Mapped[bool] = mapped_column(Boolean())
    name: Mapped[str] = mapped_column(String())
