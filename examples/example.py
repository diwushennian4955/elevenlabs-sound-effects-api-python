#!/usr/bin/env python3
"""
ElevenLabs Sound Effects — Audio Generation Example
Using NexaAPI Python SDK

Get your API key at: https://nexa-api.com
"""

from nexa_ai import NexaAI

# Initialize client
client = NexaAI(api_key="your-api-key")

# Generate audio
print("Generating audio with ElevenLabs Sound Effects...")
result = client.audio.speech(
    model="elevenlabs-sound-effects",
    text="Hello! This is a demonstration of the ElevenLabs Sound Effects text-to-speech API via NexaAPI.",
)

print(f"✅ Audio generated!")
print(f"   URL: {result.url}")
print(f"   Job ID: {result.job_id}")
