music_database = {
    "joy": ["Happy - Pharrell Williams", "Can't Stop The Feeling", "Good Life"],
    "sadness": ["Fix You", "Hall Of Fame", "Rise Up"],
    "anger": ["Weightless", "River Flows In You", "Relaxing Piano"],
    "fear": ["Peaceful Meditation", "Nature Sounds", "Calm Waves"],
    "surprise": ["Trending Global Hits", "Top Pop Songs", "Fresh Discoveries"],
    "neutral": ["LoFi Beats", "Study Music", "Coffee Shop Jazz"],
    "disgust": ["Instrumental Relaxation", "Healing Sounds"]
}

def recommend_music(emotion):
    return music_database.get(emotion, ["LoFi Beats"])