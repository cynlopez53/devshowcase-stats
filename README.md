# DevShowcase Stats

**DevShowcase Stats** is a modular, JSON-first tool designed to analyze numerical input and return structured statistics. Built for agent platforms like Relevance AI, it supports multiple modes, verbose commentary, and clean error handling.

## Features

- Accepts JSON input with keys:
  - `numbers`: list of numbers
  - `verbose`: optional boolean
  - `mode`: optional string (`basic`, `normalize`, `cumsum`, `variance`, `std`)
- Computes core stats: count, sum, mean, median, min, max
- Applies mode-specific logic (e.g., normalization, cumulative sum)
- Returns structured JSON output
- Optional natural language summary if `verbose` is true

## Example Input

```json
{
  "numbers": [1, 2, 3],
  "verbose": true,
  "mode": "normalize"
}
