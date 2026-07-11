from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Learning Journey",
    description="A practical project for learning professional backend development.",
    version="1.0.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "FastAPI Learning Journey boshlandi!",
        "status": "success",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }