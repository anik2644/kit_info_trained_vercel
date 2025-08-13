from fastapi import APIRouter
from app.schemas.request import RagRequest
from app.models.rag_model import retrieve_top_k
from app.models.t5_model import generate_answer

router = APIRouter()

@router.post("/rag-summary")
async def rag_summary(req: RagRequest):
    results = retrieve_top_k(req.question)
    top_answers = [r["answer"] for r in results]
    summary = generate_answer(f"summarize: {' '.join(top_answers)}")
    return {
        "question": req.question,
        "top_answers": top_answers,
        "summary": summary,
        "source": "Summary of top 3 RAG answers"
    }
