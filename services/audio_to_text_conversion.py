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

# ----------------FROM GOOGLE---------------------

# import io
# from google.oauth2 import service_account
# from google.cloud import speech

# def transcribe_model_selection(
#     speech_file: str,
#     model: str,
# ) -> speech.RecognizeResponse:
#     """Transcribe the given audio file synchronously with
#     the selected model."""
#     # construct the speech client object to connect to the speech endpoint
#     client_file = "sa_speech_recognition.json" 
#     credentials = service_account.Credentials.from_service_account_file(client_file) # pass client file to credentials object
#     client = speech.SpeechClient(credentials=credentials) # authenticate the connection

#     with open(speech_file, "rb") as audio_file:
#         content = audio_file.read()

#     audio = speech.RecognitionAudio(content=content)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="en-US",
#         model=model,
#     )

#     response = client.recognize(config=config, audio=audio)

#     for i, result in enumerate(response.results):
#         alternative = result.alternatives[0]
#         print("-" * 20)
#         print(f"First alternative of result {i}")
#         print(f"Transcript: {alternative.transcript}")

#     return response

# if __name__ == "__main__":
#     transcribe_model_selection("Speech_Recognition_Audio.wav", "default")

# --------------------------------------------------------------------------------------
# from google.cloud import speech_v1p1beta1 as speech
# from google.oauth2 import service_account
# import io

# audio_file_path = 'Speech_Recognition_Audio.wav'

# def transcribe_audio():
#     # construct the speech client object to connect to the speech endpoint
#     client_file = "sa_speech_recognition.json" 
#     credentials = service_account.Credentials.from_service_account_file(client_file) # pass client file to credentials object
#     client = speech.SpeechClient(credentials=credentials) # authenticate the connection

#     with io.open(audio_file_path, 'rb') as audio_file:
#         content = audio_file.read()

#     audio = speech.RecognitionAudio(content=content)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,  # Update this if your audio has a different sample rate.
#         language_code="en-US"  # Update this for your language.
#     )

#     response = client.recognize(config=config, audio=audio)

#     for result in response.results:
#         print("Transcript: {}".format(result.alternatives[0].transcript))

# if __name__ == "__main__":
#     transcribe_audio()
