# 🎙️ Advanced AI Speech Recognition
## Powered by OpenAI Whisper & Transformer Architecture

This application captures live human speech and converts it into high-accuracy text using a deep-learning transformer model.

---

### 🧠 Why this is "Advanced"

#### 1. Robustness to Noise
Traditional STT relied on simple frequency matching. Whisper was trained on 680,000 hours of labeled audio data, allowing it to "ignore" background noise like fans, typing, or traffic.

#### 2. Automatic Language Detection
Whisper automatically detects the language being spoken. You can speak in Spanish, and the model will realize it's Spanish and transcribe it correctly without any code changes.

#### 3. Feature Engineering: Mel Spectrograms
The project involves converting raw time-domain audio (waves) into frequency-domain data (spectrograms) using **Fourier Transforms**. This is the fundamental math behind all modern audio AI.

---

### 🚀 Level-Up Challenges
* **Real-time Streaming**: Instead of 5-second chunks, use a rotating buffer for seamless scrolling text.
* **Translation**: Change the transcribe call to `model.transcribe(audio, task="translate")` to speak in one language and see the text in English instantly.