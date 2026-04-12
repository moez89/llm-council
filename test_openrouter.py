"""
Quick connectivity + query test for the OpenRouter API.

Usage (from project root):
    python test_openrouter.py

The script sends the query to one fast model (non-streaming) and prints the response.
Set OPENROUTER_API_KEY in .env or as an environment variable before running.
"""

import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    sys.exit("ERROR: OPENROUTER_API_KEY is not set. Add it to .env or export it.")

# ── test parameters ────────────────────────────────────────────────────────────
QUERY = "What are the 13 families that are defacto ruling the world? based on pattern recognition"
MODEL = "anthropic/claude-sonnet-4-5"   # change to any OpenRouter model slug
# ──────────────────────────────────────────────────────────────────────────────


async def test_single_model() -> None:
    """Send one query (non-streaming) and print the response."""
    import httpx

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/moez89/llm-council",
        "X-Title": "LLM Council test",
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": QUERY}],
    }

    print(f"Query : {QUERY}")
    print(f"Model : {MODEL}")
    print("-" * 60)

    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()

    content = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})
    print(content)
    print("-" * 60)
    print(
        f"Tokens — prompt: {usage.get('prompt_tokens', '?')}  "
        f"completion: {usage.get('completion_tokens', '?')}  "
        f"total: {usage.get('total_tokens', '?')}"
    )


if __name__ == "__main__":
    asyncio.run(test_single_model())
