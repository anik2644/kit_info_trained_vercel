from fastapi import APIRouter
from app.schemas.request import RagRequest
from app.models.rag_model import retrieve_top_k

router = APIRouter()

@router.post("/rag-only")
async def rag_only(req: RagRequest):
    results = retrieve_top_k(req.question)
    return {
        "question": req.question,
        "top_matches": results,
        "source": "RAG only"
    }
