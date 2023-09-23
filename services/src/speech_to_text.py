# class for speech-to-text conversion
class SpeechToText:
    def __init__(self, openai, model: str = "whisper-1"):
        self.__model = model
        self.__openai = openai

    # method to transcribe audio file to text
    def transcribe(self, file_path: str):
        with open(file_path, "rb") as f:
            transcript = self.__openai.Audio.transcribe(self.__model, f)
            text = transcript["text"]
        return text
