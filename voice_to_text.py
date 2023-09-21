from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import subprocess
import json
import os

model = Model("model")
rec = KaldiRecognizer(model, 16000)
rec.SetWords(True)

class AudioProcessor:
    def __init__(self, input_audio):
        self.input_audio = input_audio

    def convert_to_wav(self):
        output_audio = f'{str(self.input_audio)[:-4]}_result.wav'
        command = ['ffmpeg', '-i', self.input_audio, '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1', output_audio]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Произошла ошибка при конвертации: {stderr.decode('utf-8')}")
        return output_audio

    def add_punctuation(self, text):
        cased = subprocess.check_output('python3 recasepunc/recasepunc.py predict recasepunc/checkpoint', shell=True,
                                        text=True, input=text)
        return cased

    def process_audio(self):
        output_audio = self.convert_to_wav()
        os.remove(self.input_audio)
        audio = AudioSegment.from_file(output_audio)
        rec.AcceptWaveform(audio.raw_data)
        result = rec.Result()
        text = json.loads(result)["text"]
        return self.add_punctuation(text)


def main():
    raw_audio = 'Sound_12125.wav'
    audio_processor = AudioProcessor(raw_audio)
    result = audio_processor.process_audio()
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == "__main__":
    main()
