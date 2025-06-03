import numpy as np
import sounddevice as sd
from scipy.signal import resample

FS = 48000         # Taxa de amostragem
DURATION = 0.1     # Latência do bloco
FREQ_MOD = 70      # Frequência do oscilador robótico
PITCH_SHIFT = 0.5  # 1.0 = normal, <1.0 = mais grave

# IDs dos dispositivos: use `sd.query_devices()` se quiser selecionar
INPUT_ID = 17
OUTPUT_ID = 16

t_global = 0

def shift_pitch(audio, shift_factor):
    """Altera o pitch do áudio (sem preservar duração exata)"""
    new_len = int(len(audio) / shift_factor)
    return resample(audio, new_len)[:len(audio)]

def efeito_goiaba(audio, t0):
    t = np.linspace(t0, t0 + DURATION, len(audio))
    mod = np.sin(1 * np.pi * FREQ_MOD * t)

    # Aplica modulação robótica
    audio_mod = audio * mod

    # Aplica pitch grave
    audio_mod = shift_pitch(audio_mod, PITCH_SHIFT)

    # Distorção leve
    audio_mod = np.tanh(audio_mod * 1)

    # Ajusta tamanho final
    if len(audio_mod) < len(audio):
        audio_mod = np.pad(audio_mod, (0, len(audio) - len(audio_mod)))
    else:
        audio_mod = audio_mod[:len(audio)]

    return audio_mod

def callback(indata, outdata, frames, time, status):
    global t_global
    audio = indata[:, 0]
    audio_mod = efeito_goiaba(audio, t_global)
    outdata[:, 0] = audio_mod
    t_global += DURATION

print("Fale no microfone (Ctrl+C para parar)")

try:
    with sd.Stream(
        samplerate=FS,
        blocksize=int(FS * DURATION),
        dtype='float32',
        channels=1,
        device=(INPUT_ID, OUTPUT_ID),
        callback=callback
    ):
        input("🗣️ Fale agora! Pressione ENTER para encerrar...\n")
except KeyboardInterrupt:
    print("\n⛔ Encerrado.")
