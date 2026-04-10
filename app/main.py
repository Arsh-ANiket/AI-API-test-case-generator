from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_service import generate_test_cases
from app.tester import run_test_cases

app = FastAPI()


# This defines what input we expect
class APIRequest(BaseModel):
    url: str
    method: str = "GET"


# basic route
@app.get("/")
def root():
    return {"message": "server is running!"}


# main route
@app.post("/analyze")
def analyze_api(request: APIRequest):
    # here we link ai_service.py to the analyze rout
    test_cases = generate_test_cases(request.url, request.method)

    if isinstance(test_cases, dict) and "error" in test_cases:
        return test_cases

    results = run_test_cases(request.url, test_cases)
    # retuyrn part 3
    return {"test_cases": test_cases, "results": results}

    # original return
    # return {
    #     "received_url": request.url,
    #     "method": request.method,
    #     "status": "Ready for AI processing",
    # }
    # reutn part 2
    # return {
    #     "url": request.url,
    #     "method": request.method,
    #     "ai_generated_test_cases": test_cases,
    # }
