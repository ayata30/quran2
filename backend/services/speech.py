from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech


PROJECT_ID = "qurandetect"

# Instantiates a client
client = SpeechClient()

# Reads a file as bytes
'''
with open("resources/audio.wav", "rb") as f:
    audio_content = f.read()
    '''

def transcribe_audio(audio_bytes: bytes) -> str:
    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
    #encoding=cloud_speech.ExplicitDecodingConfig.AudioEncoding.LINEAR16,
    #sample_rate_hertz=16000,
   # audio_channel_count=1,

        language_codes=["ar-SA"],
        model= "latest_short",

)

    request = cloud_speech.RecognizeRequest(
    recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
    config=config,
    content=audio_bytes,
)

# Transcribes the audio into text
    response = client.recognize(request=request)

    if not response.results:
        return "no transcript found"

    return response.results[0].alternatives[0].transcript

'''
for result in response.results:
    print(f"Transcript: {result.alternatives[0].transcript}")
    '''