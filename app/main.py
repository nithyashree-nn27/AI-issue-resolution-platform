import logging
import time

from fastapi import FastAPI, Request

from app.api.routes import router
from app.config.logging import configure_logging
from app.config.settings import settings


configure_logging()

logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.app_name,
    description=(
        "Sanitized representative implementation of an "
        "AI-powered enterprise issue-resolution workflow."
    ),
    version=settings.app_version,
)


@app.middleware("http")
async def request_logging_middleware(
    request: Request,
    call_next,
):
    """Log request method, path, status, and processing time."""

    start_time = time.perf_counter()

    response = await call_next(request)

    duration_ms = (
        time.perf_counter() - start_time
    ) * 1000

    logger.info(
        "HTTP request completed | method=%s | path=%s | "
        "status=%s | duration_ms=%.2f",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )

    return response


app.include_router(router)


@app.get(
    "/",
    summary="Service information",
)
def root():
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "status": "running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get(
    "/health",
    summary="Health check",
)
def health_check():
    return {
        "status": "healthy",
        "service": "ai-issue-resolution-platform",
        "environment": settings.environment,
    }