import vosk
import sys
import sounddevice as sd
import queue
import json

model = vosk.Model("model")

q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def stt_listen(callback):
    with sd.RawInputStream(samplerate=16000, blocksize=8000, device=1, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])