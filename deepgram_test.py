import asyncio, os, json
from dotenv import load_dotenv
from deepgram import Deepgram
from pprint import pprint

load_dotenv()
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')

def main():
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    with open('1280.mp4', 'rb') as file_to_transcribe:
        source = { 'buffer': file_to_transcribe, 'mimetype': 'video/mp4'}
        transcription_options = { 'punctuate': True, 'paragraphs': True, 'summarize': True}
        response = deepgram.transcription.sync_prerecorded(source, transcription_options)
        pprint(response)

transcript = main()

