import azure.cognitiveservices.speech as speechsdk
from pathlib import Path
import os

# Paths
base_folder_path = Path(__file__).parent
audio_folder_path = base_folder_path / "audio"
text_folder_path = base_folder_path / "text"

# Ensure directories exist
audio_folder_path.mkdir(parents=True, exist_ok=True)
text_folder_path.mkdir(parents=True, exist_ok=True)

# File paths
filename = "001"
speech_file_path = audio_folder_path / f"{filename}.mp3"
text_file_path = text_folder_path / f"{filename}.txt"

# Enter the text you want to convert to speech!
text_input = '''and that's why you don't mess with the three billy goats gruff!'''

# Write text to file
with open(text_file_path, 'w') as text_file:
    text_file.write(text_input)

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = os.environ.get('SPEECH_KEY'), os.environ.get('SPEECH_REGION')
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
speech_config.speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"

# Create an audio configuration that points to an audio file.
audio_config = speechsdk.audio.AudioOutputConfig(filename=str(speech_file_path))

# Creates a speech synthesizer using the specified audio config.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Synthesizes the received text to speech.
result = speech_synthesizer.speak_text_async(text_input).get()

# Checks result.
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to file [{}] for text [{}]".format(speech_file_path, text_input))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")
