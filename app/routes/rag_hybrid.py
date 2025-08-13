from fastapi import APIRouter
from app.schemas.request import RagRequest
from app.models.rag_model import retrieve_top_k
from app.models.t5_model import generate_answer
from app import config

router = APIRouter()

@router.post("/rag-hybrid")
async def rag_hybrid(req: RagRequest):
    results = retrieve_top_k(req.question)
    best_match = results[0]

    if best_match["similarity"] >= config.SIMILARITY_THRESHOLD:
        return {
            "question": req.question,
            "matched_question": best_match["question"],
            "answer": best_match["answer"],
            "similarity": round(best_match["similarity"], 4),
            "source": "RAG (high confidence)"
        }
    else:
        ans = generate_answer(f"question: {req.question}")
        return {
            "question": req.question,
            "final_answer": ans,
            "similarity": round(best_match["similarity"], 4),
            "source": "T5 only (low RAG confidence)"
        }
