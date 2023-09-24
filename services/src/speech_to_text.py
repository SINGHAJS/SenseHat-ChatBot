# import necessary modules for speech-to-text conversion
from google.oauth2 import service_account
from google.cloud import speech

# create a class for speech-to-text conversion
class SpeechToText:
    def __init__(self, credentials_path, 
                encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16, 
                sample_rate=44100, language_code="en-US", num_channels = 1):
        # initialize the SpeechToText class with required parameters
        
        # load Google Cloud credentials from the provided JSON file
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        
        # create a SpeechClient instance with the obtained credentials to authenticate the connection
        self.__client = speech.SpeechClient(credentials=credentials)
        
        # configure the recognition settings, such as audio encoding, sample rate, language, and channel count
        self.__config = speech.RecognitionConfig(
            encoding=encoding, sample_rate_hertz=sample_rate, language_code=language_code, audio_channel_count=num_channels)

    # define a method to transcribe an audio file to text
    def transcribe(self, file_path: str):
        text = None
        
        # load the audio file from the specified file path
        with open(file_path, 'rb') as f:
            content = f.read()
            audio = speech.RecognitionAudio(content=content)

            # transcribe the audio file using the Google Cloud Speech API
            response = self.__client.recognize(config=self.__config, audio=audio)

            # extract the transcribed text from the API response
            for result in response.results:
                text = result.alternatives[0].transcript

        # return the transcribed text
        return text
