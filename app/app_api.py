from fastapi import FastAPI, HTTPException
from .app import * 

app = FastAPI()

# @app.get("/generate-content")
# async def generate_content_api(prompt: str):
#     content = generateContent(prompt)
#     return {"content" : content}

# @app.get("/generate-keywords")
# async def generate_keywords_api(prompt: str):
#     keywords = generateKeywords(prompt)
#     return {"keywords" : keywords}


@app.get("/generate-content")
async def generate_content_api(prompt: str):
    if validateInput(prompt):
        content = generateContent(prompt)
        keywords = generateKeywords(prompt)
        return {"content" : content, "keywords": keywords}
    
    else:
        raise HTTPException(status_code=404, detail="Entry too  long! Must be under 30 characters")





"""
To run API

uvicorn app.app_api:app --reload
"""







