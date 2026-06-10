from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

MODEL_NAME = ("j-hartmann/emotion-english-distilroberta-base")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

labels = [ "anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]

def predict_emotion(text):
    inputs = tokenizer( text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = F.softmax( outputs.logits, dim=1)[0]
    confidence_scores = {}

    for idx, label in enumerate(labels):
        confidence_scores[label] = round( float(probs[idx]) * 100, 2)

    predicted_class = labels[torch.argmax(probs).item()]
    return predicted_class, confidence_scores