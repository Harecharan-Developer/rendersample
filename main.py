from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime, timedelta
import json
from process import read_community_fisherman_data

app = FastAPI()



# Allow CORS for all origins during development (replace "*" with your actual frontend URL in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/schedule/")
def get_schedule():
    allocated_fish_json = read_community_fisherman_data()

    return {"schedule": allocated_fish_json}