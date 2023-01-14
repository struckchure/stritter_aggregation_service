import typer
import uvicorn

from config import env

typer_app = typer.Typer()


@typer_app.command()
def run_server(host="0.0.0.0", port=env.API_PORT):
    uvicorn.run(
        "config.app:app",
        host=host,
        port=int(port),
        reload=True,
    )


def main():
    typer_app()


if __name__ == "__main__":
    main()
