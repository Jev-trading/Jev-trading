import random
from typing import Dict, List


class ExchangeHub:
    """Manages connections to CEX (Binance, Bybit, OKX, Coinbase) and Web3 DEX

    wallets (MetaMask, Phantom). Aggregates user balances.
    """

    def __init__(self):
        self.connections: Dict[str, bool] = {
            "Binance": False,
            "Bybit": False,
            "OKX": False,
            "Coinbase": False,
            "MetaMask (Ethereum)": False,
            "Phantom (Solana)": False,
        }
        self.encrypted_keys: Dict[str, str] = {}
        self.mock_balances: Dict[str, Dict[str, float]] = {
            "Binance": {"USDT": 12500.0, "BTC": 0.45, "ETH": 3.2},
            "Bybit": {"USDT": 8300.0, "BTC": 0.12},
            "OKX": {"USDT": 4100.0, "ETH": 1.5},
            "Coinbase": {"USD": 2500.0},
            "MetaMask (Ethereum)": {"ETH": 4.8, "USDC": 3000.0},
            "Phantom (Solana)": {"SOL": 120.0, "USDC": 1500.0},
        }

    def connect_cex(
        self, exchange_name: str, api_key: str, api_secret: str
    ) -> bool:
        """Validates and establishes CEX API connection."""
        if exchange_name in self.connections:
            # Simulate basic connection verification
            if len(api_key) > 5 and len(api_secret) > 5:
                self.connections[exchange_name] = True
                return True
        return False

    def connect_web3_wallet(
        self, wallet_name: str, wallet_address: str
    ) -> bool:
        """Connects Web3 wallet address for DEX monitoring."""
        if wallet_name in self.connections and len(wallet_address) > 10:
            self.connections[wallet_name] = True
            return True
        return False

    def disconnect(self, platform_name: str) -> None:
        """Disconnects platform."""
        if platform_name in self.connections:
            self.connections[platform_name] = False

    def get_aggregated_balances(self) -> Dict[str, float]:
        """Calculates total portfolio balance aggregated across active connections."""
        totals: Dict[str, float] = {}
        for platform, is_connected in self.connections.items():
            if is_connected and platform in self.mock_balances:
                for asset, amount in self.mock_balances[platform].items():
                    totals[asset] = totals.get(asset, 0.0) + amount
        return totals

    def get_connection_statuses(self) -> Dict[str, bool]:
        """Returns connection states of all supported platforms."""
        return self.connections
