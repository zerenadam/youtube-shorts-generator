import ffmpeg
from os import PathLike, makedirs
from generate import Subtitle

class Editor:

    def __init__(self, video_path: PathLike, audio_path: PathLike) -> None:
        self.video_path = video_path
        self.audio_path = audio_path

        self.video_stream = ffmpeg.input(self.video_path)
        self.audio_stream = ffmpeg.input(self.audio_path)


    def burn_subtitles(self, subtitles: tuple[list[Subtitle], list[Subtitle]]):
        words, segments = subtitles
        video = self.video_stream

        for word in words:
            video = video.drawtext(
                text=word.text,
                fontsize=80,
                fontfile="src/font/TikTokSans-ExtraBold.ttf",
                color='white',
                x='(w-text_w)/2',
                y='(h=text_h)/2',
                enable=f"between(t, {word.start_time}, {word.end_time})"
            )
        
        return video
