# Speech Recognition Automatic Translator
-----------------
## This program is a Real-Time Voice Translation System that combines Speech-to-Text (STT) and Machine Translation technologies.
It captures the user's voice input via a microphone, converts the Korean speech into text, and immediately translates it into one or more user-specified target languages (e.g., English, Japanese). The system is designed to perform continuous speech recognition using background threads, ensuring the main program flow remains uninterrupted.

## Key points

Multi-Target Translation: Capable of translating a single voice input into multiple languages simultaneously (handled as a list).
Asynchronous Processing: Utilizes the listen_in_background function to continuously detect and process voice in the background without blocking the main execution thread.
Noise Adjustment: Enhances recognition accuracy by analyzing ambient noise levels and dynamically calibrating thresholds using adjust_for_ambient_noise.
Google API Integration:
- Recognition: Leverages the Google Web Speech API (recognize_google) for high-accuracy Korean speech recognition.
- Translation: Utilizes the deep_translator library to access Google Translate services.

## Requirements

**Hardware & Network**
- Microphone: Essential for capturing voice input.
- Internet Connection: Required for communicating with Google STT and Translation servers.

**Software & Libraries (which version I tested on)**
- Python (3.8.0)
- SpeechRecognition (3.8.1): Core library for speech-to-text conversion.
- deep-translator (1.9.1): Library for multi-language translation.
- PyAudio (0.2.11): Essential dependency for accessing microphone hardware.
- setuptools: Standard Python package manager.

## Results
**user input(example) :**
```py
ex) English->en,japan->ja(Enter first two letters) Exception:Chinese(Mandarin) -> zh-cn : en, ja
Please enter audio duration : 30
```
**Process & Output :**
1. Initialization: The system pauses to adjust for ambient noise ("Noise adjustment paused" -> "Noise adjustment done").
2. Speech Recognition: The user speaks (e.g., "안녕하세요 반갑습니다").
3. Real-time Output:
```py
   Real-time Text: 안녕하세요 반갑습니다

Translation Result :
{'en': 'Hello nice to meet you', 'ja': 'こんにちは、お会いて嬉しいです'}
```
4. Termination: The program automatically stops listening after the specified duration (30 seconds).


## The Limitations
- Dependency on Connectivity: The system relies entirely on Google servers. It will not function without an internet connection (potential RequestError).
- API Limits: The recognize_google function uses a default public API key intended for testing purposes. It may have usage limits (e.g., approx. 50 requests/day) or throttling, making it unsuitable for large-scale commercial deployment.
-Latency: Since the process involves two network steps (Speech-to-Text $\rightarrow$ Translation), there is a slight delay between the user's speech and the final output.
-Sensitivity to Noise: In environments with high ambient noise or if pronunciation is unclear, the system may throw a sr.UnknownValueError (labeled as "No answer audio" in the code) and fail to translate.
