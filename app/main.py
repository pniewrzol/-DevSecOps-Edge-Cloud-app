"""SmartGate DevSecOps: local parking access simulator, not real barrier control."""
from contextlib import asynccontextmanager
import os
import secrets
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel, Field
from app.parking import initialize, check_plate, event_summary


@asynccontextmanager
async def lifespan(_app: FastAPI):
    initialize()
    yield


app = FastAPI(title="SmartGate DevSecOps (Edge demo)", version="0.2.0", lifespan=lifespan)


class AccessRequest(BaseModel):
    plate: str = Field(min_length=4, max_length=20, description="Fictional plate: e.g. SK 12345")


def require_api_key(x_api_key: str | None = Header(default=None)) -> None:
    configured = os.environ.get("SMARTGATE_API_KEY", "")
    if not configured:
        raise HTTPException(status_code=503, detail="API key not configured")
    if x_api_key is None or not secrets.compare_digest(x_api_key, configured):
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/health")
def health():
    return {"status": "ok", "service": "smartgate-edge-demo"}


@app.get("/")
def root():
    return {"message": "SmartGate DevSecOps Edge demonstrator", "status": "prototype"}


@app.post("/api/v1/access/check", dependencies=[Depends(require_api_key)])
def check_access(request: AccessRequest):
    try:
        return check_plate(request.plate)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.get("/api/v1/events/summary", dependencies=[Depends(require_api_key)])
def events_summary():
    return event_summary()
