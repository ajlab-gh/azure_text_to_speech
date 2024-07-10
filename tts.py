from pathlib import Path
from openai import OpenAI
import warnings

# Ignore DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Paths
base_folder_path = Path(__file__).parent
audio_folder_path = base_folder_path / "audio"
text_folder_path = base_folder_path / "text"

# File paths
filename = "001"
speech_file_path = audio_folder_path / f"{filename}.mp3"
text_file_path = text_folder_path / f"{filename}.txt"

# Text input
text_input = '''and that's why you don't mess with the three billy goats gruff!'''

# Write text to file
with open(text_file_path, 'w') as text_file:
    text_file.write(text_input)

# Initialize OpenAI client
client = OpenAI()

# Generate Speech from Text
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="shimmer",
  input= text_input
)

response.stream_to_file(speech_file_path)
