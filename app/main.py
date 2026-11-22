from fastapi import FastAPI

app = FastAPI(title="Edge–Cloud DevSecOps PoC", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "edge-demo"}


@app.get("/")
def root():
    return {"message": "Edge–Cloud DevSecOps PoC", "status": "prototype"}
