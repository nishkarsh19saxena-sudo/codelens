from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.ai import review_code


app = FastAPI(title="AI Code Reviewer")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def home():
    return {
        "message": "AI Code Reviewer is running!"
    }


@app.post("/analyze")
def analyze(request: CodeRequest):

    print("CODE RECEIVED:")
    print(request.code)

    result = review_code(request.code)

    print("RETURNING RESULT:")
    print(result)

    return {
        "analysis": result
    }