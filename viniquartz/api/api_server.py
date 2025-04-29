import sys
import os

from fastapi import FastAPI, Request, HTTPException # type: ignore
from api.routers import users_router, superusers_router, top_countries_router, teams_router

# Fix path modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

# routes
app.include_router(users_router)
app.include_router(superusers_router)
app.include_router(top_countries_router)
app.include_router(teams_router)

@app.get("/")
def read_root():
    return {"message": "API está funcionando!"}