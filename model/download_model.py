import os
import requests

MODEL_URL = "https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf/resolve/main/ggml-model-q4_K.gguf"
MODEL_PATH = "model.gguf"

def ensure_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        response = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)
        print("Model downloaded.")
    return MODEL_PATH