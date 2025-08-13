import re

def clean_text(text: str) -> str:
    """Basic cleanup for questions/answers."""
    if not text:
        return ""
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

def normalize_question(question: str) -> str:
    """Ensure question is formatted for T5 input."""
    question = clean_text(question)
    if not question.lower().startswith("question:"):
        question = f"question: {question}"
    return question

def truncate_text(text: str, max_chars: int = 500) -> str:
    """Truncate text to avoid exceeding model token limits."""
    text = clean_text(text)
    if len(text) > max_chars:
        text = text[:max_chars] + "..."
    return text
