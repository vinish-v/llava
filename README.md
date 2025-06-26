# 🦙 LLaVA Flask API (Railway Ready)

This is a Flask-based API that uses `llama-cpp-python` to analyze a base64 image using a LLaVA-compatible model.

## ✅ Features

- Upload base64 image
- Returns LLaVA-generated mood description
- No OpenAI or Gemini API needed
- Fully self-hosted and free to run (Railway)

## 📦 How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## 🚀 Deploy to Railway

1. Push to GitHub
2. Deploy from GitHub in Railway
3. Set `web: python app.py` in Procfile

Use `/analyze` endpoint with:
```json
{
  "image_base64": "data:image/png;base64,...",
  "prompt": "Describe the mood"
}
```