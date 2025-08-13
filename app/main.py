from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import generate_only, rag_only, rag_hybrid, rag_summary

app = FastAPI(title="KIT RAG + T5 API")

@app.get("/", include_in_schema= True)
def root():
    return RedirectResponse(url="/docs")


@app.get("/healthz")
def healthz():
    return {"ok": True}

# Register routes
app.include_router(generate_only.router)
app.include_router(rag_only.router)
app.include_router(rag_hybrid.router)
app.include_router(rag_summary.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)