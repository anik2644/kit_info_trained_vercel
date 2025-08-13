from fastapi import APIRouter
from app.schemas.request import RagRequest
from app.models.t5_model import generate_answer

router = APIRouter()

@router.post("/generate-only")
async def generate_only(req: RagRequest):
    ans = generate_answer(f"question: {req.question}")
    return {
        "question": req.question,
        "generated_answer": ans,
        "source": "T5 only"
    }
