import torch
import sounddevice as sd
from silero import silero_tts
import time

language = 'ua'
model_id = 'v3_ua'
sample_rate = 48000
speaker = 'mykyta'
put_accent = True
put_yo = True
device = torch.device('cpu')

model, _ = silero_tts(language=language,
                      speaker=model_id)
model.to(device)


def tts_speak(what: str):
	audio = model.apply_tts(text=what + "..",
	                        speaker=speaker,
	                        sample_rate=sample_rate,
	                        put_accent=put_accent,
	                        put_yo=put_yo)
	sd.play(audio, sample_rate)
	time.sleep((len(audio) / sample_rate) + 0.5)
	sd.stop()
