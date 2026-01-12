from fastapi import FastAPI, Form, HTTPException
import requests

app = FastAPI()

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Input text is empty")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": f"Summarize this:\n\n{text}",
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()
        result = response.json()

        if "response" not in result:
            raise HTTPException(status_code=500, detail="Invalid response from Ollama")

        return {"summary": result["response"]}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
