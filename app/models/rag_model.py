import json
import torch
from sentence_transformers import SentenceTransformer, util
from app import config

print("Loading SentenceTransformer embedder...")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

with open(config.KB_FILE, "r", encoding="utf-8") as f:
    qa_pairs = json.load(f)

print(f"Loaded {len(qa_pairs)} QA pairs.")
question_texts = [pair["question"] for pair in qa_pairs]
question_embeddings = embedder.encode(question_texts, convert_to_tensor=True)

def retrieve_top_k(query: str, k=config.TOP_K):
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    cos_scores = util.cos_sim(query_embedding, question_embeddings)[0]
    top_results = torch.topk(cos_scores, k=min(k, len(qa_pairs)))
    results = []
    for idx, score in zip(top_results.indices, top_results.values):
        idx = int(idx)
        results.append({
            "question": qa_pairs[idx]["question"],
            "answer": qa_pairs[idx]["answer"],
            "similarity": float(score)
        })
    return results
