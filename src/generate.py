from faster_whisper import WhisperModel
from os import PathLike
from dataclasses import dataclass

@dataclass(frozen=True)
class Subtitle:
    text: str
    start_time: float
    end_time: float
    
    @property
    def duration(self) -> float:
        return self.end_time - self.start_time
    

class Transcriber:

    def __init__(self) -> None:
        self.model = WhisperModel(
            "tiny"
        )

    def transcribe(self, audio_path: PathLike) -> tuple[list[Subtitle], list[Subtitle]]:
        transcribed, i = self.model.transcribe(audio_path)

        words = []
        segments = []

        for segment in transcribed:
            segments.append(Subtitle(text=segment.text, start_time=segment.start, end_time=segment.end))

            if not segment.words:
                continue

            for word in segment.words:
                words.append(Subtitle(text=word.word, start_time=word.start, end_time=word.end))

        return words, segments
       