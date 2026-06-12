import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from model import predict_emotion
from translator import translate_to_english
from recommender import recommend_music
from chatbot import generate_reply
from database import init_db, save_analysis, get_recent_analyses


load_dotenv()
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
init_db()

@app.route("/")
def home():
    history = get_recent_analyses()
    return render_template("index.html", history=history)

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("text", "")
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    translated_text = translate_to_english(text)
    emotion, confidence_scores = predict_emotion(translated_text)
    recommendations = recommend_music(emotion)
    bot_reply = generate_reply(emotion)
    save_analysis(original_text=text, translated_text=translated_text, emotion=emotion)
    return jsonify({"emotion": emotion, "confidence_scores": confidence_scores, "translated_text": translated_text, "recommendations": recommendations, "bot_reply": bot_reply})

@app.route("/history")
def history():
    data = get_recent_analyses()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)