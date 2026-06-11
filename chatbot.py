responses = {"joy":"""You seem happy today. Keep enjoying the positive moments.""",
             "sadness":"""I noticed sadness in your text. Consider listening to uplifting music or talking with someone you trust.""",
             "anger":"""You appear frustrated. Relaxing music or a short break may help.""",
             "fear":"""Fear can be challenging. Focus on one step at a time.""",
             "surprise":"""Something unexpected happened. I hope it brings new opportunities.""",
             "neutral":"""Your message appears balanced. Have a productive day.""",
             "disgust":"""That seems uncomfortable. Consider focusing on things that improve your mood."""
}

def generate_reply(emotion):

    return responses.get(emotion, "Tell me more about how you feel.")