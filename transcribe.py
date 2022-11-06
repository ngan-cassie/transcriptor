from dotenv import load_dotenv

load_dotenv()
def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=44100,
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
        """ 
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))
        """
        transcript.append(result.alternatives[0].transcript)
    print("".join(transcript))
    return "".join(transcript)

# text = transcribe_gcs("gs://transcriber_audio_files/A one minute TEDx Talk for the digital age | Woody Roseland | TEDxMileHigh.mp3")
# print(text)