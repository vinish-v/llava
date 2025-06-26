from flask import Flask, request, jsonify
from PIL import Image
import base64
import io
from llama_cpp import Llama
from model.download_model import ensure_model

app = Flask(__name__)
model_path = ensure_model()

llm = Llama(model_path=model_path, n_ctx=2048, verbose=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    img_b64 = data.get("image_base64")
    prompt = data.get("prompt", "")

    if not img_b64:
        return jsonify({"error": "Missing image_base64"}), 400

    try:
        # Decode and save image
        image_data = base64.b64decode(img_b64.split(",")[-1])
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        image.save("input.jpg")

        # Custom system prompt for mood + playlist
        custom_prompt = (
            "You are an expert at analyzing human emotions and a world-class DJ.\n\n"
            "Your task is two-fold: determine a mood, then create a matching playlist.\n\n"
            "1. **Determine the Mood:**\n"
            "   Analyze the user's facial expression from their photo. The mood must be a single, descriptive word from this list:\n"
            "   Happy, Sad, Energetic, Calm, Thoughtful, Excited, Content, Melancholy, Playful, Serious.\n"
            "   - Based on the final mood, select a single, representative emoji.\n\n"

        )

        full_prompt = f"<|user|>\n<image>\n{custom_prompt}\n<|assistant|>\n"
        result = llm(full_prompt, images=["input.jpg"])

        return jsonify({"result": result["choices"][0]["text"].strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
