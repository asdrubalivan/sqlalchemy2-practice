import typer
import db
from db import TodoItem

app = typer.Typer()


@app.command()
def create_todo(name: str, finished: bool = True) -> None:
    with db.session() as session:
        session.add(TodoItem(finished=finished))
        session.commit()


@app.command()
def create_tables() -> None:
    print("Creating tables")
    db.create_tables()


if __name__ == "__main__":
    app()
