#!/usr/bin/env python3
"""
ElevenLabs Sound Effects — AI sound effects generation

Installation:
    pip install nexa-ai

Get your API key:
    https://rapidapi.com/nexaquency/elevenlabs-sound-effects/pricing

Model: elevenlabs-sound-effects
"""

from nexa_ai import NexaAI

# ── Setup ──────────────────────────────────────────────────────────────────────
# Replace with your actual API key from https://nexa-api.com
API_KEY = "your-api-key"

client = NexaAI(api_key=API_KEY)

# ── Basic Usage ────────────────────────────────────────────────────────────────
print("Starting elevenlabs-sound-effects generation...")

result = client.audio.speech(
    model="elevenlabs-sound-effects",
    text="A thunderstorm with rain and lightning",

)

print(f"✅ Generation complete!")
print(f"   Audio url: {result.url}")
print(f"   Job ID: {result.job_id}")
print(f"   Status: {result.status}")
