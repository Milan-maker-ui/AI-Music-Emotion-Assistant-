# 🎵 AI Music Emotion Assistant

An AI-powered web application that detects emotions from user text, supports multilingual input, provides emotion-based music recommendations, and offers an emotion-aware chatbot response.

---

## 🚀 Features

### 🧠 Emotion Detection
- Uses Hugging Face Transformers
- DistilRoBERTa emotion classification model
- Detects:
  - Joy 😊
  - Sadness 😢
  - Anger 😠
  - Fear 😨
  - Surprise 😲
  - Neutral 😐
  - Disgust 🤢

### 🌍 Multilingual Support
Supports:
- English
- Hindi
- Marathi
- Any language supported by Google Translate

Automatically translates text to English before prediction.

### 🎵 Music Recommendation
Provides music suggestions based on detected emotion.

Example:

| Emotion | Recommendation |
|----------|---------------|
| Joy | Happy Songs |
| Sadness | Motivational Songs |
| Anger | Relaxing Music |
| Fear | Calm Instrumentals |
| Neutral | Lo-Fi Music |

### 🤖 Emotion Chatbot
Generates supportive responses according to detected emotion.

### 📊 Visualization Dashboard
- Confidence Score Bars
- Pie Chart Visualization
- Interactive UI

### 💾 Analysis History
Stores all predictions in SQLite database.

---





