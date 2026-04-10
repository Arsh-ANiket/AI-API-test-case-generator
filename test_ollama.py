import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "Generate 3 API test cases for GET /users",
        "stream": False,
    },
)

print(response.json())
