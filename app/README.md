# 🤖 AI-Powered API Testing Assistant

An intelligent backend system that automatically generates and executes API test cases using a local LLM (Ollama).
This project demonstrates how AI can be integrated into backend workflows to automate testing and validation.

---

## 🚀 Features

- 🔗 Accepts API endpoint and method as input
- 🤖 Uses local LLM (Ollama) to generate test cases
- 🧪 Executes API requests dynamically
- ✅ Validates responses (status + basic structure)
- 🛡️ Handles unreliable AI output gracefully
- 📊 Returns structured results with pass/fail summary

---

## 🧠 How It Works

```
User Request → FastAPI → AI (Ollama)
                         ↓
                  Generate Test Cases
                         ↓
                  Execute API Calls
                         ↓
                  Validate Response
                         ↓
                      Output
```

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **AI Engine**: Ollama (Local LLM - llama3)
- **HTTP Client**: requests
- **Language**: Python

---

## 📂 Project Structure

```
ai-api-tester/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── ai_service.py    # AI integration (Ollama)
│   └── tester.py        # API testing engine
│
├── venv/
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd ai-api-tester
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install fastapi uvicorn requests python-dotenv
```

---

### 4. Install & Run Ollama

Download and install Ollama, then run:

```bash
ollama run llama3
```

---

### 5. Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

### 6. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📥 API Usage

### Endpoint: `/analyze`

**Method:** POST

### Request Body:

```json
{
  "url": "https://jsonplaceholder.typicode.com/users",
  "method": "GET"
}
```

---

### Response Example:

```json
{
  "summary": {
    "total_tests": 3,
    "passed": 2,
    "failed": 1
  },
  "test_cases": [
    {
      "name": "Valid request",
      "method": "GET",
      "expected_status": 200
    }
  ],
  "results": [
    {
      "name": "Valid request",
      "actual_status": 200,
      "status_pass": true,
      "has_data": true,
      "data_type": "list"
    }
  ]
}
```

---

## ⚠️ Limitations

- AI output may not always be valid JSON
- Response validation is basic (status + structure)
- No authentication or headers support yet
- No frontend (API-only project)

---

## 🧠 Key Learnings

- Integrating LLMs into backend systems
- Prompt engineering for structured outputs
- Handling unreliable AI responses
- Designing modular backend services
- Building automated API testing workflows

---

## 💡 Future Improvements

- Add request body support for POST/PUT APIs
- Enhance response validation (schema-based)
- Add retry mechanism for AI failures
- Support headers and authentication
- Dockerize for deployment

---
