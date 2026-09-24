from dataclasses import dataclass
import time
from typing import Callable, List, Optional
from core.jev_engine import JevDecision, JevEngine
from core.risk_manager import RiskManager


@dataclass
class ExecutionLog:
    timestamp: str
    symbol: str
    action: str
    executed: bool
    confidence: float
    required_confidence: float
    reason: str


class StrategyEngine:
    """Strategy Canvas & Execution Engine.

    Assembles triggers, JEV AI block inference, risk checks, and action
    execution.
    """

    def __init__(self, jev_engine: JevEngine, risk_manager: RiskManager):
        self.jev_engine = jev_engine
        self.risk_manager = risk_manager
        self.required_confidence: float = 90.0  # Default 90%
        self.logs: List[ExecutionLog] = []

    def run_strategy_tick(
        self,
        symbol: str,
        current_price: float,
        rsi: float,
        volume_spike: bool,
        trade_amount_usd: float,
    ) -> ExecutionLog:
        """Executes a single market tick check through the Strategy Canvas pipeline."""
        now_str = time.strftime("%H:%M:%S")

        # Step 1: Evaluate Market through JEV Engine
        decision: JevDecision = self.jev_engine.evaluate_market(
            symbol, current_price, rsi, volume_spike
        )

        # Default state
        executed = False
        reason = ""

        # Step 2: Signal Filter
        if decision.action == "HOLD":
            reason = f"JEV issued HOLD decision. {decision.details}"
            log = ExecutionLog(
                now_str,
                symbol,
                decision.action,
                False,
                decision.confidence,
                self.required_confidence,
                reason,
            )
            self.logs.append(log)
            return log

        # Step 3: Confidence Score Gate
        if decision.confidence < self.required_confidence:
            reason = (
                f"Signal ignored: JEV confidence was {decision.confidence}%, "
                f"required {self.required_confidence}%."
            )
            log = ExecutionLog(
                now_str,
                symbol,
                decision.action,
                False,
                decision.confidence,
                self.required_confidence,
                reason,
            )
            self.logs.append(log)
            return log

        # Step 4: Safety Net Validation
        risk_check = self.risk_manager.validate_trade(trade_amount_usd)
        if not risk_check.passed:
            reason = f"Risk Control Block: {risk_check.reason}"
            log = ExecutionLog(
                now_str,
                symbol,
                decision.action,
                False,
                decision.confidence,
                self.required_confidence,
                reason,
            )
            self.logs.append(log)
            return log

        # Step 5: Execution Granted
        executed = True
        reason = f"Order Executed successfully on {symbol} at ${current_price:.2f}. Latency: {decision.latency_ms}ms."
        log = ExecutionLog(
            now_str,
            symbol,
            decision.action,
            True,
            decision.confidence,
            self.required_confidence,
            reason,
        )
        self.logs.append(log)
        return log
