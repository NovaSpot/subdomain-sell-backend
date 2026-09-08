from fastapi import FastAPI
from pydantic import BaseModel
from app.api.v1 import auth, users

import logging
import time
import uuid
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from fastapi import APIRouter, Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.base import RequestResponseEndpoint
from starlette.middleware.trustedhost import TrustedHostMiddleware

from fastapi import FastAPI
from app import database

"""
FastAPI application setup.

1. Import necessary modules and packages
2. Setup logging and structlog configuration
3. Define a lifespan context manager (startup/shutdown logic — e.g. DB connections)
4. Define a function to build/aggregate all routers (_build_api_router())

5. Define the FastAPI application factory: create_app()
   - Create the FastAPI instance (title, version, lifespan, conditional docs)
   - Register exception handlers
   - Add middleware (TrustedHost, CORS, request-id/logging)
   - Include routers (versioned API routes)
   - Define health check endpoints (/health, /ready) directly on app
   - Return the app instance

6. app = create_app()  ← module-level call so ASGI servers can find it
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load anything on startup (e.g., database connection pool)
    print("Starting up...")
    yield
    # Clean up anything on shutdown (e.g., close connections)
    print("Shutting down...")









def main():
    print("Hello from subdomain-sell-backend!")

docs_enabled = True 




def create_app() -> FastAPI:

    app = FastAPI(
        title="Hi API", 
        version="0.1.0",
        lifespan=lifespan,
        docs_url="/docs" if docs_enabled else None,
        redoc_url="/redoc" if docs_enabled else None,
        openapi_url="/openapi.json" if docs_enabled else None,
    )





    app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
    #app.include_router(subdomains.router, prefix="/api/v1/subdomains", tags=["subdomains"])
    app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

    @app.get("/hi")
    async def hi() -> dict[str, str]:
        return {"message": "hi"}

    @app.get("/health", tags=["health"])
    async def health() -> dict[str, str]:
        """Liveness probe — process is up."""
        return {"status": "ok"}

    # @app.get("/ready", tags=["health"])
    # async def ready(db: AsyncSession = Depends(get_db)) -> dict[str, str]:
    #     """Readiness probe — database is reachable."""
    #     await db.execute(text("SELECT 1"))
    #     return {"status": "ready"}

    return app


app = create_app()

#this is not needed if you are using uvicorn to run the app, but it is useful for testing the app directly
if __name__ == "__main__":
    main()
