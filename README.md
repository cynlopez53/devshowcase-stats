# DevShowcase Stats

**DevShowcase Stats** is a modular, JSON-first tool designed to analyze numerical input and return structured statistics. Built for agent platforms like Relevance AI and OpenAgents, it supports multiple modes, verbose commentary, and clean error handling.

## 🔧 Features

- Accepts JSON input with keys:
  - `numbers`: list of numbers
  - `verbose`: optional boolean
  - `mode`: optional string (`basic`, `normalize`, `cumsum`, `variance`, `std`)
- Computes core stats: `count`, `sum`, `mean`, `median`, `min`, `max`
- Applies mode-specific logic (e.g., normalization, cumulative sum)
- Returns structured JSON output
- Optional natural language summary if `verbose` is `true`

## 📥 Example Input

```json
{
  "numbers": [1, 2, 3],
  "verbose": true,
  "mode": "normalize"
}
## 💳 Usage & Credit System

DevShowcase agents run on Relevance AI’s credit-based infrastructure. Here’s how usage works:

| Feature Type         | Description                              | Credit Cost |
|----------------------|------------------------------------------|-------------|
| Basic stats          | Count, sum, mean, median, etc.           | 1 credit    |
| Mode: normalize      | Scales values between 0–1                | 3 credits   |
| Mode: cumsum         | Returns cumulative sum array             | 3 credits   |
| Mode: variance/std   | Computes statistical dispersion          | 5 credits   |
| Verbose summary      | Adds natural language explanation        | +2 credits  |
| File upload (if enabled) | Parses and analyzes uploaded data   | 10 credits  |

**Note:** Credits are consumed per request. If you run out, Relevance AI will prompt you to top up.
> ⚡ DevShowcase includes premium features. See usage table below for credit costs.

To purchase credits, visit [Relevance AI](https://relevanceai.com).
## ❓ Monetization FAQ

**Q: Do I need credits to use DevShowcase?**  
A: Basic features are free. Premium features require credits.

**Q: How do I get credits?**  
A: You can purchase credits via Relevance AI’s dashboard.

**Q: What happens if I run out of credits?**  
A: You’ll be prompted to top up before accessing premium features.
