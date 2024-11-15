import torch
from TTS.api import TTS
import os

def voice_cloning(text, speaker_wav, language, output_path):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
    tts.tts_to_file(text=text, speaker_wav=speaker_wav, language=language, file_path=output_path)
    print(f"Generated voice cloning audio saved to {output_path}")

if __name__ == "__main__":

    voice_cloning("This is voice cloning.", "./TTS/input/test1.wav", "en", "./TTS/output/adaptive_target1.wav")

