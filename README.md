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

# ▶️ Run Application

```bash
python app.py
```

Expected Output:

```bash
* Running on http://127.0.0.1:5000
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# 🧪 Example Input

```text
I am very happy because I completed my project successfully.
```

Output:

```text
Emotion:
JOY

Recommendations:
- Happy
- Can't Stop The Feeling
- Good Life

Assistant:
You seem happy today. Keep enjoying the positive moments.
```

---

# 🗄 Database

SQLite database is automatically created:

```text
emotion_history.db
```

Table:

```sql
CREATE TABLE analyses (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    original_text TEXT,

    translated_text TEXT,

    emotion TEXT,

    created_at TIMESTAMP
);
```

---

# 🧠 Model Information

Model:

```text
j-hartmann/emotion-english-distilroberta-base
```

Framework:

```text
Hugging Face Transformers
PyTorch
```

The model downloads automatically during first execution.

Internet connection is required only once.

---

# 🎨 Frontend Technologies

- HTML5
- CSS3
- JavaScript
- Chart.js

UI Features:

- Glassmorphism Design
- Responsive Layout
- Pie Charts
- Confidence Bars
- Loading Spinner

---

# 📈 Future Improvements

### Voice Emotion Detection

```text
Whisper
Speech-to-Text
```

### Spotify Integration

```text
Spotify API
```

### Gemini AI

```text
Emotion Explanation
Advanced Chatbot
```

### User Authentication

```text
Flask Login
JWT
```

### Docker Deployment

```text
Docker
Docker Compose
```

### Cloud Deployment

```text
AWS
Render
Railway
Azure
```

---


