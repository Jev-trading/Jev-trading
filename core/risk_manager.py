from dataclasses import dataclass


@dataclass
class RiskCheckResult:
    passed: bool
    reason: str


class RiskManager:
    """Safety Net: Enforces maximum drawdown limits, maximum trade volume,

    and emergency circuit breakers.
    """

    def __init__(
        self,
        max_daily_drawdown_pct: float = 5.0,
        max_trade_volume_usd: float = 1000.0,
    ):
        self.max_daily_drawdown_pct = max_daily_drawdown_pct
        self.max_trade_volume_usd = max_trade_volume_usd
        self.current_daily_loss_pct = 0.0
        self.circuit_breaker_tripped = False

    def update_daily_loss(self, PnL_pct: float) -> None:
        """Updates cumulative daily loss percentage."""
        if PnL_pct < 0:
            self.current_daily_loss_pct += abs(PnL_pct)
            if self.current_daily_loss_pct >= self.max_daily_drawdown_pct:
                self.circuit_breaker_tripped = True

    def reset_daily_limits() -> None:
        """Resets daily loss counter at start of a new trading day."""
        self.current_daily_loss_pct = 0.0
        self.circuit_breaker_tripped = False

    def validate_trade(self, amount_usd: float) -> RiskCheckResult:
        """Validates if trade execution adheres to risk control policies."""
        if self.circuit_breaker_tripped:
            return RiskCheckResult(
                passed=False,
                reason=f"Daily Max Drawdown Limit ({self.max_daily_drawdown_pct}%) breached! System halted.",
            )

        if amount_usd > self.max_trade_volume_usd:
            return RiskCheckResult(
                passed=False,
                reason=f"Requested volume (${amount_usd:.2f}) exceeds Max Trade Volume Limit (${self.max_trade_volume_usd:.2f}).",
            )

        return RiskCheckResult(passed=True, reason="Risk parameters cleared.")
