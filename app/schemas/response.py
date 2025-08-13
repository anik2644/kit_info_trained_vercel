from pydantic import BaseModel
from typing import List, Optional

class MatchResult(BaseModel):
    question: str
    answer: str
    similarity: float

class RAGResponse(BaseModel):
    question: str
    top_matches: List[MatchResult]
    source: str

class T5Response(BaseModel):
    question: str
    generated_answer: str
    source: str

class HybridResponse(BaseModel):
    question: str
    matched_question: Optional[str]
    answer: Optional[str]
    final_answer: Optional[str]
    similarity: float
    source: str
