from fastapi import FastAPI
import chromadb
import ollama

app = FastAPI()
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")

@app.post("/query")
def query(q: str):
    results = collection.query(query_texts=[q], n_results=1)

    docs = results.get("documents", [[]])[0]
    context = docs[0] if docs else ""

    if not context.strip():
        return {"answer": "I don't know based on the provided documents."}

    prompt = f"""You are a QA system.
Use ONLY the CONTEXT to answer. If the answer is not in the context, say:
"I don't know based on the provided documents."

CONTEXT:
{context}

QUESTION:
{q}

ANSWER:"""

    answer = ollama.generate(
        model="tinyllama",
        prompt=prompt,
        options={"temperature": 0}
    )

    return {"answer": answer["response"]}
