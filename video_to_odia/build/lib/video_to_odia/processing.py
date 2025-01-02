import os
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from googletrans import Translator

def extract_audio_from_video(video_file):
    try:
        video = VideoFileClip(video_file)
        audio = video.audio
        base_name = os.path.splitext(video_file)[0]
        output_audio_file = f"{base_name}_audio.wav"
        audio.write_audiofile(output_audio_file)
        print(f"Audio extracted and saved as {output_audio_file}")
        return output_audio_file
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        video.close()
        audio.close()

def transcribe_audio_with_sr(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="en-US")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def save_transcription_to_file(text, audio_file):
    base_name = os.path.splitext(audio_file)[0]
    output_file = f"{base_name}_transcription.txt"
    with open(output_file, "w") as file:
        file.write(text)
        print(f"Transcription successfully saved to {output_file}")
    return output_file

def translate_text_file(input_file, src_lang='en', dest_lang='or'):
    translator = Translator()
    with open(input_file, 'r', encoding='utf-8') as file:
        text_to_translate = file.read()
    translated = translator.translate(text_to_translate, src=src_lang, dest=dest_lang)
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_odia.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated.text)
    print(f"Translation completed and saved to '{output_file}'.")
    return output_file
