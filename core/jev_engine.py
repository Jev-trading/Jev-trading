import random
import time
from dataclasses import dataclass


@dataclass
class JevDecision:
    action: str  # "BUY", "SELL", or "HOLD"
    confidence: float  # Confidence percentage (0.0 to 100.0)
    latency_ms: float  # Time taken in milliseconds
    details: str  # Additional technical justification from Jev neural model


@dataclass
class SentimentResult:
    score: int  # 1 (Very Negative) to 5 (Very Positive)
    confidence: float  # Confidence score 0-100%
    latency_ms: float  # Analysis latency in ms
    summary: str  # Summary of detected impact


class JevEngine:
    """Simulates TypeSafe AI's ultra-fast Jev neural network engine.

    Delivers low-latency decision matrix (70-300 ms) for price action and
    sentiment.
    """

    def __init__(self):
        self.version = "Jev-v2.4-Turbo"

    def evaluate_market(
        self, symbol: str, price: float, rsi: float, volume_spike: bool
    ) -> JevDecision:
        """Performs ultra-fast inference over orderbook and market indicators."""
        start_time = time.perf_counter()

        # Simulate hardware neural engine processing delay (70 - 300 ms)
        simulated_delay = random.uniform(0.07, 0.30)
        time.sleep(simulated_delay)

        # Signal generation logic using weights
        if rsi < 30 or volume_spike:
            action = "BUY"
            confidence = round(random.uniform(85.0, 98.5), 2)
            details = (
                f"Oversold condition (RSI: {rsi:.1f}) + Orderbook imbalance."
            )
        elif rsi > 70:
            action = "SELL"
            confidence = round(random.uniform(82.0, 96.0), 2)
            details = f"Overbought territory (RSI: {rsi:.1f}) with high ask volume wall."
        else:
            action = "HOLD"
            confidence = round(random.uniform(50.0, 75.0), 2)
            details = (
                "Market in consolidation phase. No clear alpha vector."
            )

        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        return JevDecision(
            action=action,
            confidence=confidence,
            latency_ms=elapsed_ms,
            details=details,
        )

    def evaluate_news_sentiment(self, text: str) -> SentimentResult:
        """Parses news or tweet text in sub-second time to derive sentiment score."""
        start_time = time.perf_counter()

        # Ultra-fast NLP parsing simulation delay
        time.sleep(random.uniform(0.05, 0.15))

        text_lower = text.lower()
        score = 3
        summary = "Neutral sentiment detected."

        positive_keywords = [
            "doge",
            "bullish",
            "partnership",
            "approval",
            "surge",
            "breakout",
            "moon",
        ]
        negative_keywords = [
            "hack",
            "exploit",
            "sec",
            "lawsuit",
            "ban",
            "crash",
            "dump",
        ]

        pos_count = sum(1 for w in positive_keywords if w in text_lower)
        neg_count = sum(1 for w in negative_keywords if w in text_lower)

        if pos_count > neg_count:
            score = min(5, 3 + pos_count)
            summary = (
                f"Positive keywords detected ({pos_count}). Strong upside potential."
            )
        elif neg_count > pos_count:
            score = max(1, 3 - neg_count)
            summary = (
                f"Negative catalysts found ({neg_count}). Downside risk high."
            )

        confidence = round(random.uniform(88.0, 99.1), 2)
        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)

        return SentimentResult(
            score=score,
            confidence=confidence,
            latency_ms=elapsed_ms,
            summary=summary,
        )
