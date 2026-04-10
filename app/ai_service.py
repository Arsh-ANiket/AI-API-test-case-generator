import requests
import json

# this is where ollama is running locally
OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_test_cases(url, method):
    prompt = f"""
You are an expert QA engineer.

Generate API test cases in STRICT JSON format.

API Details:
URL: {url}
Method: {method}

Rules:
- Return ONLY JSON (no explanation)
- Output must be a list
- Each test case must have:
  - name
  - method
  - expected_status

Example:
[
  {{
    "name": "Valid request",
    "method": "GET",
    "expected_status": 200
  }},
  {{
    "name": "Invalid endpoint",
    "method": "GET",
    "expected_status": 404
  }}
]
"""
    # calling ollama API
    # we send the prompt and get the response
    # we are making a POST req to AI
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False,
        },
    )

    data = response.json()
    ai_text = data.get("response", "")
    try:
        test_cases = json.loads(ai_text)
    except Exception:
        test_cases = {"error": "Invalid JSON from AI", "raw": ai_text}
    # print("FULL AI RESPONSE:", data)  # 👈 add this

    return test_cases
