from dataclasses import dataclass
import time
from typing import List
from core.jev_engine import JevEngine, SentimentResult


@dataclass
class NewsAlert:
    timestamp: str
    source: str
    content: str
    score: int
    confidence: float
    trade_triggered: bool
    details: str


class SentimentScanner:
    """Sentiment Scanner (HFT News Module).

    Parses RSS/Twitter feeds and triggers instant orders via JEV sentiment
    scores.
    """

    def __init__(self, jev_engine: JevEngine):
        self.jev_engine = jev_engine
        self.target_keyword = "DOGE"
        self.min_sentiment_score = 4  # Require score >= 4 out of 5
        self.alerts: List[NewsAlert] = []

    def process_incoming_post(
        self, source: str, text: str
    ) -> NewsAlert:
        """Processes live incoming post in real-time."""
        now_str = time.strftime("%H:%M:%S")

        # Analyze using Jev NLP model
        result: SentimentResult = self.jev_engine.evaluate_news_sentiment(text)

        trade_triggered = False
        details = ""

        if self.target_keyword.lower() in text.lower():
            if result.score >= self.min_sentiment_score:
                trade_triggered = True
                details = (
                    f"HFT Trigger Fired! Keyword '{self.target_keyword}' found with sentiment score {result.score}/5. "
                    f"Order placed in {result.latency_ms}ms."
                )
            else:
                details = (
                    f"Keyword found, but sentiment score ({result.score}/5) "
                    f"did not meet required threshold ({self.min_sentiment_score}/5)."
                )
        else:
            details = f"Target keyword '{self.target_keyword}' not found in news stream."

        alert = NewsAlert(
            timestamp=now_str,
            source=source,
            content=text,
            score=result.score,
            confidence=result.confidence,
            trade_triggered=trade_triggered,
            details=details,
        )
        self.alerts.append(alert)
        return alert
