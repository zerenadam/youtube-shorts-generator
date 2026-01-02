import ffmpeg
from os import PathLike

class Editor:

    def __init__(self, video_path: PathLike, audio_path: PathLike):
        self.video_path = video_path
        self.audio_path = audio_path

        self.video_stream = ffmpeg.input(self.video_path)
        self.audio_stream = ffmpeg.input(self.audio_path)
