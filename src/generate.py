from faster_whisper import WhisperModel
from os import PathLike
from dataclasses import dataclass


@dataclass
class Subtitle:
    start_time: float
    end_time: float
    text: str
    

class Transcriber:

    def __init__(self) -> None:
        self.model = WhisperModel(
            "tiny"
        )

    def transcribe(self, audio_path: PathLike) -> list[Subtitle]:
        transcribed, i = self.model.transcribe(audio_path)

        out = []

        for segment in transcribed:

            if not segment.words:
                continue

            for word in segment.words:
                out.append(Subtitle(word.start, word.end, word.word))

        return out