import io
from google.oauth2 import service_account
from google.cloud import speech

# construct the speech client object to connect to the speech endpoint
client_file = "sa_speech_recognition.json" 
credentials = service_account.Credentials.from_service_account_file(client_file) # pass client file to credentials object
client = speech.SpeechClient(credentials=credentials) # authenticate the connection

# Load the audio file
audio_file = "Speech_Recognition_Audio.wav"
with io.open(audio_file, 'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = 44100,
    language_code = "en-US",
    audio_channel_count = 2
)

# transcribe audio file
response = client.recognize(config=config, audio=audio)
print(response)
for result in response.results:
    print(result.alternatives[0].transcript)

