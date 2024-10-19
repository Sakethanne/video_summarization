import os
import google.generativeai as genai # type: ignore

# Configure the generative AI model with the API key from environment variables
genai.configure(api_key=os.environ["API_KEY"])

from youtube_transcript_api import YouTubeTranscriptApi # type: ignore
import re

# Function to extract the video ID from a YouTube URL
def get_video_id(youtube_url):
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', youtube_url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

# Function to get the transcript of a YouTube video using its URL
def get_transcript(youtube_url):
    try:
        video_id = get_video_id(youtube_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        return f"Error: {e}"

# Function to clean the transcript and remove timestamps
def clean_transcript(transcript):
    lines = transcript.strip().split('\n')
    cleaned_lines = [line.split(':', 1)[1].strip() for line in lines if ':' in line]
    cleaned_text = ' '.join(cleaned_lines)
    return cleaned_text

# Replace with your YouTube video URL
youtube_url = input("Enter the Video URL: ")# 'https://www.youtube.com/watch?v=AUBV-6E_rXY'

# Get the transcript of the YouTube video
transcript = get_transcript(youtube_url)
text = ""
if isinstance(transcript, list):
    for entry in transcript:
        text += entry['text'] + " "
else:
    print(transcript)

# Clean the transcript to remove timestamps
cleaned_text = clean_transcript(text)

# Configuration for the generative AI model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 2000,
    "response_mime_type": "text/plain",
}

# Create the generative AI model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session with the model
chat_session = model.start_chat()

# Create a prompt for the model to summarize the transcript
prompt = "Summarize the following in about a maximum of 2000 characters: " + text

# Send the prompt to the model and get the response
response = chat_session.send_message(prompt)

# Print the response from the model
print(response.text)