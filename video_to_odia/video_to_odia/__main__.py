import argparse
from .processing import extract_audio_from_video, transcribe_audio_with_sr, save_transcription_to_file, translate_text_file

def main():
    parser = argparse.ArgumentParser(description="Process video files and translate transcriptions.")
    parser.add_argument("video_file", help="Path to the video file.")
    args = parser.parse_args()

    video_file = args.video_file
    audio_file = extract_audio_from_video(video_file)
    if audio_file:
        text = transcribe_audio_with_sr(audio_file)
        if text:
            text_file = save_transcription_to_file(text, audio_file)
            translate_text_file(text_file, src_lang="en", dest_lang="or")

if __name__ == "__main__":
    main()
