from dotenv import load_dotenv

load_dotenv()
def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=22050,
        language_code="en-US",
    )
    print("before long_running_recognize")

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result()

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    transcript = []
    for result in response.results:
        transcript.append(result.alternatives[0].transcript)
        
    print("".join(transcript))
    return "".join(transcript)
