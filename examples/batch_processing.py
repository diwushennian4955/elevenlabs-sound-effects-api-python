#!/usr/bin/env python3
"""
ElevenLabs Sound Effects — AI sound effects generation
Batch Processing Example — Process multiple inputs efficiently

Installation:
    pip install nexa-ai

Get your API key:
    https://rapidapi.com/nexaquency/elevenlabs-sound-effects/pricing

Model: elevenlabs-sound-effects
"""

import time
from nexa_ai import NexaAI

# ── Setup ──────────────────────────────────────────────────────────────────────
API_KEY = "your-api-key"

client = NexaAI(api_key=API_KEY)

# ── Batch Inputs ───────────────────────────────────────────────────────────────
inputs = [
    "Rain falling on leaves in a forest",
    "A busy coffee shop with background chatter",
    "Ocean waves on a tropical beach",
]

# ── Batch Processing ───────────────────────────────────────────────────────────
print(f"Processing {len(inputs)} audios with elevenlabs-sound-effects...")
print("-" * 60)

results = []
for i, input_text in enumerate(inputs, 1):
    print(f"[{i}/{len(inputs)}] Generating: {input_text[:50]}...")
    
    result = client.audio.speech(
        model="elevenlabs-sound-effects",
        text=input_text,

    )
    
    results.append({
        "input": input_text,
        "url": result.url,
        "job_id": result.job_id,
    })
    print(f"  ✅ Done → {result.url}")
    
    # Small delay to respect rate limits
    if i < len(inputs):
        time.sleep(0.5)

# ── Summary ────────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(f"✅ Batch complete! Generated {len(results)} audios")
print("\nResults:")
for r in results:
    print(f"  • {r['input'][:40]}...")
    print(f"    URL: {r['url']}")
