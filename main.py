from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/summarize")
def summarize_article(request: URLRequest):
    try:
        response = requests.get(request.url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        if not text:
            raise HTTPException(status_code=400, detail="Conteúdo não encontrado.")

        prompt = f"Resuma o seguinte artigo de blog em português:\n\n{text[:6000]}"
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        summary = completion.choices[0].message["content"]
        return {"summary": summary.strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
