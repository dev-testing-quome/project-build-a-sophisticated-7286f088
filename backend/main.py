import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from database import engine
from routers import contracts, users # Import your routers
from models import Base # Import your base model

app = FastAPI(title="Contract Review Management", version="1.0.0", openapi_url="/openapi.json")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # Replace with your allowed origins in production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Database Initialization
Base.metadata.create_all(bind=engine)

# Router Registration
app.include_router(contracts.router)
app.include_router(users.router)

# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Static Files serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{file_path:path}")
    async def serve_frontend(file_path: str):
        if file_path.startswith("api/") or file_path.startswith("static/") or file_path == "favicon.ico":
            return None  # Let API routes and static files handle it
        index_file = os.path.join("static", "index.html")
        if os.path.exists(index_file):
            return HTMLResponse(content=open(index_file, "r").read())
        else:
            raise HTTPException(status_code=404, detail="Not Found")
else:
    print("Warning: 'static' directory not found. Frontend assets will not be served.")

# Error Handling
@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    return HTTPException(status_code=500, detail=str(exc))

# Run the application (for development)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
