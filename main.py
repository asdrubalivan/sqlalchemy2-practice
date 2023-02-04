import typer
import click
from rich.panel import Panel
from rich.pretty import Pretty
import db
from db import TodoItem
from rich import print

app = typer.Typer()


@app.command()
def create_todo(name: str, finished: bool = True) -> None:
    with db.session() as session:
        session.add(TodoItem(name=name, finished=finished))
        session.commit()


@app.command()
def list_todos() -> None:
    with db.session() as session:
        values = session.query(TodoItem).all()
    for v in values:
        print(Panel(v))


@app.command()
def get_todo_by_id(id: int) -> None:
    with db.session() as session:
        print(session.query(TodoItem).get(id))


@app.command()
def mark_todo(id: int, finished: bool) -> None:
    with db.session() as session:
        value = session.query(TodoItem).get(id)
        if value:
            value.finished = finished
        session.add(value)
        session.commit()
        print("Value updated", value)


@app.command()
def create_tables() -> None:
    print("[green] Creating tables")
    db.create_tables()


if __name__ == "__main__":
    app()
