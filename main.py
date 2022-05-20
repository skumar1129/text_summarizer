from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from text_summarization.summarizer import analyze_text

app = FastAPI()


class EndpointRequest(BaseModel):
    text: str

@app.post('/summarize-text', status_code=200)
async def read_item(text_request: EndpointRequest):
    try:
        return analyze_text(text_request.text)
    except Exception as e:
         return HTTPException(status_code=500, detail=f'Error {e} while trying to summarize text')