from fastapi import APIRouter
from pydantic import BaseModel
from services.mcp import handle_query

router = APIRouter()

class Query(BaseModel):
    query: str

@router.post("/ask")
async def ask_question(q: Query):
    response = await handle_query(q.query)
    return {"response": response}
