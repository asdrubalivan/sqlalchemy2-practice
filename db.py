from sqlalchemy import create_engine, Engine
from typing import Callable, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session
from sqlalchemy.types import Boolean, String
from rich.repr import RichReprResult
from rich.console import RenderResult, Console, ConsoleOptions
from rich.table import Table

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

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        yield f"[b]Todo #{self.id}[/b]"
        table = Table("Attribute", "Value")
        table.add_row("id", str(self.id))
        table.add_row("finished", "[green]yes" if self.finished else "[red]no")
        table.add_row("name", self.name)
        table.add_row("description", self.description)
        yield table

    def __rich_repr__(self) -> RichReprResult:
        yield "ID", self.id
        yield "Finished", ("yes" if self.finished else "no")
        yield "Name", self.name
        if self.description is not None:
            yield "Description", self.description


def create_tables() -> None:
    Base.metadata.create_all(get_engine())
