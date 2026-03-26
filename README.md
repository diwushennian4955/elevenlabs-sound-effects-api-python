# ElevenLabs Sound Effects API — Python SDK

> AI-generated sound effects.

[![PyPI](https://img.shields.io/pypi/v/nexa-ai)](https://pypi.org/project/nexa-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**ElevenLabs Sound Effects** via NexaAPI — the cheapest and fastest Audio/TTS API. Starting at **$0.02/effect**.

🔗 **[Get API Key on RapidAPI](https://rapidapi.com/nexaquency/elevenlabs-sound-effects/pricing)**

## 🚀 Quick Start

```bash
pip install nexa-ai
```

```python
from nexa_ai import NexaAI

client = NexaAI(api_key="your-api-key")  # Get key at https://nexa-api.com

result = client.audio.speech(
    model="elevenlabs-sound-effects",
    text="Hello world, this is a test of AI text to speech.",
)
print(result.url)  # Direct URL to generated audio
```

## 💰 Pricing

| Model | Price | Speed |
|-------|-------|-------|
| **ElevenLabs Sound Effects** | **$0.02/effect** | Fast |

Compare with competitors:
- **Replicate**: 2-5x more expensive
- **FAL.ai**: Similar pricing, fewer models
- **Together AI**: Limited audio models

👉 **[Full pricing comparison](https://nexa-api.com/pricing)**

## 📦 Installation

```bash
# pip
pip install nexa-ai

# poetry
poetry add nexa-ai

# conda
pip install nexa-ai
```

## 🔧 Usage Examples

### Basic Audio/TTS

```python
from nexa_ai import NexaAI

client = NexaAI(api_key="your-api-key")

result = client.audio.speech(
    model="elevenlabs-sound-effects",
    text="Hello world, this is a test of AI text to speech.",
)
print(result.url)
print(result.job_id)
print(result.status)
```

### Async Usage

```python
import asyncio
from nexa_ai import AsyncNexaAI

async def main():
    client = AsyncNexaAI(api_key="your-api-key")
    result = await client.audio.speech(
    model="elevenlabs-sound-effects",
    text="Hello world, this is a test of AI text to speech.",
    )
    print(result.url)

asyncio.run(main())
```

### Using with RapidAPI

```python
from nexa_ai import NexaAI

# Use your RapidAPI key instead
client = NexaAI(
    api_key="your-rapidapi-key",
    base_url="https://elevenlabs-sound-effects.p.rapidapi.com" if model.get('rapidapi_slug') else "https://nexa-api.com",
)
```

## 🤖 Available Models

NexaAPI offers **56+ AI models** across image, video, and audio generation:

### Image Generation
Flux Schnell, Flux Dev, Flux Pro, Flux 2 Pro, Flux 2 Max, GPT-Image 1.5, Gemini 3 Pro, Stable Diffusion 3.5, SDXL, Ideogram v2, Recraft v3, and more.

### Video Generation
Kling v3 Pro, Veo 3.1, Sora 2, Minimax Video, Hunyuan Video, and more.

### Audio
ElevenLabs v3, OpenAI TTS, Kokoro TTS, Suno v4.5, Udio v2, and more.

👉 **[See all models](https://nexa-api.com/models)**

## 🔗 Links

- **Website**: [nexa-api.com](https://nexa-api.com)
- **API Docs**: [nexa-api.com/docs](https://nexa-api.com/docs)
- **Pricing**: [nexa-api.com/pricing](https://nexa-api.com/pricing)
- **RapidAPI**: [rapidapi.com/nexaquency](https://rapidapi.com/nexaquency)
- **PyPI**: [pypi.org/project/nexa-ai](https://pypi.org/project/nexa-ai/)
- **npm**: [npmjs.com/package/nexa-ai](https://www.npmjs.com/package/nexa-ai)

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Keywords**: ElevenLabs Sound Effects API, ElevenLabs Sound Effects Python, ElevenLabs Sound Effects API pricing, cheapest ElevenLabs Sound Effects API, Audio/TTS API, AI API, NexaAPI, text to image API, AI image generation
