"""
This module reconvert your TTS files into the newly selected voice in a batch order.
"""

import os
from pathlib import Path
import azure.cognitiveservices.speech as speechsdk  # type: ignore

# Configure your subscription key and service region
speech_key = os.getenv('SPEECH_KEY')
service_region = os.getenv('SPEECH_REGION')

# Ensure directories exist
base_folder_path = Path(__file__).parent
audio_folder_path = base_folder_path / "audio"
text_folder_path = base_folder_path / "text"
audio_folder_path.mkdir(parents=True, exist_ok=True)
text_folder_path.mkdir(parents=True, exist_ok=True)

def synthesize_speech(text, filename):
    """
    Synthesize speech from the provided text and save it to an MP3 file.

    Args:
        text (str): The text to be converted to speech.
        filename (str): The base name of the file where the audio will be saved.
    """
    audio_output_path = str(audio_folder_path / f"{filename}.mp3")

    # Create a speech config
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = 'en-US-AvaNeural'
    speech_config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat.Audio48Khz192KBitRateMonoMp3
    )

    # Create an audio configuration that points to an audio file
    audio_config = speechsdk.audio.AudioOutputConfig(filename=audio_output_path)

    # Create a synthesizer with the given settings
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    # Synthesize the text to speech
    result = synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized for text [{text}] to [{audio_output_path}]")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")

def main():
    """
    Main function to process all text files in the 'text'
    directory and generate corresponding MP3 files.

    This function iterates through all the text files in the 'text'
    directory, reads the content of each file, and calls the synthesize_speech
    function to convert the text to speech and save it as an MP3 file.
    """
    for text_file in sorted(text_folder_path.glob('*.txt')):
        filename = text_file.stem
        with open(text_file, 'r', encoding='utf-8') as file:
            text_input = file.read()
            synthesize_speech(text_input, filename)

if __name__ == "__main__":
    main()
