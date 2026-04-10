import requests

# this is where ollama is running locally
OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_test_cases(url, method):
    prompt = f"""
    You are an expert QA engineer.
    
    Generate API test cases for:
    URL: {url}
    Method: {method}
    
    Include:
    - Normal test cases
    - Edge cases
    - Invalid input cases
    
    Return respnonse in JSON format like:
    [
      {{
        "name": "Test case name",
        "description": "What it tests"
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
    print("FULL AI RESPONSE:", data)  # 👈 add this

    return data.get("response", "No response from AI")
