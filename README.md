# 🚀 AI Text Summarizer API

## 🔴 Live Demo
https://summarizer-service-230227073831.asia-south1.run.app/

## 📌 Project Description
This project is an AI-based text summarization API. It takes input text and returns a concise yet meaningful summary using Natural Language Processing (NLP) techniques.

## ⚙️ Tech Stack
* Python
* Flask / FastAPI
* NLP (Text Summarization)
* Google Cloud Run

# 🛠️ Project Setup & Execution (Step-by-Step)

## 🔹 1. Create Project Folder
```bash
mkdir ai-summarizer
cd ai-summarizer
```

## 🔹 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
```
Activate:
```bash
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

## 🔹 3. Install Dependencies

```bash
pip install flask transformers torch
```
Save dependencies:
```bash
pip freeze > requirements.txt
```

## 🔹 4. Create Main Application File
Create `app.py` and add your summarization logic.
Run locally:
```bash
python app.py
```

## 🔹 5. Test Locally
Use Postman or curl:
```bash
curl -X POST http://127.0.0.1:5000/summarize \
-H "Content-Type: application/json" \
-d '{"text":"AI is transforming the world"}'
```

# ☁️ Deployment (Google Cloud Run)

## 🔹 1. Build Docker Image
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/summarizer
```

## 🔹 2. Deploy to Cloud Run
```bash
gcloud run deploy summarizer-service \
--image gcr.io/PROJECT-ID/summarizer \
--platform managed \
--region asia-south1 \
--allow-unauthenticated
```

## 🔹 3. Get Live URL
After deployment, you’ll get:
```
https://summarizer-service-xxxxx.run.app
```

# 🔗 API Usage

## Endpoint:
POST /summarize

## Full URL:
https://summarizer-service-230227073831.asia-south1.run.app/summarize

## 📥 Sample Input
```json
{
  "text": "Artificial Intelligence is transforming the world rapidly."
}
```

## 📤 Sample Output
```json
{
  "summary": "AI is transforming the world."
}
```

# 🧪 How to Test
You can test the API using:
* Postman
* cURL
* Any API testing tool

# 💡 Features
* Fast and efficient text summarization
* Cloud-based API
* JSON-based API Request & Response
* Easy integration with any application

# 📷 Future Improvements
* Adding a web interface (UI)
* Supporting multiple languages
* File upload support (PDF, Text)

# 📁 Project Structure
```
ai-summarizer/
│
├── app.py
├── requirements.txt
├── Dockerfile (optional)
├── README.md
```

# 👨‍💻 Author

**Himatej Maradana**
