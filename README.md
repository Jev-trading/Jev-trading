# ⚡Jev-trading: The Ultimate AI Terminal for Algo-Trading

Jev-trading is a desktop application that combines the ultra-fast neural network model **Jev** (by TypeSafe AI) with an intuitive visual interface. We've created a platform where the power of algorithmic trading is accessible without writing a single line of code, messing with Python scripts, or configuring servers in the terminal.

---

## 🚀 Why Jev-trading?

Traditional trading bots require programming knowledge, and integrating regular LLMs (like ChatGPT) into trading is too slow and unpredictable. Jev-trading solves both problems:

* **Full No-Code Experience.** The entire process — from connecting an exchange to building a complex trading strategy — happens in a modern, modular UI/UX interface. Even a beginner can handle it.
* **Ultra-speed of the Jev Neural Network.** Unlike LLMs that generate text over several seconds, the built-in Jev engine analyzes the order book, charts, and news in **70–300 milliseconds**, returning a strict mathematical answer (Buy / Sell / Hold).
* **Absolute Risk Control (Confidence Score).** You don't trust the AI blindly. The interface features an "AI Confidence" slider. If the neural network gives a buy signal but its confidence level is below your set 92%, the trade is canceled.
* **Lightning-fast News Parsing.** The built-in Jev-trading sentiment module reads news feeds and X (Twitter). It manages to evaluate the impact of a tweet and open a trade faster than a human trader can even read the news.
* **Local Security.** The application is installed on your PC (Windows/macOS). All API keys from exchanges are encrypted locally and are never transmitted to our servers.
* **Multi-threading.** The interface allows you to run dozens of independent strategies for different trading pairs in adjacent tabs without overloading the system.

---

## 💾 Desktop Client Installation

Forget about `git clone`, `npm install`, and setting up dependencies. Jev-trading installs like a standard application.

**For Windows users:**

1. Download `Jev-trading-x64.7z` from the [Releases](../../releases) section.
2. Run the file with a double click.
3. Follow the installer instructions (the program will automatically add a desktop shortcut).

**For macOS users (Apple Silicon / Intel):**

1. Download `Jev-trading-macOS.dmg` from the [Releases](../../releases) section.
2. Open the downloaded file.
3. Drag and drop the **Jev-trading** icon into the **Applications** folder.

*Upon the first launch, the program will prompt you to select a Dark or Light theme and set up a master password to encrypt your data.*

---

## ⚙️ Full Functionality: From Start to Profit

Jev-trading implements a modular approach. The interface is divided into logical workspaces.

### 1. Connection Hub

* **CEX Integration:** Automated binding via API keys for Binance, Bybit, OKX, and Coinbase in two clicks.
* **Web3 Wallet Integration (DEX):** Integration with MetaMask and Phantom for trading altcoins and tokens on Uniswap/Raydium.
* **Balance Manager:** A single visual dashboard aggregating data on all your assets across different platforms.

### 2. Strategy Canvas

The core of the application. This is a drag-and-drop workspace where you assemble the bot's logic from pre-built blocks.

* **Trigger Blocks:** Set launch conditions (e.g., "Price dropped by 5% in 15 minutes" or "Trading volume increased 3x").
* **Jev AI Block (Analyst):** You simply drag this block onto the canvas. It takes the current market data and makes a decision. You configure only one parameter: *"Required Confidence"*.
* **Action Blocks:** "Buy at Market", "Place Limit Order", "Move Stop-Loss to Breakeven".
* *No-code connection example:* `If RSI < 30` ➔ `Ask JEV` ➔ `If JEV = BUY and Confidence > 90%` ➔ `Buy with 5% of deposit`.

### 3. Sentiment Scanner (HFT News)

* **Data Feeds:** Connect RSS feeds, Telegram channels, and X (Twitter) accounts.
* **Instant Evaluation:** Jev-trading automatically filters out the noise. You visually configure the reaction: for example, *"If Elon Musk's tweet contains the word DOGE, and JEV evaluates the positive sentiment (Score) at 4/5 ➔ Buy $1000 worth of DOGE"*. Reaction speed is less than a second.

### 4. Safety Net (Advanced Risk Management)

The section where you set global limits to prevent blowing up your deposit.

* **Daily Drawdown:** If the bot loses X% in a day, the program forcibly stops all trading and closes positions until the next day.
* **Volume Isolation:** A strict limit on the maximum size of a single trade (in dollars or percentage of the deposit) that the AI is not allowed to exceed.

### 5. Time Machine (Backtesting Lab)

Before risking real money, you test your build on historical data.

* **Visual Replay:** Load the BTC/USDT chart for the past year, hit play, and see exactly where Jev-trading would have opened and closed trades on the chart.
* **Detailed Report:** Automatic calculation of strategy metrics (Winrate, P&L, Maximum Drawdown, Profit Factor).

### 6. Command Center (Live Dashboard)

The window you keep open while working.

* **Active Bot Cards:** The status of each running algorithm and its current profit for the day/week.
* **AI Log:** A unique feature showing why the bot *did not* enter a trade. (For example: *"Buy signal ignored. JEV confidence was 74%, required 90%"*). This provides a complete understanding of the system's logic.
* **Notifications:** Telegram integration for receiving alerts about every executed trade right on your phone.

## ⚠️ Disclaimer

**Risk Warning:** Trading financial instruments, cryptocurrencies, and altcoins involves high risk and can result in the loss of your entire capital.

* **Educational Purpose Only:** Jev-trading is provided solely for software, analytical, and educational purposes. Nothing in this software or documentation constitutes financial, investment, legal, or trading advice.
* **No Guarantees:** Past market performance, historical backtesting metrics, and AI confidence scores do not guarantee future returns.
* **User Responsibility:** You are solely responsible for managing your financial risk, credentials, API permissions, and trade parameters. The authors and maintainers assume no liability for any direct or indirect financial losses incurred while using this application.

---

## 📄 License

Distributed under the **MIT License**
