
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI Text Analyzer")

POSITIVE_WORDS = {"love", "great", "good", "happy", "excellent", "exciting"}
NEGATIVE_WORDS = {"hate", "bad", "sad", "terrible", "awful", "angry"}


class TextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/analyze")
def analyze_text(request: TextRequest):
    text = request.text
    words = text.split()
    word_set = {word.strip(".,!?;:").lower() for word in words}

    positive_count = len(word_set & POSITIVE_WORDS)
    negative_count = len(word_set & NEGATIVE_WORDS)

    if positive_count > negative_count:
        sentiment = "positive"
    elif negative_count > positive_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "word_count": len(words),
        "character_count": len(text),
        "sentiment": sentiment
    }
