#!/usr/bin/env python3
"""
ElevenLabs Sound Effects — AI sound effects generation
Advanced Options Example — Explore all available parameters

Installation:
    pip install nexa-ai

Get your API key:
    https://rapidapi.com/nexaquency/elevenlabs-sound-effects/pricing

Model: elevenlabs-sound-effects
"""

from nexa_ai import NexaAI

# ── Setup ──────────────────────────────────────────────────────────────────────
API_KEY = "your-api-key"

client = NexaAI(api_key=API_KEY)

print("🔧 elevenlabs-sound-effects — Advanced Options Demo")
print("=" * 60)

# ── Voice Variations ──────────────────────────────────────────────────────────
print("\n🎤 Testing different voices...")
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
sample_text = "Hello! This is a demonstration of NexaAPI text-to-speech."

for voice in voices:
    try:
        result = client.audio.speech(
            model="elevenlabs-sound-effects",
            text=sample_text,
            voice=voice,
        )
        print(f"  ✅ Voice '{voice}': {result.url}")
    except Exception as e:
        print(f"  ℹ️  Voice '{voice}': {e}")

# ── Speed Variations ───────────────────────────────────────────────────────────
print("\n⚡ Testing different speeds...")
speeds = [0.75, 1.0, 1.25, 1.5]

for speed in speeds:
    try:
        result = client.audio.speech(
            model="elevenlabs-sound-effects",
            text=sample_text,
            speed=speed,
        )
        print(f"  ✅ Speed {speed}x: {result.url}")
    except Exception as e:
        print(f"  ℹ️  Speed {speed}x: {e}")

# ── Language Support ───────────────────────────────────────────────────────────
print("\n🌍 Testing multilingual support...")
multilingual_texts = [
    ("Hello, how are you today?", "English"),
    ("Bonjour, comment allez-vous?", "French"),
    ("Hola, ¿cómo estás hoy?", "Spanish"),
    ("你好，今天怎么样？", "Chinese"),
]

for text, language in multilingual_texts:
    try:
        result = client.audio.speech(
            model="elevenlabs-sound-effects",
            text=text,
        )
        print(f"  ✅ {language}: {result.url}")
    except Exception as e:
        print(f"  ℹ️  {language}: {e}")

print("\n✅ Advanced options demo complete!")
print("📖 Full API docs: https://nexa-api.com/docs")
print("💰 Pricing: https://rapidapi.com/nexaquency/elevenlabs-sound-effects/pricing")
