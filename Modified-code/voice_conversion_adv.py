# Import the necessary library
from TTS.api import TTS

# Initialize the TTS model for voice conversion
tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=False).to("cuda:0")

# Specify the source and target WAV file paths
source_wav = "./TTS/input/test2.wav"
target_wav = "./TTS/input/test1.wav"
output_file_path = "./TTS/output/voice_conversion/output1.wav"

# Perform voice conversion and save the output
tts.voice_conversion_to_file(source_wav=source_wav, target_wav=target_wav, file_path=output_file_path)
